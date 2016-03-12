#!/bin/bash
#Kimibox_uploader.sh    
#Cek file di directory dan upload ke KIMI server
#perlu apt-get install inotify-tools
#
#__license__ = "GPL"
#__version__ = "1.0"
#__maintainer__ = "Izak Jenie"
#__email__ = "izak.jenie@gmail.com"
#__status__ = "Prototype"


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
