#!/usr/bin/python3
# Filename: zm_reply_m.py
import time
import threading
import zmq
import signal
import sys
import zlocal
import importlib
import msgpack

def worker_routine(worker_url, context=None):
    context = context or zmq.Context.instance()
    # Socket to talk to dispatcher
    socket = context.socket(zmq.REP)
    socket.connect(worker_url)

    while True:
        [func, args] = msgpack.unpackb(socket.recv(),use_list=False, raw=False)
# reload the zlocal library if changed
        importlib.reload(zlocal)
        module = importlib.import_module('zlocal')
        try:
    # get the function if callable
            fn = getattr(module, func)
            if callable(fn):
#                print("Calling fn: {}, args: {} ".format(fn, args))
                reply = fn(*args)
#                print("Reply to fn: {}. {}".format(fn, reply))
        except:
            reply = "Reply.Error in : " + func
#            print("Reply.Error fn: {}".format(func))
        socket.send(msgpack.packb(reply, use_bin_type=True))

def main():
    url_worker = "inproc://workers"
    url_client = "tcp://*:5555"
    context = zmq.Context.instance()

    # Socket to talk to clients
    clients = context.socket(zmq.ROUTER)
    clients.bind(url_client)
    # Socket to talk to workers
    workers = context.socket(zmq.DEALER)
    workers.bind(url_worker)

    # Launch pool of worker threads
    for i in range(3):
        thread = threading.Thread(target=worker_routine, args=(url_worker,))
        thread.start()

    zmq.proxy(clients, workers)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Stopping!")
# We should never get here but clean up anyhow
        clients.close()
        workers.close()
        context.term()
        sleep(2)
