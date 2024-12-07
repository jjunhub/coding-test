import sys
n = int(input())

if n == 2:
  A, B = map(int, input().split())
  yaksoo_numbers = []
  for number in range( 1 , int(min(A,B)**0.5)+1): # 루트 N
    if min(A,B) % number == 0:
      yaksoo_numbers.append(number)
      yaksoo_numbers.append(min(A,B)//number)
  
  yaksoo_numbers = list(set(yaksoo_numbers)) # N
  yaksoo_numbers.sort() # N 로그N
  

  for yaksoo in yaksoo_numbers: # 루트 N보다 적게
    if A % yaksoo == 0 and B % yaksoo == 0:
      print(yaksoo)

else : # n == 3
  A, B, C = map(int, input().split())
  yaksoo_numbers = []
  for number in range( 1 , int(min(A,B,C)**0.5)+1):
    if min(A,B) % number == 0:
      yaksoo_numbers.append(number)
      yaksoo_numbers.append(min(A,B,C)//number)
  
  yaksoo_numbers = list(set(yaksoo_numbers)) # N
  yaksoo_numbers.sort()

  for yaksoo in yaksoo_numbers:
    if A % yaksoo == 0 and B % yaksoo == 0 and C % yaksoo == 0:
      print(yaksoo)