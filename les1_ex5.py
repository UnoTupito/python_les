import random

list1 = []
list2 = []
list_help = []

len1 = int(input('length of the first list'))
len2 = int(input('length of the second list'))

for i in range(len1):
    list1.append(random.randint(0, len1+len2))
for i in range(len2):
    list2.append(random.randint(0, len1 + len2))
print(list1)
print(list2)
list_help = list1 + list2
print(list_help)
list_help.sort()
print(list_help)

for i in range(len(list1)):
    print(list_help[i], end=' ')
print('\n')
for i in range(len(list2)):
    print((list_help[i+len(list1)]), end=' ')




