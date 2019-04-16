# import library socket karena menggunakan IPC socket
import socket

# definisikan IP server tujuan file akan diupload

ip = '10.20.2.42'
# definisikan port number proses di server

port = 12345
# definisikan ukuran buffer untuk mengirim

buffer_size = 1024
# buat socket (apakah bertipe UDP atau TCP?)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# lakukan koneksi ke server
s.connect((ip, port))

# buka file bernama "file_diupload.txt bertipe byte
# masih hard code, file harus ada dalam folder yang sama dengan script python

file = open('file_diupload.txt','rb')

try:
    # baca file tersebut sebesar buffer
    byte = file.read(buffer_size)
    # selama tidak END OF FILE; pada pyhton EOF adalah b''
    while byte != b'':
# kirim hasil pembacaan file
        s.send(byte)
# baca sisa file hingga EOF
        byte = file.read(buffer_size)
# print(byte)
finally:
    print("end sending")

    # tutup file jika semua file telah  dibaca
    file.close()
# tutup koneksi setelah file terkirim
s.close()