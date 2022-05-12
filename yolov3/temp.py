with open(r'D:\hw3\MixamoDownloader-master\having_actions.txt', 'r', encoding='UTF-8') as f_read:
    line = list(eval(f_read.readlines()[0].strip()))

print(len(line))
for l in line:
    print(l)