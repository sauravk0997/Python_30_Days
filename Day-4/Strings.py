str = 'Thirty', 'Days', 'Of', 'Python'
result =' '.join(str)
print(result)
company = "Coding For All"
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[0:9])
print(company.find("For"))
print(company.index("For"))
print(company.replace("Coding", "Python"))
str = 'Coding For All'
print(str.split(' '))
print(company[9])
print(company.rfind("l"))
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.rfind("because"))
print(sent.find("because"))
print(sent[31:54])
sub_str = "Coding"
print(company.rindex(sub_str,0))
print(sub_str[0:5:2])
print(company.startswith("Coding"))
print(company.endswith("Coding"))
str1  = '   Coding For All      '
print(str1.strip())
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())
web_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(web_tech))
print("I am enjoying this challenge.\nI just wonder what is next.")
print("name,\tAge, \tCountry, \tCity")
print("Asabeneh, \t25. \tIndia, \t Bangalore")
radius = 10
area = 3.14 * radius ** 2
result = "The area of a circle with radius {}  is {}.".format(radius, area)

print(result)