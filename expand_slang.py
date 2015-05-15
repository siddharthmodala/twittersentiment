import csv
import twokenize as tw


slang_list={}
with open('slang_list.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',',quotechar='|')
    for row in spamreader:
        slang_list[row[0]] =   (" ".join(row[1:])).strip()


#print slang_list[token]

def expand(token):
    if token in slang_list.keys():
        return tw.tokenize(slang_list[token])
    else:
        return [token]
    