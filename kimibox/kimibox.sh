#!/bin/bash

source kimibox.cnf
while :
do
   if [ -e "$mp3_filename" ]; then
	current_time=$(date "+%Y%m%d-%H%M%S")
	new_filename=$boxid"-"$current_time.mp3

	#write id3 tag for audit
	eyeD3 -a "$boxid" -A "KIMI Platform" -t "$current_time" $mp3_filename

	#write the new file
	cp $mp3_filename $search_dir/$new_filename
	#TODO: check if written file is error
	echo "Write $new_filename .. done."
   fi
   sleep $waitingtime
done

#upload to server
#curl -F "kimi=@$new_filename" $post_url

