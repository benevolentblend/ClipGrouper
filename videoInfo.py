import pymediainfo
import datetime
import re

class VideoInfo:
    """
    function startToDateTime(c)
    params:
        c - string: The creation date
    Desciption:
        Converts a string in a datetime
    """
    def startToDateTime(self, c):
        dt = datetime.datetime.strptime(c, "UTC %Y-%m-%d %H:%M:%S")
        return dt

    """
    function durationToTimeDelta(c)
    params:
        d - string: The duration
    Desciption:
        Converts a string in a timedelta
    """
    def durationToTimeDelta(self, d):
        result = re.match('(\d{2}):(\d{2}):(\d{2}).(\d{3})', d)

        hours = int(result.group(1))
        minutes = int(result.group(2))
        seconds = int(result.group(3))
        milliseconds = int(result.group(4))
        t = datetime.timedelta(0, seconds, 0, milliseconds, minutes, hours)
        return t

    def __init__(self, filename):
        fileData = pymediainfo.MediaInfo.parse(filename)
        videoData = fileData.tracks[1]

        self.startstring = videoData.to_data()["encoded_date"]
        self.durationstring = videoData.to_data()["other_duration"][3]

        self.filename = filename
        self.start = self.startToDateTime(str(self.startstring))
        self.duration = self.durationToTimeDelta(self.durationstring)
        self.end = self.start + self.duration

    def __str__(self):
        return "File start:\t\t" + str(self.start) + "\nFile Duration:\t\t" + str(self.duration) + "\nFile End:\t\t" + str(self.end)
