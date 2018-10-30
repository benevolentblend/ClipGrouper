import os
import datetime
from videoInfo import VideoInfo

videoFiles = []
gaps = []
gapsum = datetime.timedelta()

for f in os.listdir('videofiles'):
    if f.endswith('.MP4'):
        file = VideoInfo('videofiles/' + f)
        print file.filename
        videoFiles.append(file)

print len(videoFiles)

sortedFiles = sorted(videoFiles, key=lambda vf: vf.start)

print "should print all files except last one"

# itterate with i over sortedFiles except for last file
for i, file1 in enumerate(sortedFiles[:-1]):
    file2 = sortedFiles[i + 1]
    gap = file2.start - file1.end
    gapsum += gap
    print gap
    gaps.append(gap)

gapavg = gapsum / len(gaps)

print "New group for " + sortedFiles[0].filename
for i, gap in enumerate(gaps):
    nextClip = sortedFiles[i + 1]
    if gap < gapavg:
        print "\t" + nextClip.filename
    else:
        print "New group for " + nextClip.filename
