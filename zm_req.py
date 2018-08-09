#!/usr/bin/python3
# zm_req.py
from time import sleep
import zmq
import sys
import msgpack

class ZReqst:
    def __init__ (self, url):
        context = zmq.Context()
        self.sock = context.socket(zmq.REQ)
        self.srv, x = url.split('.', 1)
        self.sock.connect("tcp://{}".format(url))
        # x seconds timeout
        self.sock.RCVTIMEO = 20*1000
        self.sock.LINGER = 0
# use poller for timeouts
        self.poller = zmq.Poller()
        self.poller.register(self.sock, zmq.POLLIN)
        return
        
    def req (self, name, *args):
        print("sending request : {}, {}".format(name, args))
        reply=""
        try:
            self.sock.send(msgpack.packb([name, args]))
# poll the socket - x seconds timeout
            if self.poller.poll(20*1000):
                reply = msgpack.unpackb(self.sock.recv())
                if isinstance(reply, Exception):
                    raise reply
            else:
# timeout reached, so no reply
                reply = "NoReply"
                return reply
        except zmq.ZMQError as e:
            print("Excpt : {}, {}".format(self.srv, e))
            pass        
        return reply
