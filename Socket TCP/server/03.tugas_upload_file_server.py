import socket
ip = "10.20.2.42"
port = 12345
buffer_size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
s.listen(1)
print ('Connection address:', ip)
buat = open("upload.txt", "wb+")
c, addr = s.accept()
while 1:
    data = c.recv(buffer_size)
    buat.write(data)
    if not data: break
buat.close()
c.close()
