## Tes with dictionaries

monthNumber = { 'Jan':1, 'Feb':2, 'Mar':3, 1:'Jan', 2:'Feb', 3:'Mar'}

friends = { '0904009':'Shihab', '0904022':'Mahamid', '0904088':'Nahid', '0904106':'Nasim', '0904110':'Zaman'}

collect = []
for e in friends :
    collect.append(friends[e])

print(collect)
print(friends.keys())

tuple_1 = (1, 2, 3)                 ## KEY
copy_of_tuple_1 = tuple_1     ## VALUE

tuple_2 = (4, 5, 6)                 ## KEY
copy_of_tuple_2 = tuple_2     ## VALUE

dict = {tuple_1:copy_of_tuple_1, tuple_2:copy_of_tuple_2}

print(dict)


