import zmq

import sys



port = 5556 

if len(sys.argv) > 1:

    port = sys.argv[1]

    int(port)



context = zmq.Context()

socket = context.socket(zmq.SUB)



socket.connect("tcp://localhost:%s" % port)



topicfilter = ""

socket.setsockopt(zmq.SUBSCRIBE, topicfilter)


while True:
	string_updates_time = socket.recv()
	print string_updates_time