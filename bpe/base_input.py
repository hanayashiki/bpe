import re
import logging

word_pat = re.compile(r"[\S]+(?:@@)?")

def words(line: str):
  return re.findall(word_pat, line)


def run_line_readers(line_readers, o=False):

  for r in line_readers:
    r.send(None)

  while True:
    try:
      l = input()
      if l == "EOF":
        break
      for r in line_readers:
        r.send(l)
    except EOFError:
      break

  return [r.send(None) for r in line_readers]

