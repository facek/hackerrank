#!/usr/bin/python3
def maxXor(l, r):
	max = 0
	for a in range(l,r+1):
		for b in range(a,r+1):
			if a^b > max:
				max = a^b
	return max
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))