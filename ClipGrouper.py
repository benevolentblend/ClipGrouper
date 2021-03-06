"""
Author:         Benjamin Thomas
Major:          Software Development
Creation Date:  April 5th, 2019
Due Date:       April 5th, 2019
Course:         Independent Study
Professor:      Dr. Frye
Filename:       CliperGrouper.py
Purpose:        The program will look in the directory passed for mp4 or mov files,
                then use mediainfo to lookup and store the information about the video
                files. Once sorted, the program will measure the gaps between the videos
                and display an estimate for how the video clips should be grouped.
"""

import os
import datetime
import argparse
from videoInfo import VideoInfo

# Usuage funtion and arugment parser
parser = argparse.ArgumentParser(description="Groups related video files (mov or mp4) in a directory based off the gaps in between.")
parser.add_argument("directory", help="directory with video files")
parser.parse_args()
args = parser.parse_args()

directory = args.directory

if not os.path.isdir(directory):
    quit("The directory '" + directory + "' does not exist.")

if not directory.endswith("/"):
    directory = directory + "/"


videoFiles = []
gaps = []
gapsum = datetime.timedelta()

# Loop though files in directory and store the video info
for f in os.listdir(directory):
    if f.lower().endswith('.mp4') or f.lower().endswith('.mov'):
        file = VideoInfo(directory + f)
        videoFiles.append(file)

if len(videoFiles) < 1:
    quit('No video files in the directory')

# sort the files by their start value
sortedFiles = sorted(videoFiles, key=lambda vf: vf.start)

# itterate with i over sortedFiles except for last file
for i, file1 in enumerate(sortedFiles[:-1]):
    file2 = sortedFiles[i + 1]
    gap = file2.start - file1.end
    gapsum += gap
    #print file1
    print "Video Gap between " + str(i) +  " and " + str(i + 1) + ": " + str(gap)

    gaps.append(gap)

gapavg = gapsum / len(gaps)

print "Avg Gap: %s\n" % str(gapavg)

print "New group:\n\t" + sortedFiles[0].filename
for i, gap in enumerate(gaps):
    nextClip = sortedFiles[i + 1]
    if gap < gapavg:
        print "\t" + nextClip.filename
    else:
        print "New group:\n\t" + nextClip.filename
