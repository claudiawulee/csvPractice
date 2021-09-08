import csv
import statistics as stat
def gradebookSummary(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    data = list(reader)
    header = ["ids", "mean", "median"]
    testLst=[]
    innerLst=[]
    #print(data)
    for i in range(len(data)):
        if data[i] != []:
            innerLst=[]
            innerLst.append(data[i][0])
            numbers = data[i][1:]

            for j in range(len(numbers)):

                numbers[j] = int(numbers[j])
            mean = round(stat.mean(numbers), ndigits=2)
            innerLst.append(mean)
            median = stat.median(numbers)
            innerLst.append(median)
            testLst.append(innerLst)
    #return testLst
    file = open("summary_" + str(filename), "w", newline ="")
    with file:
        write = csv.writer(file)
        write.writerow(header)
        write.writerows(testLst)

def testGradebookSummary():
    import os
    print("Testing gradebookSummary()...", end="")

    gradebookSummary("gradebook1.csv")

    # did you generate a file of the correct name?
    assert(os.path.exists("summary_gradebook1.csv") == True)
    f1 = open("summary_gradebook1.csv", "r")
    text1 = f1.read()
    f1.close()
    result1 = """
ids,mean,median
wilma,92.67,93
fred,90.4,90
betty,88,88
""".strip()
    # are you producing the correct text results?
    assert(text1.strip() == result1.strip())

    gradebookSummary("gradebook2.csv")

    # did you generate a file of the correct name?
    assert(os.path.exists("summary_gradebook2.csv") == True)
    f2 = open("summary_gradebook2.csv", "r")
    text2 = f2.read()
    f2.close()
    result2 = """
ids,mean,median
kaladin,84,85
shallan,89.67,92.0
adolin,85,85
lift,50,50
szeth,56.67,70
""".strip()
    # are you producing the correct text results?
    assert(text2.strip() == result2.strip())
    print("... done!")

testGradebookSummary()