first_name = 'thirty'
second_name = 'days'
space = ''
third_name = 'of'
fourth_name = 'python'
full_name = first_name + second_name + space + fourth_name
print(f"estoy haciendo los {first_name} {second_name} {space}{third_name} {fourth_name}")

new_name = 'coding'
second_space = 'for'
todo = 'all'
print(f"tengo que hacer la {new_name} {second_space} {todo}")

company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

print(company.capitalize())
print(company.title())
print(company.swapcase())

remove_coding = company[7:15]
print(remove_coding)

print(company.index('for'))
print(company.replace('coding','python'))

print(company.replace('coding for all', 'Python for Everyone'))
print 