def list_transformation(lst1:list, lst2:list) -> list:
    return list(set([x ** 3 for x in lst1] + [x ** 3 for x in lst2]))

print(list_transformation(list(range(6)), list(range(3))))