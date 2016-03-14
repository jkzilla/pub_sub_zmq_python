
import zmq

import sys

from time import sleep

from datetime import datetime



port = "5556"

if len(sys.argv) > 1:

    port = sys.argv[1]

    int(port)



#Connect to the socket 



context = zmq.Context()

socket = context.socket(zmq.PUB)

socket.bind("tcp://*:%s" % port)



while True:

    time = str(datetime.now().time())

    print "Current time: %s" % time

    socket.send("%s" % time)
    sleep(1)	

