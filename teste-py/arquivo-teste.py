# file = open('abc.txt', 'w+')
# file.write('linha 1\n')
# file.write('linha 2\n')
# file.write('linha 3\n')
# 
# file.seek(0, 0)
# print('lendo linhas:')
# print(file.read())
# print('#######')
# 
# file.seek(0, 0)
# for line in file.readlines():
#     print(line, end='')
# 
# file.close() 

# try:
#     file = open('abc.txt', 'w+')
#     file.write('linha')
#     file.seek(0)
#     print(file.read())
# finally:
#     file.close()    

# with open('abc.txt', 'w+') as file:
#     file.write('linha 1\n')
#     file.write('linha 2\n')
# 
#     file.seek(0)
#     print(file.read())

# with open('abc.txt', 'r') as file:
#    print(file.read())


#with open('abc.txt', 'a+') as file:
#    file.write('Outra Linha')
#    print(file.read())

