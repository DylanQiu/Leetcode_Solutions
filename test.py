# product = 1
# list = [1,2,3,4]
# for num in list:
#     product = product * num

product = reduce((lambda x,y:x*y), [1,2,3,4])

print product
