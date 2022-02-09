person = {'first_name' : 'Saurav', 'last_name':'Kumar', 'age': 29, 'country': 'India', 'is_married' : False,
          'skills':['JavaScript', 'Python', 'Selenium', 'MongoDb'], 'address' : {'street': 'Purani Bazaar', 'zipcode': 805110}}\

print(len(person))
print(person['first_name'])
print(person['skills'][1])
print(person['address']['street'])
print(person.get('city'))
print(person.get('skills'))
person['job_title'] = "QA"
person['skills'].append('API Testing')
print(person)
person['age'] = 30
print(person)
person.pop('first_name')
person.popitem()
del person['is_married']
print(person)
person['first_name'] = 'Saurav'
person['job_title'] = "QA"
person['is_married'] = False
print(person)
print(person.items())
keys = person.keys()
print(keys)
values = person.values()
print(values)
comp = ['TCS', 'Infy', 'Wipro', 'TechMahindra']
job_position = ['Dev', 'QA', 'DevOps', 'AWS']
dict_a = dict(zip(comp, job_position))
print(dict_a)

str_a = "abc 1 2 3 you 7"
a = 1
print(type(a))
str_split = str_a.split()

for i in str_split:
    if i.isdigit():
        print(i)
    else:
        pass

dog = {}
print(type(dog))
student =  {'first_name':'Saurav', 'last_name':'Kumar', 'gender':'M', 'age':29, 'Marital ststus':'Unmarried',
            'skills':['Python', 'JS', 'Selenium', 'API', 'SQL'], 'country': 'India', 'city': 'Vadodara',
            'address':{'street': 'Markapur', 'zipcode': 805110}}
print(student)
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].append('AWS')
student['skills'].append('GIT')
print(student)
student['RollNo'] =1234
print(student)
keys = student.keys()
print(keys)
vals = student.values()
print(vals)

student['address']['streetno']=123
print(student)
print(student['address']['streetno'])
print(student['skills'][0])
print(student.items())
del student['RollNo']

print(student)

print(student)
