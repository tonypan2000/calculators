from fractions import Fraction
import math
import sys


def calc_ent(q):
  if q == 1 or q == 0:
    print(0)
    return
  entropy = -(q * math.log2(q) + (1 - q) * math.log2(1 - q))
  print(entropy)

if len(sys.argv) != 2:
  print("Usage: enter one number in range [0, 1]")
  exit(-1)
input_str = str(sys.argv[1])
if '/' in input_str:
  num = Fraction(input_str)
else:
  num = float(input_str)

calc_ent(num)
