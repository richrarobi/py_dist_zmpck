# py_dist_zmpck
distributed Python3 using zeromq and Messagepack
Very simple minded system to allow localised distributed computing based on Python3.

Consists of four main components:

1. a local library zlocal.py (example)
2. a reply server  zm_reply_m.py
3. request clients zm_req.py (example)
4. your application code (see zmrq_blinkt_beat.py for example)

Requires python install for pyzmq messagepack, etc details to follow....

sudo apt-get install python3-zmq

sudo pip3 install pyzmq

sudo pip3 install msgpack


The reply server is run on each system (Linux based) that is used to run routines. On these systems, a local library zlocal.py is also required. Note that if this is modified, the reply program will atttempt to reload it.

The program calling request includes hostname of the correct reply system - see my zmrq_blinkt_beat.py

I have also included zlocal_a.py as an example of what I use on a Raspberry pi to control a Pimoroni Blinkt device. This file would need renaming to zlocal.py.

5. zm_prox.py
6. zm_px-blinkt_beat.py

zprox is used for an RPC style approach to the client interface as shown in the example zm_px-blinkt.py.
The reply server is the same as before.
