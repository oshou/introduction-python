# -*- coding: utf-8
#import urllib.request
#
#def main():
#  data = urllib.request.urlopen("https://algorithm.joho.info/")
#  html = data.read()
#  print(html)
#  data.close()
#
#if __main__ == "__main__":
#  main()
import urllib

def main():
  data = urllib.urlopen("https://algorithm.joho.info/")
  html = data.read()
  print(html)
  #data.close()

if __main__ == "__main__":
  main()
