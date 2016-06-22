#!/bin/sh

#source kimi.cnf
BOXID=3579
WAIT_TIME=20
POST_URL=http://188.166.248.198/kimi/upload.php

RECORD_QUALITY=dat
RECORD_TIME=10
THRESHOLD_AMPLITUDE=0.2

record_file=/dev/shm/record
#store the file to ram
card=$(arecord -l | grep "card 1")
if [ -z "$card" ]; then
  echo "no sound card detected"
  exit
fi
export AUDIODEV=hw:1,0
amixer -c 1 sset 'Mic' 90%

while :
do
  sox -r 44100 -d $record_file.2.wav  trim 0 0:05
#  arecord  -f $RECORD_QUALITY -d $RECORD_TIME -D plughw:1 $record_file.2.wav
  sox $record_file.2.wav -c 1 $record_file.wav
  amplitude=$(sox -t .wav $record_file.wav -n stat 2>&1|grep "Maximum amplitude"|awk -F':' '{print $2}'|tr -d '[[:space:]]')
  echo "max amplitude:$amplitude"
  if [ $(echo "$amplitude > $THRESHOLD_AMPLITUDE"|bc) -eq "1" ]; then
    timestamp=$(date +"%s")
    lame --quiet -V4 --ta "$BOXID" --tl "KIMI Platform" --tt "$timestamp" $record_file.wav $record_file.mp3

    current_time=$(date "+%Y%m%d-%H%M%S")
	  filename=$BOXID"-"$current_time.mp3
    echo "uploadding $filename"
    curl -F "kimi=@$record_file.mp3" -F "namafile=$filename" $POST_URL
    rm $record_file.mp3
  fi
  sleep $WAIT_TIME
done
