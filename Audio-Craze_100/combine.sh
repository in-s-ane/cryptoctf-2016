#!/bin/bash

# exiftool -track *.mp3
# sort by track number
tracks="bygveicymawvushj.mp3
anxvjsvdzpyajcmm.mp3
ginsbaofhohjjyqu.mp3
oqeenzhoivtgiylj.mp3
reapdkteeheswjho.mp3
puuuuomspbyqchnq.mp3
vifwihaachnbpirr.mp3
gzwagwjwjgxpahrp.mp3
emibcegjajfsvzpy.mp3
asxrrodzdhhlthgz.mp3
pstydhlpxzbyxjmq.mp3
uicxorlnamlraypq.mp3
psyystvnbtpaukzi.mp3
jjjbiuwwiyyiludw.mp3
fbtseyuswdfjppnr.mp3
wlnxcdsfzlvgjkov.mp3
gjoynhvcetnnkncr.mp3
lkfjxutekoqdgfnf.mp3"

rm -rf combined.mp3

for track in $tracks; do
    cat "$track" >> combined.mp3
done
