# a)

def print_names(names):
    for name in names:
        print(name)

print_names(["Kasia", "Basia", "Asia", "Jan", "Marian"])

# b)

def mult_list_i(nums):
    return [x * 2 for x in nums]

def mult_list_ii(nums):
    ans = []
    for num in nums:
        ans.append(num * 2)
    return ans

mult1 = mult_list_i([1,2,3,4,5])
mult2 = mult_list_ii([1,2,3,4,5])

# c)

def print_evens(nums):
    for num in nums:
        if num % 2 == 0:
            print(num)

print_evens(list(range(10)))

# d)

def print_every_second_number(nums):
    for i, num in enumerate(nums):
        if i % 2 == 0:
            print(num)

print_every_second_number(list(range(10)))