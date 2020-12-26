import sys
import socket
import getopt
import threading
import subprocess

listen = False
command = False
execute = ''
target = ''
upload_destination = ''
port = 0

def instruction():
    print("*********************Victor Nunes's Net Tool********************* \n")
    print("Usage: vsnnet.py -t target_host -p port")
    print("-l --listen               - Listen on [host]:[port] for incoming connections")
    print("-e --execute=file_to_run  - Execute the given file upon receiving a connection")
    print("-c --command              - Initialize a command shell")
    print("-u --upload=destination   - Upon receiving connection upload a file and write to [destination] \n\n")
    print("Examples:")
    print("vsnnet.py -t 192.168.2.1 -p 1212 -l -c")
    print("vsnnet.py -t 192.168.2.1 -p 1212 -l -u=c:\\target.exe")
    print("vsnnet.py -t 192.168.2.1 -p 1212 -l -e=\'cat /etc/passwd\'")
    print("echo 'ABCDEFG' | ./vsnnet.py -t 192.168.2.1 -p 100")
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        instruction()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help", "listen", "execute", "target", "port", "command", "upload"])
    except getopt.GetoptError as err:
        print(err)
        instruction()

    for opt,arg in opts:
        if opt in ("-h", "--help"):
            instruction()
        elif opt in ("-l", "--listen"):
            listen = True
        elif opt in ("-e", "--execute"):
            execute = arg
        elif opt in ("-c", "--commandshell"):
            command = True
        elif opt in ("-u", "--upload"):
            upload_destination = arg
        elif opt in ("-t", "--target"):
            target = arg
        elif opt in ("p", "--port"):
            port = int(arg)
        else:
            assert False, "Unhandled Option"

    if not listen and len(target) and port > 0:
        client_sender(buffer)

    if listen:
        server_loop()

main()


    
    
    
    
