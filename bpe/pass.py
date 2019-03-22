import sys

f = sys.argv[1]

while True:
  try:
    with open(f, encoding="utf-8") as r:
      for l in r:
        print(l, end='')
      print("EOF")
  except BrokenPipeError:
    break

