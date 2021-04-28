output = open('output.txt', 'wt', encoding='utf-8')
for i in range(1,151):
    filepath = './docs/issue-' + str(i) + '.md'
    print("processing " + filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if  '欢迎订阅' in line:
                break
            if line[:2] == '##' or line[:2] == '# ':
                print(line, file=output)
output.close()
                