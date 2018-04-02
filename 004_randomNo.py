import re

file_name = 'test.txt'

lines_count = 0
words_count = 0
chars_count = 0
words_dict  = {}
lines_list   = []

with open(file_name, 'r') as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count  = chars_count + len(line)
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            # 只要英文单词，删掉其他字符
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1

print 'words_count is', len(words_dict)
print 'lines_count is', lines_count
print 'chars_count is', chars_count

for k,v in words_dict.items():
    print k,v
