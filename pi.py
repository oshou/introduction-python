#!/usr/bin/python

import sys
import math

def arctan(x, k):
  arctanx = 0
  for n in range(0, k):
    arctanx +=  pow(-1, n) * (1/(2 * (n+1) - 1)) * pow(x, (2*(n+1) - 1))
  return arctanx

if __name__ == '__main__':
    argv = sys.argv

    if len(argv) != 2:
        print('usage : {0} <n>'.format(argv[0]))
        quit()

    for k in range(1, int(argv[1])):
        pi = 4 * (4 * arctan(1/5, k) - arctan(1/239, k))

    print(pi)
