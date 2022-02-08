fruits = ('Mango' ,'Orange' , 'Pineapple' , 'Apple')
print(len(fruits))
print(fruits[0])
print(fruits[1])
last_fruits = len(fruits)-1
print(last_fruits)
print(fruits[-4])
print(fruits[-1])
print(fruits[0:])
print(fruits[0:4])
print(fruits[2:3])
print(fruits[::-1])
print(fruits[-4:])
print(fruits[-3:])
#fruits[1] = 'Banana'

fruits_1 = list(fruits)
fruits_1[1] = 'Banana'
print(fruits_1)
print('Orange' in fruits)
print('Banana' in fruits)
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
mix = fruits+vegetables
print(mix)
empty_tup = ()
brothers = ('Abc', 'def' , 'ghi', 'jkl')
Sisters = ('klo', 'lop', 'iop', 'lkj')
sibling = brothers + Sisters
print(sibling)
print(len(sibling))
family_members = list(sibling)
family_members.append('Father')
family_members.append("Mother")
print(family_members)
sib  = tuple(family_members)
print(type(sib))
Parents = family_members[8:10]
print(Parents)
Ssiblings = family_members[0:8]
print(Ssiblings)
Vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
Fruits = ('Mango' ,'Orange' , 'Pineapple' , 'Apple', 'Banana')
animal_products = ('Milk', 'Curd', 'Meat')

food_stuff_tp = Vegetables+Fruits+animal_products
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt[5:10])
first_three = food_stuff_lt[0:3]
print(first_three)
last_three = food_stuff_lt[-3:]
print(last_three)

del food_stuff_tp
#print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Iceland' in nordic_countries)