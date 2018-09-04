# /usr/bin/env python
# -*- coding: utf-8 -*-
# make_crf_train_data.py
# 4 tags for character tagging: B(Begin), E(End), M(Middle), S(Single)
import codecs
import os
import re
def character_4tagging(input_path, output_file):
    file_flag = 0
    for dirpath, dirnames, filenames in os.walk(input_path):
        if filenames != []:
            file_flag = 1
            for file_name in filenames:
                input_file = dirpath+'/'+file_name
                print(input_file)
                input_data = codecs.open(input_file, 'r', 'utf-8')
                output_data = codecs.open(output_file, 'a', 'utf-8')
                for line in input_data.readlines():
                    word_list = line.strip().split(" ")
                    for word in word_list:
                        if word == '' or re.search('/[^a-zA-Z]', word) != None:
                            continue
                        else:
                            words = word.split("/")
                            #print(words)

                            if len(words) >= 2:
                                xz = words[1]
                                word = words[0]
                                if len(word) == 1:
                                    output_data.write(word + "\t" + xz + "\tS\n")
                                else:
                                    output_data.write(word[0] + "\t" + xz + "\tB\n")
                                    for w in word[1:len(word) - 1]:
                                        output_data.write(w + "\t" + xz + "\tM\n")
                                    output_data.write(word[len(word) - 1] + "\t" + xz + "\tE\n")

                    output_data.write("\n")
    if file_flag == 0:
        print("No datasets!")
    input_data.close()
    output_data.close()
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("pls use: python make_crf_train_data.py input output")
        sys.exit()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    character_4tagging(input_file, output_file)
