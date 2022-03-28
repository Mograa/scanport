import socket
import sys
from time import sleep

rHost = "127.0.0.1"
print("\033[36mHelp: -h 111")
comand = input("\033[4;0;35m>>> ")
comand2 = comand.split()
rHostIP = socket.gethostbyname(comand2[2])
TPorts = [22,443,80,8080,53,19,111,17,23,67,68,69,123,135,
136,137,138,139,161,162,21]
TPorts.sort()
UPorts = [7,11,13,17,18,19,37,42,49,53,67,68,69,71,72,73,74,
80,88,104,105,107,108,111,117,118,123,126,135,]
UPorts.sort()
if comand == "mping -t {}".format(rHost):
    rHostIP = socket.gethostbyname(rHost)
    sleep(0.3)
    print("Please wait, scanning...", rHostIP)
    try:
        for ports in TPorts:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            resultado = s.connect_ex((rHostIP, ports))
            if resultado == 0:
                sleep(1)
                print("Port {} open".format(ports))
            else:
                sleep(0.2)
                print("Ports {} closed".format(ports))
    except KeyboardInterrupt:
        print("\nProgram interrupted")
        sys.exit()
elif comand == "mping -o {}".format(rHost):
    rPORT = int(input("Enter Port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((rHost,rPORT))
    if result == 0:
        sleep(0.3)
        print("Port {} open".format(rPORT))
    else:
        sleep(0.3)
        print("Port {} closed".format(rPORT))
elif comand == "mping -u {}".format(rHost):
    rHostIP = socket.gethostbyname(rHost)
    sleep(0.3)
    print("Please wait, scanning...", rHostIP)
    try:
        for ports in UPorts:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            socket.setdefaulttimeout(0.1)
            resultado = s.connect_ex((rHostIP, ports))
            if resultado == 0:
                sleep(0.2)
                print("Port {} open".format(ports))
            else:
                sleep(0.2)
                print("Ports {} closed".format(ports))
    except KeyboardInterrupt:
        print("\nProgram interrupted")
        sys.exit()
elif comand == "mping -o {}".format(rHost):
    rPORT = int(input("Enter Port: "))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((rHost,rPORT))
    if result == 0:
        sleep(0.3)
        print("Port {} open".format(rPORT))
    else:
        sleep(0.3)
        print("Port {} closed".format(rPORT))
elif comand == "mping -h 111":
    print("""
        -t        scan TCP ports | 17 - 443/8080
        -o        scan an port
        -u        scan UDP ports | 7 - 135
        -h 111    manual
         """)

else:
    sys.exit()