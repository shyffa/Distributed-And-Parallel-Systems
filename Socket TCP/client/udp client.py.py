
# import library socket karena akan menggunakan IPC socket
import socket

# definisikan target IP server yang akan dituju

UDP_IP = '10.20.2.42'
# definisikan target port number server yang akan dituju

UDP_PORT = 12345

print ("target IP:", UDP_IP)
# definisikan pesan yang akan dikirim
MESSAGE = 'sister gampang cuy'
print ("target port:", UDP_PORT)
print ("pesan:", MESSAGE)

# buat socket bertipe UDP
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# lakukan loop 10 kali
for x in range (10):

# kirim pesan
    sock.sendto(MESSAGE.encode(), (UDP_IP, UDP_PORT))
