from bpe.stat_subwords import get_vocabulary
from bpe.base_input import run_line_readers, words
import re
import logging
from typing import *

def merge_if(judges : List[Callable]):

  while True:
    line = yield

    if line:
      tokens = words(line)
      to_merge = []
      for token in tokens:
        if token.endswith("@@"):
          to_merge.append(token)
        else:
          if len(to_merge) > 0:
            merged_word = "".join(to_merge + [token]).replace("@@", "").lower()
            do_merge = any((judge(merged_word, to_merge + [token]) for judge in judges))
            if do_merge:
              logging.debug(str(merged_word))
              logging.debug(line)
              for subword in to_merge:
                line = re.sub(re.escape(subword) + "\s+", subword[0:-2], line)
              logging.debug(line)
            to_merge.clear()

      print(line)
    else:
      pass



if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG)

  vocab, = run_line_readers([get_vocabulary()], True)
  logging.info("vocab size: %d" % len(vocab))

  google_10k = set(open("../data/google-10000-english.txt").read().split('\n'))

  whole_vocab = vocab | google_10k

  run_line_readers([merge_if([
    lambda w, l: w in whole_vocab
  ])], True)