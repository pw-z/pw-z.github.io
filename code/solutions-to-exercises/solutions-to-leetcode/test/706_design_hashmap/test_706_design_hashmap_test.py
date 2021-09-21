

def read_testcase(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        lines = f.readlines()
        output = lines[0][1:-1].split(',')
        expected = lines[1][1:-1].split(',')
        op = lines[2][1:-1].split(',')
        num = lines[3][1:-1].split('],')
        return output,expected,op,num


def diff():
    output,expected,op,num = read_testcase('./testdata.txt')
    with open('./x.txt','w',encoding='utf8') as f:
        for exp, out, op, num in zip(expected, output, op, num):
            f.write(op[1:-1] + '('+num[1:]+')   exp:' + exp + '  out:' +out + '\n')
            if(exp != out):
                f.write('#\n'*80)
                print(op[1:-1] + '(' + num[1:] + ')' + '  exp = ' + exp + '  out = ' + out)

def gen():
    output,expected,op,num = read_testcase('./testdata.txt')
    with open('./test.cpp','w',encoding='utf8') as f:
        f.write('#include "706_2nd_try.h"\nint main(int argc, char const *argv[]){\nMyHashMap* obj = new MyHashMap();\n')

        for exp, out, op, num in zip(expected, output, op, num):
            f.write("obj->" + op[1:-1] + "(" + str(num[1:]) + ");\n")

        f.write("return 0;\n}")

if __name__=='__main__':
    diff()
    gen()





