fruits = ['banana', 'orange', 'mango', 'lemon']
last_index = len(fruits) - 1
print(last_index)
last_fruit = fruits[last_index]
print(last_fruit)
lst = ['item', 'item1', 'item2','item3', 'item4', 'item5']
first_item, seceond_item, third_item, *rest = lst
print(first_item)
print(rest)
print(fruits[::2])
print(lst[0:5:3])
print(fruits[1::])

l = [2,4,5,'Mango', {'A':123, 'B':'acs'}]
print(len(l))
print(l[3])
mixed_data_types = ['Saurav', 29, 178, 'Single', 'Bangalore']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']
print(mixed_data_types)
print(it_companies)
for x in it_companies:
    print(x)
print(*it_companies, sep = ',')
print(','.join(it_companies))
print(it_companies[0], it_companies[3], it_companies[5])
it_companies[4] = 'Netflix'
print(it_companies)
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('Chickoo')
print(fruits)
fruits.insert(3, 'Watermaelon')
print(fruits)
it_companies.append('Flipkart')
it_companies.insert(3, 'Infosys')
print(it_companies[1].upper())
print('#'.join(it_companies))
ban = 'banana' in fruits
print(ban)
it_companies.sort(reverse=True)
print(it_companies)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
fruits = ['banana', 'orange', 'mango', 'lemon']
more_fruits = ['Chickoo', 'Watermelon', 'Grapes']
fruits.extend(more_fruits)
print(fruits)
print(fruits[0:4])
print(fruits[-3:])
fruits.remove('banana')
print(fruits)
del fruits[1]
print(fruits)
fruits.insert(1, 'mango')
print(fruits)
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)
print(it_companies)
del it_companies[-1]
print(it_companies)
it_companies.clear()
print(it_companies)
print(fruits)
print(fruits[0:])
print(fruits[-4:])
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
del fruits[0:]
print(fruits)
back_end = ['Node','Express', 'MongoDB']
all_end = front_end + back_end
print(all_end)
all_end_copy = all_end.copy()
print(all_end_copy)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
max_age  = max(ages)
print(max_age)
min_age = min(ages)
print(min_age)
ages.append(max_age)
ages.append(min_age)
print(ages)
sum_age = sum(ages)
ln_age = len(ages)
avg_age = sum_age//ln_age
print(avg_age)
print(max_age - min_age)
my_list = []
start = max_age
end = min_age
my_list.extend(range(start, end))

print(my_list)

assert abs(max_age) == 26
length = len(ages)//2
print(length)
first_half = ages[:6]
second_half = ages[6:]
print(first_half)
print(second_half)
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
*rest, f_item, s_item, t_item, fr_item =  countries
print(*rest)
