#!/usr/bin/python
"""Kimi_agent.py"""
"""Ambil paket-kimi dari MQ dan recognize dengan fingerprint di database"""
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Izak Jenie"
__email__ = "izak.jenie@gmail.com"
__status__ = "Prototype"


import os
import sys
import json
import warnings
import argparse
import pika
from dejavu import Dejavu
from dejavu.recognize import FileRecognizer
from dejavu.recognize import MicrophoneRecognizer
from argparse import RawTextHelpFormatter

warnings.filterwarnings("ignore")

DEFAULT_CONFIG_FILE = "dejavu.cnf.SAMPLE"

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='paket-kimi')


def callback(ch, method, properties, body):
    #print(" [x] Received %r" % body)
    # djv = init(config_file)
    djv = init("dejavu.cnf.SAMPLE")
    client_data=json.loads(body)
    namafile=client_data['namafile']
    print "Received >>> " + namafile
    opt_arg="/var/www/kimi/uploads/" + namafile
    song = djv.recognize(FileRecognizer, opt_arg)
    print(song)

def init(configpath):
    """ 
    Load config from a JSON file
    """
    try:
        with open(configpath) as f:
            config = json.load(f)
    except IOError as err:
        print("Cannot open configuration: %s. Exiting" % (str(err)))
        sys.exit(1)

    # create a Dejavu instance
    return Dejavu(config)


if __name__ == '__main__':


    channel.basic_consume(callback,
                      queue='paket-kimi',
                      no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()



