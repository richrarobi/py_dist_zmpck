#!/usr/bin/python3
from time import sleep
from zm_prox import ZProxy

if __name__ == "__main__":
    zpc = ZProxy("c.local:5555")
    led = 5
    try:
        while True:
            zpc.ledSet(led, 64, 0, 0, 0.2)
            zpc.ledSet(led, 64, 0, 0)
            zpc.ledSet(led, 64, 0, 0, 5, 6)
            print("	system c : led {}, {}".format(led,  zpc.ledGet(led)))
            sleep(1)
            
            zpc.ledSet(led, 0, 64, 0, 0.2)
            print("	system c : led {}, {}".format(led,  zpc.ledGet(led)))
            sleep(1)
            
            zpc.ledSet(led, 0, 0, 64, 0.2)
            print("	system c : led {}, {}".format(led,  zpc.ledGet(led)))
            sleep(1)
 
    except KeyboardInterrupt:
        print("Stopping!")
        sleep(1)
        zpc.ledSet(led, 0, 0, 0, 0.0)
#        print("	system c : led {}, {}".format(led,  zpc.ledGet(led)))
        sleep(1)
