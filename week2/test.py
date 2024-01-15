test = {1,2,3,4,5,6,7,8}
item = 0
for i in test:
    if item != 0 :
        test.remove(item)
        item = 0
    if i == 2 :
        item = i
    print(i)