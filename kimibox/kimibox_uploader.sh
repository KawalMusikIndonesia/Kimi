#!/bin/bash
# Kimi uploader 1.0
# IzakJenie, March 2016

search_dir="mp3_result"
uploaded_dir="mp3_uploaded"
post_url=http://theresia.jaskapital.com/kimi/upload.php

source kimibox.cnf

Upload_Directory () {
	for entry in "$search_dir"/*
	do
		filename="${entry##*/}"
		#upload to server
		curl -F "kimi=@$entry" -F "namafile=$filename" $post_url
		#TODO: check if upload is error
		mv $entry "$uploaded_dir/$filename"
		#TODO: check if move file is error
		
	done
}


#upload existing first
Upload_Directory

inotifywait -m $search_dir -e create -e moved_to |
    while read path action file; do
        #echo "The file '$file' appeared in directory '$path' via '$action'"
        # do something with the file

	Upload_Directory
    done
