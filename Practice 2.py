def changeLit(lst):
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    else:
        print("введи нормально")

my_list = [1, 2, 3, 4, 5]
changeLit(my_list)
print(my_list)



def listToDict(lst):
    return {key: key for key in lst}
my_list = ['a', 'b', 'c', 'd']
result_dict = listToDict(my_list)
print(result_dict)




def dataToSet(data):
    my_set = set(data)
    set_length = len(my_set)
    return my_set, set_length
data = [1, 2, 3, 3, 4, 5, 5, 5]
result_set, length = dataToSet(data)
print(result_set)
print(length)