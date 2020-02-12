f = open(file='demo.txt', mode="r")
# f.write("Hello From python!")
file_content = f.read()
file_content_lines = f.readlines()
f.close()

print(file_content)

# user_input = input("Type your name: try without f.close()")

# with open('demo.txt', mode='w') as f:
#     # f.write('Add this content!\n')
#     # file_content = f.readlines()
#     # f.close()
#
#     # for line in file_content:
#     #     print(line[:-1])
#     # line = f.readline()
#     # while line:
#     #     print(line)
#     #     line = f.readline()
#     f.write('Testing if this closes...')
# user_input = input('Testing: ')
# print('Done!')
