
from bpe.base_input import run_line_readers, words

def get_vocabulary(tolower=True):

  vocab = set()

  while True:
    line = yield
    if line:
      results = words(line)
      for r in results:
        if tolower:
          vocab.add(r.lower())
        else:
          vocab.add(r)
    else:
      yield vocab

if __name__ == '__main__':

  results = run_line_readers([get_vocabulary()])

  for idx, r in enumerate(results):
    print("=======%d=======" % idx)
    print(len(r))