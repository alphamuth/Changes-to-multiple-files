import os, re

directory = os.listdir('/home/rrahul/word')
os.chdir('/home/CIBIV/rrahul/project/msa4')
t1=time.time()
for file in directory:
    open_file = open(file,'r')
    read_file = open_file.read()
    print(read_file)
    #changes to be made (mistake word)
    regex = re.compile(' rhual')
    #changes to be made (new word)
    read_file = regex.sub('rahul', read_file)
    write_file = open(file,'w')
    write_file.write(read_file)
