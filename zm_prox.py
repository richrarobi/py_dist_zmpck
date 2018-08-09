#!/usr/bin/python3
# zm_prox
import zmq
import sys
import msgpack

# proxy to call the  remote system
class ZProxy:
    def __init__(self, url):
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
        
    def __getattr__(self, name):
        def rpc(*args):
            try:
                print("RPC sending to: {}, {}, {}".format(self.srv, name, args))
                self.sock.send(msgpack.packb([name, args], use_bin_type=True))
            except zmq.ZMQError as e:
                print("Excpt : {}, {}".format(self.srv, e))
                pass
# poll the socket - x seconds timeout
            if self.poller.poll(2*1000):
                reply = msgpack.unpackb(self.sock.recv(),use_list=False, raw=False)
                if isinstance(reply, Exception):
                    raise reply
            else:
# timeout reached, so no reply
                reply = "NoReply"
            return reply
        return rpc
