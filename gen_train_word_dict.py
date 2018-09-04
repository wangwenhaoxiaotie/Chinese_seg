import re
import codecs
#filenames = ['train_finance_jieba.txt']
filenames = ['test_finance_jieba.txt']
#output_file = 'train_worddict.txt'
output_file = '../corpus/test_worddict.txt'
for file_name in filenames:
    input_file = '../'+file_name
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'a', 'utf-8')

    for line in input_data.readlines():
        word_list = line.strip().split("/ ")
        for wl in word_list:
            if re.search("^[\u4e00-\u9fa5]+", wl):
                output_data.write(wl+'\n')