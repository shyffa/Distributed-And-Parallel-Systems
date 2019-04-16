# import library socket karena akan menggunakan IPC socket

import socket
# definisikan tujuan IP server
ip = '10.20.2.42'

# definisikan port dari server yang akan terhubung
port = 12345

# definisikan ukuran buffer untuk mengirimkan pesan

buffer_size = 1024

# definisikan pesan yang akan disampaikan
MESSAGE ='hai sistem paralel dan terdistribusi'

# buat socket TCP
s = socket.socket()

# lakukan koneksi ke server dengan parameter IP dan Port yang telah didefinisikan
s.connect((ip, port))

# kirim pesan ke server

s.send(MESSAGE.encode())
# terima pesan dari server

data = s.recv(buffer_size)

# tampilkan pesan/reply dari server

print ("received data:", data.decode())
# tutup koneksi

s.close()
