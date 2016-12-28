# from ffmpy import *
#
#
# class Concatenator:
#
#     def __init__(self):
#         self.ffmpeg_command1 = ["ffmpeg", "-i", "/home/xincoz/test/connect.webm", "-acodec", "copy", "-ss", "00:00:00", "-t", "00:00:30", "/home/xincoz/test/output1.webm"]
#         self.ffmpeg_command2 = ["ffmpeg", "-i", "/home/xincoz/test/connect.webm", "-acodec", "copy", "-ss", "00:00:30", "-t", "00:00:30", "/home/xincoz/test/output2.webm"]
#         self.ffmpeg_command3 = ["mencoder", "-forceidx", "-ovc", "copy", "-oac", "pcm", "-o", "/home/xincoz/test/output.webm", "/home/xincoz/test/output1.webm", "/home/xincoz/test/output2.webm"]
#
#
# subprocess.call(ffmpeg_command1)
# subprocess.call(ffmpeg_command2)
# subprocess.Popen(ffmpeg_command3)