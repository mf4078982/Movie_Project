# first prgramm

# list = [1,4,0,3,0,4,5,0,0,0,7,8]
# non_zero = [x for x in list if x != 0]
# zero = [x for x in list if x == 0]
# result = non_zero + zero
# print(result)


# second programm

x = input('Enter the name: ')
y = input('Enter the second name: ')
def fun(x,y):
    for i in x:
        if i not in y:
            return False
    return True
result = fun(x,y)
print(result)    

# third programm

# x = input('Enter the alpha: ')
# y = input('plz enter the found value: ')
# idx = 0
# for i in x:
#     if(i == y):
#         print('correct index: ',idx)
#         f = x.count(y)
#     idx +=1
# print("count the x: ",f)

         
        
    