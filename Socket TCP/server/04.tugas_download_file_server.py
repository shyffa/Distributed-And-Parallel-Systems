# import library socket karena menggunakan IPC socket
import socket
ip = "192.168.43.208"
port = 12345
buffer_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, port))
sock.listen(1)
print ('Connection address:', ip)
file = open('file_didownload.txt','rb')
c, addr = sock.accept()
try:
    byte = file.read(buffer_size)
    while byte != b'':
        # kirim hasil pembacaan file dari server ke client
        c.send(byte)
        # baca sisa file hingga EOF
        byte = file.read(buffer_size)
finally:
    print ("end sending")
    # tutup file jika semua file telah  dibaca
    file.close()
# tutup socket
sock.close()
# tutup koneksi
c.close()