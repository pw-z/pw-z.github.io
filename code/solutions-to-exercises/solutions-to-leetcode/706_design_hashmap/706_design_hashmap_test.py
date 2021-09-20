

def read_testcase(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
        output = lines[0][1:-1].split(',')
        expected = lines[1][1:-1].split(',')
        op = lines[2][1:-1].split(',')
        num = lines[3][1:-1].split('],')
        return output,expected,op,num


def diff():
    output,expected,op,num = read_testcase('./706_testcase.txt')
    with open('./x.txt','w',encoding='utf8') as f:
        for exp, out, op, num in zip(expected, output, op, num):
            f.write(op + '('+num+')   exp:' + exp + '  out:' +out + '\n')
            if(exp != out):
                f.write('#\n'*80)
                print(op + '(' + num + ')' + '  exp = ' + exp + '  out = ' + out)



if __name__=='__main__':
    diff()





