import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
s.bind((host,8081))

s.listen(5)
while(True):
    c, addr = s.accept()
    print(f"Got connected with (addr)")
    c.send("thank you for connecting")
    c.close()
