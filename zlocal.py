#!/usr/bin/python3
# zlocal.py
from time import sleep
import subprocess

def is_ARM():
    tmp = runprc("cat /proc/cpuinfo")
    for line in tmp.splitlines():
        if "model name" in line:
            x, t = line.split(": ")
            if "ARM" in t:
                return True
    return False

def getTmp():
    if is_ARM():
        import subprocess
        tmp = subprocess.check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        tmp = tmp.decode("utf-8").rstrip("\n")
        tmp = tmp[5:]
        tmp = tmp[:-2]
        return tmp
    else:
        return "notARM"

def runprc(cmnd):
# be very careful with this one !!!
    from subprocess import Popen, STDOUT, PIPE
    import shlex
    try:
        args = shlex.split(cmnd)
        if args[0] in ["uname", "ls", "ps", "lsusb", "df", "cat"]:
            p = Popen(args, stdout=PIPE)
            out, err = p.communicate(timeout=30)
            out = out.decode("utf-8").rstrip("\n")
        else:
            out = "runprc: Not Allowed"
    except:
        p.kill()
    return out

def datim():
    import datetime
    now = datetime.datetime.now()
    x = str(now)
    y, z = x.split(" ")
    y, m, d = y.split("-")
    hh, mm, ss = z.split(":")
    ss, dec = ss.split(".")
    stmp = "{}-{}-{} {}:{}:{}".format(y, m, d, hh, mm, ss)
    return stmp

if __name__ == "__main__":
    print(getTmp())
    print(datim())
    print(runprc("ls -l"))
