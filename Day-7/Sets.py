fruits = {'banana', 'orange', 'mango', 'lemon'}
print(len(fruits))
print('mango' in fruits)
fruits.add('grapes')
print(fruits)
vegetables = {'tomato', 'potato', 'onion', 'cabbage', 'carrot'}

fruits.update(vegetables)
print(fruits)
fruits.remove('carrot')
print(fruits)
fruits.pop()
print(fruits)
fruits_a = ['banana', 'orange', 'mango', 'lemon','organic', 'banana']
fruits_b = set(fruits_a)
print(fruits_b)
st3 = fruits.union(fruits_b)
print(st3)
print(fruits.intersection(fruits_b))
print(fruits.issubset(fruits_b))
print(fruits.issuperset(fruits_b))
print(fruits.difference(fruits_b))

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_comp = {'Capgemini', 'Accenture', 'Cognizant'}
it_companies.update(it_comp)
print(it_companies)
it_companies.remove('Capgemini')
print(it_companies)
it_companies.discard('ABC')
C = A.union(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
print(len(age))
age_set = set(age)
print(age_set)
print(len(age_set))
str = "I am a teacher and I love to inspire and teach people."
str_split = str.split()
print(str_split)

str_set = set(str_split)
print(str_set)

def words(l):
    for i in l:
        print(i)

strb = "geeks for geeks"
stra =  "I am a teacher and I love to inspire and teach people."
s = set(strb.split(" "))
words(s)