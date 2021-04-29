
def analyze():
    output = open('output.txt', 'wt', encoding='utf-8')
    title={}
    for i in range(1,151):
        filepath = './docs/issue-' + str(i) + '.md'
        print("processing " + filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                if  '欢迎订阅' in line:
                    break
                if line[:2] == '##':
                    if line[3:] not in title:
                        title[line[3:]]=1
                    else:
                        title[line[3:]]+=1
                    print(line, file=output, end="")
    print("\n\n\n\n\n", file=output)
    for count_result in title:
        print(count_result[:-1] + '  ' + str(title[count_result]), file=output)
    output.close()

def process():
    print()

if __name__=="__main__": 
    analyze()
                