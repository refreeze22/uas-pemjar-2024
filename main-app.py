import socket
import ftplib
import paramiko
import subprocess
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from paramiko import SSHClient, AutoAddPolicy

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('main-menu.html')

def main_menu():
    print("1. Akses Port Socket")
    print("2. FTP Server dan Client")
    print("3. SSH Server dan Client")
    print("4. Cek Port Server")
    print("0. Keluar")
    choice = input("Pilih menu: ")
    return choice

def socket_access():
    host = input("Masukkan alamat host: ")
    port = int(input("Masukkan nomor port: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            print(f"Berhasil terhubung ke {host} pada port {port}")
        except Exception as e:
            print(f"Gagal terhubung ke {host} pada port {port}: {e}")

def ftp_server():
    authorizer = DummyAuthorizer()
    authorizer.add_user("user", "12345", ".", perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer(("0.0.0.0", 2121), handler)
    print("Server FTP berjalan pada port 2121")
    server.serve_forever()

def ftp_client():
    host = input("Masukkan alamat host FTP: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    with ftplib.FTP(host) as ftp:
        ftp.login(user=username, passwd=password)
        ftp.retrlines('LIST')
        print("Koneksi FTP berhasil")

def ftp_server_client():
    choice = input("Pilih: 1 untuk FTP Server, 2 untuk FTP Client: ")
    if choice == '1':
        ftp_server()
    elif choice == '2':
        ftp_client()
    else:
        print("Pilihan tidak valid.")

def ssh_client():
    host = input("Masukkan alamat host SSH: ")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password)

    stdin, stdout, stderr = client.exec_command('ls')
    print(stdout.read().decode())
    client.close()

def ssh_server_client():
    choice = input("Pilih: 1 untuk SSH Client (SSH Server memerlukan setup manual): ")
    if choice == '1':
        ssh_client()
    else:
        print("Pilihan tidak valid.")

def check_port_server():
    host = input("Masukkan alamat host: ")
    port = int(input("Masukkan nomor port: "))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"Port {port} pada {host} terbuka.")
        else:
            print(f"Port {port} pada {host} tertutup.")

def main():
    while True:
        choice = main_menu()
        if choice == '1':
            socket_access()
        elif choice == '2':
            ftp_server_client()
        elif choice == '3':
            ssh_server_client()
        elif choice == '4':
            check_port_server()
        elif choice == '0':
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
