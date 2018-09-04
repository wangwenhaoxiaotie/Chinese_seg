import codecs
import sys
import re

# def character_2_word(input_file, output_file):
#     input_data = codecs.open(input_file, 'r', 'utf-8')
#     output_data = codecs.open(output_file, 'w', 'utf-8')
#     for line in input_data.readlines():
#         if line == "\n":
#             continue
#         else:
#             char_tag_pair = line.strip().split('\t')
#             if len(char_tag_pair)==1:
#                 continue
#             else:
#                 char = char_tag_pair[0]
#                 if char == '。':
#                     output_data.write(' ' + char +'\n')
#                     #print(' ' + char +'\n')
#                 else:
#                     tag = char_tag_pair[1]
#                     if tag == 'B':
#                         output_data.write(' ' + char)
#                     elif tag == 'M':
#                         output_data.write(char)
#                     elif tag == 'E':
#                         output_data.write(char + ' ')
#                     else: # tag == 'S'
#                         output_data.write(' ' + char + ' ')
#     input_data.close()
#     output_data.close()
# if __name__ == '__main__':
#     input_file = "../test_finance_tag.txt"
#     output_file = "../test_gold_seg.txt"
#     character_2_word(input_file, output_file)
    
    
    
# input_data = codecs.open('../test_gold_seg.txt','r','utf-8')
# output_data = codecs.open('../test_gold_seg_proc.txt','w','utf-8')
# for line in input_data.readlines():
#     if re.search('^。',line.lstrip()) == None:
#         output_data.write(line.lstrip())


input_data = codecs.open('../test_finance_outcome.txt','r','utf-8')
output_data = codecs.open('../test_finance_outcome_proc.txt','w','utf-8')
for line in input_data.readlines():
    if re.search('^。',line.lstrip()) == None:
        output_data.write(line.lstrip())