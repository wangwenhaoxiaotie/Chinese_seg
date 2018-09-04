import codecs
import os
import re
def character_4tagging(output_file):
    #filenames = ['finNlp_wallstreet1_jieba.txt','finNlp_wallstreet1_jieba.txt','caijing_licai_jieba.txt','china_insurance_jieba.txt']
    filenames = ['../test_finance_jieba.txt']
    for file_name in filenames:
        input_file = './'+file_name
        input_data = codecs.open(input_file, 'r', 'utf-8')
        output_data = codecs.open(output_file, 'a', 'utf-8')
        
        for line in input_data.readlines():
            word_list = line.strip().split("/ ")
            for word in word_list:
                if word == '' or re.search('/[^a-zA-Z]', word) != None:
                    continue
                elif word == '。/':
                    output_data.write("。" + "\t" + "S\n")
                else:
    #                 words = word.split("/")
    #                 #print(words)

    #                 if len(words) >= 2:
    #                     xz = words[1]
    #                     word = words[0]
                    if len(word) == 1:
                        output_data.write(word + "\t" + "S\n")
                        #print(word + "\t" + "S\n")
                    else:
                        output_data.write(word[0] + "\t" + "B\n")
                        #print(word[0] + "\t" + "B\n")
                        for w in word[1:len(word) - 1]:
                            output_data.write(w + "\t" + "M\n")
                            #print(w + "\t" + "M\n")
                        output_data.write(word[len(word) - 1] + "\t" + "E\n")
                        #print((word[len(word) - 1] + "\t" + "E\n"))

            output_data.write("\n")
if __name__ == '__main__':
    character_4tagging("../test_finance_tag.txt")