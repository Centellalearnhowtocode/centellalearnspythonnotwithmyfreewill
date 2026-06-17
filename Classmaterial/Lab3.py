#1. accessing value in dictionary
person = {
  'first_name': 'John',
  'last_name':'Doe',
  'age':19,
  'favorite_color':['pink','red'],
  'status': True
}
print(person['first_name'])
print(person['last_name'])
print(person['favorite_color'])
print('Using get method:')
print(person.get('age'))

#2. Adding/modifying key-value pair
person2 = {
  'first_name2': 'Centella',
  'last_name2':'Asiatica',
  'age2':19,
  'favorite_color2':['Green','Pink'],
  'status': True
}
print(f'person2 ={person2}')
person['gender']='Princess'
print(f'\n added new key-value to person ={person2}')
#Modify value o exisiting key
person['age']=30
print(f'\n modified person={person2}')

#3 Removing key-value pairs
person3 = {
  'first_name3': 'John',
  'last_name3':'Cena',
  'age':20,
  'favorite_color3':['pink','violet'],
  'status': True
}
print(f'person = {person3}')
del person3['status']
del person3['favorite_color3']
print(f'person={person3}')

#4.Looping in Dictionaries
stocks = {
  'AAPL':121,
  'AMZN':3380,
  'MSFT':219,
  'BIIB':169,
  'LVGO':144,
}
print(f'stocks = {stocks}')
new_stocks = {}
for key,value in stocks.items():
  new_stocks[key]= value*1.02

print(f'new stocks = {new_stocks}')

#Dictionarie Comprehension
stocks2 = {
  'AAPL':121,
  'AMZN':3380,
  'MSFT':219,
  'BIIB':169,
  'LVGO':144,
}
print(f'stocks = {stocks2}')
new_stocks2 = { key:value*1.02 for key, value in stocks2.items()}
print(f'new stocks = {new_stocks2}')