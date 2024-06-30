import ftplib

HOSTNAME = "ftp.dlptest.com"
USERNAME = "dlpuser"
PASSWORD = "rNrKYTX9g7z3RgJRmxWuGHbeu"

ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.encoding = "utf-8"

# store the thingy
filename = "sample.txt"
with open(filename, "rb") as file:
    ftp_server.storbinary(f"STOR {filename}", file)

# ls
ftp_server.dir()

ftp_server.quit()
