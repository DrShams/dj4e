import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost', 9000))
cmd = 'GET http://localhost/romeo.txt HTTP/1.0\r\n\r\n'.encode()#from Unicode to UTF-8, "\r\n\r\n" - means hit enter
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')#from UTF-8 to Unicode (python inside works with Unicode)

mysock.close()