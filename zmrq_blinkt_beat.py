#!/usr/bin/python3
# zmq_blinkt_beat.py
from time import sleep
from zm_req import ZReqst

if __name__ == "__main__":
    zp = ZReqst("c.local:5555")
    led = 2

    try:
        while True:
            print("system c : isARM : {}".format(zp.req("is_ARM")))
            print("system c : getTMP : {}".format(zp.req("getTmp")))
            
            print("system c : invalid : {}".format(zp.req("invalid call")))
            zp.req("ledSet",led, 64, 0, 0, 0.2)
            print(" system c : led {}: {}".format(led, zp.req("ledGet",led)))
            sleep(1)
            
            zp.req("ledSet",led, 0, 64, 0, 0.2)
            print(" system c : led {}: {}".format(led, zp.req("ledGet",led)))
            sleep(1)
            
            zp.req("ledSet",led, 0, 0, 64, 0.2)
            print(" system c : led {}: {}".format(led, zp.req("ledGet",led)))
            sleep(1)
 
    except KeyboardInterrupt:
        print("Stopping!")
        sleep(2)
        zp.req("ledSet",led, 0, 0, 0, 0.0 )
        zp.req("ledSet",led, 0, 0, 0, 0.0 )
#        print(" system c : led {}: {}".format(led, zp.req("ledGet",led)))
        sleep(1)
