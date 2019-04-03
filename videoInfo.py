"""
Author:         Benjamin Thomas
Major:          Software Development
Creation Date:  April 5th, 2019
Due Date:       April 5th, 2019
Course:         Independent Study
Professor:      Dr. Frye
Filename:       videoInfo.py
Purpose:        Class file that will read a video file and create an object with
                the video's filename, start time, end time, and clip duration.
"""

import os
import platform
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
        dt = datetime.datetime.fromtimestamp(c)
        return dt

    def creationTime(self, p):
        stat = os.stat(p)
        return stat.st_mtime

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

    """
    function __init__(self, filename)
    params:
        filename - string: the video file to read
    Desciption:
        Reads the file and stores the information
    """
    def __init__(self, filename):
        fileData = pymediainfo.MediaInfo.parse(filename)
        videoData = fileData.tracks[1]

        self.startstring = self.creationTime(filename)
        self.durationstring = videoData.to_data()["other_duration"][3]

        self.filename = filename
        self.start = self.startToDateTime(self.startstring)
        self.duration = self.durationToTimeDelta(self.durationstring)
        self.end = self.start + self.duration

    """
    function __str__(self)
    Desciption:
        Overrides string operator and displays the video information
    """

    def __str__(self):
        return "Filename:\t\t" + self.filename + "\nFile start:\t\t" + str(self.start) + "\nFile Duration:\t\t" + str(self.duration) + "\nFile End:\t\t" + str(self.end)
