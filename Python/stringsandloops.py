sentence = (input("Please type a sentence:\t"))
dataArr = sentence.split()

for element in dataArr:
    for i in range(0,len(element)):
        print(element[i])
    print("-")
