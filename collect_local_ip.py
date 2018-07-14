# -*- coding: utf-8 -*-
import socket

def main():
  ip = socket.gethostbyname(socket.gethostname())
  print(ip)

if __name__ == "__main__":
  main()
