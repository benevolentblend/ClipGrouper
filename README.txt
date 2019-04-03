# ClipGrouper
Groups MP4 files in videofiles directory based on the time gaps inbetween the videos.

## Dependencies

- Python 2.7+
- [pymediainfo](https://pypi.org/project/pymediainfo/)

##VideoInfo.py

This file acts as a class file that stores information about a video file.
Using a python mediainfo wrapper, it extracts video meta data to determine when
the clip was encoded, and the duration. Then it calculates the "end" point of
the clip. The resulting object contains the filename, start, end, and duration
of the video file.

##ClipGrouper.py

This is the main project file. It will read a file directory passed to it and
group the files based of the the gaps in between.

The grouping algorithm works by comparing the gaps in between the videos, and
finds the average gap time. Any gap that is above the average will indicate the
start of a new group.

##Known Issues

In some cases were videos were recorded back to back, the start and end times of clips
may overlap, due to when the camera encoded the files.
