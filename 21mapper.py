# Case 2 - Mapper using standard input and output
# Easy to test locally in the terminal

import sys 

# iterate through each line provided via standard input
for line in sys.stdin:
  datalist = line.strip().split("    ")
  datalist = datalist[0].split(",")
  print(datalist)
  if (len(datalist) == 7) : 
    gender, race,parental_education,	lunch,	math,	reading,	writing = datalist

    # print intermediate key-value pairs to standard output
    print(gender,"\t",math)

