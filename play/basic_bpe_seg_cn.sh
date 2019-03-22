#!/usr/bin/env bash

train_file=../data/10w_ch
test_file=${train_file}
num_operations=30000
codes_file=./basic_bpe_seg_cn.codes
out_file=./basic_bpe_seg_cn.out

python3.6 -m subword_nmt.learn_bpe -s ${num_operations} < ${train_file} > ${codes_file}
python3.6 -m subword_nmt.apply_bpe -c ${codes_file} < ${test_file} > ${out_file}