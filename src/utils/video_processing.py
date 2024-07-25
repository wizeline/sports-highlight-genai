import os
import urllib.request 
import manage_files_s3
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
#clip with name suffix final.mp4 will trigger the lambda
def create_clip_from_video(videoName,startTimestamp,endTimestamp, clipName):
    #placeholder, using presigned url
    videoPath=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'clips'))
    videoName=videoPath+'\\matchVideo.mp4'
    clipName=videoPath+'\\'+clipName
    ffmpeg_extract_subclip(videoName,startTimestamp,endTimestamp,targetname=clipName)

    



