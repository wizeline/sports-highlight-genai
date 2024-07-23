import os
import urllib.request 
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# videoName : str
#       Path to the file from which the subclip will be extracted.
# startTimestamp : float
#       Moment of the input clip that marks the start of the produced subclip.
# endTimestamp : float
#       Moment of the input clip that marks the end of the produced subclip.
# clipName : str, optional
#       Path to the output file. Defaults to
#       ``<inputfile_name>SUB<start_time>_<end_time><ext>``.
def create_clip_from_video(videoName,startTimestamp,endTimestamp, clipName)
#placeholder, using presigned url
videoPath=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'clips'))
videoName=videoPath+'\\video.mp4'
clipName=videoPath+'\\clip1.mp4'
urllib.request.urlretrieve("https://wc-highlights-videostorage.s3.us-east-2.amazonaws.com/MLB%20Arizona%20Diamondbacks%20vs%20Los%20Angeles%20Dodges%20FULL%20GAME%20-%2002.07.2024%20%28360p_30fps_H264-96kbit_AAC%29.mp4?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMiJHMEUCIFIUgbuVqZsvUYHf5SLy4aYek7q4Y8xeRtVk2oOUEty1AiEAxMFZ%2FOPb0zDdokLuSpmtv5ZOk9jSBrCW8i1bv0YeTm0qpAMIYhAAGgw4OTEzNzcyOTc3MDgiDKtcyEsKRygk3nVbpiqBA9obafhcxkvytyScNn%2FrWFsGDQw4NvldnCE8NPcAf%2FoNvLe5htNzcSv1JxxeHgfZZpmmRtmrl2sVfEdACgf14GeSrciAXqc185uo29rX5NFZUCxBJVl5eHg%2FSh%2Bd43TarWt6kBlg7TeKZyd0MnXBpHp01EZbg8hLkEOm18GR2gEBnHWciFfsFzU%2Fi5pUmMShRIvU4fcrSpqnr3fkZg%2Fthf%2FY2qplBB1sgybF%2FJLo7usSfmnpn1j2SY5IS7irT66LmmGaRnMxZSHDDuBISiYHrnjbtYLtLvskBOTsEi6OxPGh0nnA%2B%2FBCrn6qnoZQ18DTTc5ybJadcA0IAOJn2olamxxJcxb6kCuQIJuvlFHKOIMsaXTRI8k6Y1YcyIXtEMQrkMvJ9bJ7O3vp9zgSubA9jG%2B4vKIy8KxceEaOXy%2FA5wiPe%2FjaA8jFBHyJay1xbxuRlFSM8f5xKaNB0%2FDvQmUEXhpRhod5fCJE%2BX6KMDug4sHKJ4r7kt92M1nnVq%2B5wWpWfVQwsIX1tAY6hAID3i6avF33DkDMobwM%2BKlY33af62lwU7BQE6GZgGOB7SC9nyfbSd4NeNFNL2Ezh6LMzDDOsXKUMEipYCSo1JoCJsznWDHhD1zOnyhJ6%2Fx39tyXrUhoFkcRMa5K1m8NorrZ1PiJEp5W6WIiOcSDWyMgxyX7nkvdzlF6nbpD9bNPwAsHlA2%2BxUaV%2BWkIg%2BnuVKpMU1BqY8Og%2B%2Ft8rsIySrLOha6M7oigP%2BT5iwpjEQOfQ2DkuofYQmjU97aGCBn2aTfo4uSb%2FsdyB5ZVw0l84NKdLKLt0XRzLYlbkktWx%2B8coBeAhw5yaEr5t6qq9XNEkNRsyxoA8xfSupK9Z8V3o0%2FwjmZ%2BUA%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240721T210418Z&X-Amz-SignedHeaders=host&X-Amz-Expires=10800&X-Amz-Credential=ASIA47CR2FEWBVGKWYMA%2F20240721%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Signature=ee01aab7a5b7d82690e46faab6710e450265c1fb8894c1048009a27d06abda98",videoName)
ffmpeg_extract_subclip(videoName,10,50,targetname=clipName)


