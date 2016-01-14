'''
When input file is in the format -- see the example

Sample Input :
4
12 43 65 76

in below code the n will store the value 4 and the array will be stored in arr
'''


import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


'''
When input file is in the format to fetch matrix -- see the example

Sample Input :
3
11 2 4
4 5 6
10 8 -12


in below code the n will store the value 3 and the array will be stored in a
'''

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

