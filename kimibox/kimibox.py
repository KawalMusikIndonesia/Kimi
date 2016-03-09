#!/usr/bin/python

import sys
import argparse
import dejavu.decoder as decoder
import time
import json
import httplib

from argparse import RawTextHelpFormatter



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Kimi: Audio Fingerprint Reporting",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument('-p', '--printfp', nargs=3,
                        help='Print the fingerprint from mic/file\n '
                             'Usage: \n'
                             '--printfp boxid mic number_of_seconds \n'
                             '--printfp boxid file path/to/file \n')
    args = parser.parse_args()


    if not args.printfp:
        parser.print_help()
        sys.exit(0)

    if args.printfp:
        # Recognize audio source
        song = None

        boxid = args.printfp[0]
        source = args.printfp[1]
        opt_arg = args.printfp[2]

	frames, fs, file_hash=decoder.read(opt_arg, 3)
	

	#get time and construct filename

	stime=time.strftime("%H:%M:%S")
	sdate=time.strftime("%Y/%m/%d")

	filename="kfp_"+sdate+"_"+stime+"_"+boxid+".txt"

	paket={}
	paket['jam']=stime
	paket['tanggal']=sdate
	paket['boxid']=boxid
	paket['fingerprint']=file_hash

	paket_kimi=json.dumps(paket)

	print paket_kimi
	# send to server

	headers = { "charset" : "utf-8", "Content-Type": "application/json" }
	conn = httplib.HTTPConnection("localhost")
	conn.request("POST", "/kimi/kimisubmit.php", paket_kimi, headers)
	response = conn.getresponse()
	print(response.read())
	conn.close()
