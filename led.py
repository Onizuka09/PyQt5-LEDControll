import os
from os.path import exists


def setPIn(PIN="23"):
    if (exists(f"gpio{PIN}")==0):
        #f = open(f"gpio{PIN}", "w")
        f = open("/sys/class/gpio/export", "w") 
       
        f.write(PIN)
        f.close()
        s = open(f"/sys/class/gpio/export/gpio{PIN}/direction", "w")
        #s = open(f"gpio{PIN}", "w")
        s.write("out")
        s.close()
    else:
        print("file exists") 

def setVAL(VAL,PIN="23"):
    #f = open(f"gpio{PIN}", "w")
    f = open(f"/sys/class/gpio/export/gpio23/value", "w")
    f.write(VAL)
    f.close()
