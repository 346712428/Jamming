from threads.anc import ActiveNoiseControl
import settings
import numpy as np
import matplotlib.pyplot as plt
from utils.codec import Codec
import wave

def run():
    anc_thread = ActiveNoiseControl(
        settings.OUT_FS, settings.IN_FS,
        settings.CHIRP_LENGTH + settings.NOISE_LENGTH,
        settings.SIMULATION_LENGTH)
    # 实际接收到train信号
    reality = np.load('C:/Users/Tango/Documents/GitHub/Jamming/test_data/train_x0.npy')
    # 噪声库中的噪声
    ideal = np.load('C:/Users/Tango/Documents/GitHub/Jamming/test_data/train_y0.npy')
    # 信道估计
    anc_thread.channel_simulation(reality, ideal)
    ideal_audio = np.array([])
    for i in range(0, 10):
        # 实际接收到的test信号
        receive_path = "C:/Users/Tango/Documents/GitHub/Jamming/test_data/test_x" + str(i) + ".npy"
        receive = np.load(receive_path)
        # 噪声库中的噪声
        noise_path = "C:/Users/Tango/Documents/GitHub/Jamming/test_data/test_y" + str(i) + ".npy"
        noise = np.load(noise_path)
        # 噪声消除
        temp = anc_thread.eliminate_noise(receive, noise)
        ideal_audio = np.append(ideal_audio, temp)
    print(ideal_audio)
    audio = Codec.encode_audio_to_bytes(ideal_audio, 1, 16)
    f = wave.open("test.wav", "wb")
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(48000)
    f.writeframes(audio)

    # H = anc_thread.H
    # # n = min(ideal.size, H.size)
    # n = 2000
    # ideal = ideal[:n]
    # H = H[:n]
    # combine = ideal * H
    # n = combine.size
    # y = np.arange(0, n)
    # fig = plt.figure()
    # ax = fig.add_subplot(111)
    # ax.scatter(y, combine, s=1, marker='.')
    # plt.show()