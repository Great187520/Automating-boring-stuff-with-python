name = ['bossu', 'John', 'paul']
for i in range(len(name)):
    print('index ' +str(i)+ ' has the name: '+ name[i])

myPets = ['Tommy', 'Scooby', 'Jerry']
name= str(input('Enter your pets name: '))

if name in myPets:
    print('I have pet: '+ name)

else:
    print(name + ' is not my pet')
