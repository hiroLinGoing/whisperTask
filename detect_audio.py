import whisper
#不需要简繁体转换则不需要暗转
from zhconv import convert_for_mw

model = whisper.load_model("large-v2", download_root='openai/whisper-large-v2/')

result = model.transcribe("sample_30844.mp3", word_timestamps=True)
# print(result["text"])

with open('result.txt', 'w', encoding='utf8') as f:
    for item in result['segments']:
        #如果需要转换繁体的话，使用zhconv
        #f.write(convert_for_mw(item['text'], 'zh-hans'))
        f.write(item['text'])


## 如果需要自定义音频长度的话 使用这里的进行切割
# from pydub import AudioSegment
# from pydub.silence import split_on_silence
# from pydub.utils import db_to_float
#
#
# sound = AudioSegment.from_mp3("sample_30844.mp3")
# average_loudness = sound.rms
# silence_threshold = average_loudness * db_to_float(-30)
#
# chunks = split_on_silence(sound,
#     # 静音片段的持续时间
#     min_silence_len=30,
#
#     # 切割片段的静音大小 -16 dBFS
#     silence_thresh=-16
#  )
# print(len(chunks))
#
# for i, chunk in enumerate(chunks):
#     chunk.export("mp3_temp2/{}.mp3".format(i), format="mp3")