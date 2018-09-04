 #!/bin/sh
#python ./CRF++/make_crf_train_data.py "./kcws-master/2014" "./train.txt"
#./CRF++/CRF++-0.58/crf_learn -f 3 -c 4.0 ./CRF++/CRF++-0.58/example/seg/template "./train.txt" ./CRF++/CRF++-0.58/crf_model_all
python ./make_crf_test_data.py ./test_finance.txt ./test_proc.txt
./CRF++-0.58/crf_test -m ./CRF++-0.58/crf_model_all_finance ./test_proc.txt > ./test_pred.txt
python ./crf_data_2_word.py ./test_pred.txt ./test_finance_seg.txt
rm ./test_proc.txt
rm ./test_pred.txt


# ./CRF++/CRF++-0.58/crf_learn -f 3 -c 4.0 ./CRF++/CRF++-0.58/example/seg/template "./train_finance_tag.txt" ./CRF++/CRF++-0.58/crf_model_all_finance