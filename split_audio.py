from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import db_to_float


sound = AudioSegment.from_mp3("sample_30844.mp3")
average_loudness = sound.rms

#计算当前音频静音大小
silence_threshold = average_loudness * db_to_float(-30)

chunks = split_on_silence(sound,
    # 静音片段的持续时间
    min_silence_len=30,

    # 切割片段的静音大小 -16 dBFS
    silence_thresh=-16
 )


print(len(chunks))

#分片保存到文件中
for i, chunk in enumerate(chunks):
    chunk.export("temp/{}.mp3".format(i), format="mp3")