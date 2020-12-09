import sys

if len(sys.argv) != 5:
  print("Usage: enter the sample sizes and stds as n1, n2, a1, s2")
  exit(-1)

n1 = float(sys.argv[1])
n2 = float(sys.argv[2])
s1 = float(sys.argv[3])
s2 = float(sys.argv[4])

nu = (s1 ** 2 / n1 + s2 ** 2 / n2) ** 2 / ((s1 ** 2 / n1) ** 2 / (n1 - 1) + (s2 ** 2 / n2) ** 2 / (n2 - 1))
print("degrees of freedom:", nu)
