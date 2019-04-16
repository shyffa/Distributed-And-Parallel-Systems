# import library socket karena akan menggunakan IPC socket
import socket

# definisikan alamat IP binding  yang akan digunakan 
ip = "10.20.2.42"

# definisikan port number binding  yang akan digunakan 
port = 12345

# definisikan ukuran buffer untuk mengirimkan pesan
buffer_size = 1024

# buat socket bertipe TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lakukan bind
s.bind((ip, port))

# server akan listen menunggu hingga ada koneksi dari client
s.listen(1)

# lakukan loop forever
while 1:
	# menerima koneksi
    conn, addr = s.accept()

	# menampilkan koneksi berupa IP dan port client yang terhubung menggunakan print
    print('Connection address:', addr)

	# menerima data berdasarkan ukuran buffer
    data = conn.recv(buffer_size).decode()

	# menampilkan pesan yang diterima oleh server menggunakan print
    print("received data:", data)

	# mengirim kembali data yang diterima dari client kepada client
    conn.send(data.encode())

# tutup koneksi	
conn.close()
