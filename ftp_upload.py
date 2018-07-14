# -*- coding: utf-8 -*-
import ftplib

def main():
    ftp = ftplib.FTP("192.168.33.200")
    ftp.set_pasv("true")
    ftp.login('vagrant','vagrant')
    fp = open("test.txt","rb")
    ftp.storbinary("STOR /share/test.txt", fp)
    ftp.close()
    fp.close()

if __name__ =="__main__":
    main()
