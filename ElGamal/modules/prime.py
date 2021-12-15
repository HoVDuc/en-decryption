import math
import random

def isPrime(n):
   for i in range(2, int(math.sqrt(n) + 1)):
      if n % i == 0:
         return False
   return True

def prime():
   n = 999999
   while True:
      x = random.randint(999, n)
      if(isPrime(x)):
         break
   return x
