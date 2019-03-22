## BPE Adaptor

+ 这是一个基于管道的工具，主要的工具都在 bpe 文件夹下。基本的输入应该是 `subword_nmt` 所拆分的文本，subword 都以 `@@` 结尾来标注。
+ `pass.py` 用来循环读入并打印文件，用法是 `python3 pass.py <file_name>`，会从头到尾逐行打印读入的文本，如果读到尾巴会打印 “EOF”
 然后回到开头。如此循环直到管道另一端关闭。
+ `stat_subwords.py` 会从标准输入按行读入文本，然后在标准输出输出一个单词的数量，可以用来统计。如果要统计语料的单词量，可以使用
    ```
    python3 pass.py corpus.txt | python3 stat_subwords.py
    ```
+ `merge_subwords.py` 会从标准输入按行读入文本，然后统计词汇量，并且按照两条简单的规则来合并 subwords，处理完一行以后打印到标准输出
    1. 如果 subword 的小写化在词汇中出现过，合并之。
    2. 如果 subword 的小写化在 `data/google-10000-english.txt` 中出现过，合并之
    3. 对中英文都适用。
    使用方法：
    拆分亚词
    ```
    python3 pass.py corpus.txt | python3 merge_subwords.py > corpus2.txt
    ```