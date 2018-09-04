import socket

s = socket.socket()
host = socket.gethostname()
s.bind(host,8080)

s.listen(5)
while(True):
    c = s.accept()
    print("Got connected with {}".format(c))
    c.send("thank you for connecting")
    c.close()
