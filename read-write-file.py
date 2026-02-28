#f = open("/Users/sas_vsCodeWorkspace/python_basics/file2.txt", "a")
#f.write("Hellow world! Welcome")
#f.close()

# number of lines
f = open("/Users/sas_vsCodeWorkspace/python_basics/file2.txt", "r")
for line in f:
    print(line)
f.close()

# number of words count
f = open("/Users/sas_vsCodeWorkspace/python_basics/file2.txt", "r")
f_out = open("/Users/sas_vsCodeWorkspace/python_basics/file3.txt", "w")
for line in f:
    tokens = line.split(" ")
    f_out.write("wordcount:"+str(len(tokens))+line)
    # print(len(tokens))
f.close()
f_out.close()