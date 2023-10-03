import os
def read_file(name):
    with open(name, 'r+', encoding='utf-8') as f:
        space = ' '
        zap = ','
        tchk = '.'
        per = '\n'
        i = 0
        j = f.read(1)
        print(f.read())
        print(j)
name = 'data.txt'
read_file(name)

        
#for name in os.listdir(dir):
#    path = os.path.join(dir, name)
#    if os.path.isfile(path):
#        print(path)
#    else:
#        print('[' + path + ']')
#print(os.listdir())