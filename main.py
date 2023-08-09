# # # # # var1 = 'value'
# # # # # print(var1[0])
# # # # # print(var1[1:])
# # # # # print(len(var1))

# # # # # num1 = 1
# # # # # print(num1)
# # # # # print(type(num1))

# # # # # comp = complex(4 + 6j)
# # # # # print(comp)

# # # # # str1='hello'
# # # # # str2= str1[0:2]+'mm'+str1[4:]
# # # # # print(str2)

# # # # # create calculater app

# # # # # we will learn about how to deal with if else condition in python and how to
# # # # # take input from user

# # # # # what is if else condition

# # # # # if else condition is used to check the condition and based on the condition
# # # # # we can perform some action

# # # # # if >>> true >> perform some action
# # # # # else >>> false >> perform some action

# # # # # if else condition syntax
# # # # # import numbers

# # # # # choose1= input('enter your choice: ')
# # # # # #  convert string to int

# # # # # if choose1.isdigit():
# # # # #     print(choose1)
# # # # # else:
# # # # #     print('please enter number only')

# # # # # for loop in python

# # # # # for loop is used to iterate over a sequence
# # # # # i = 0
# # # # # for i in range(2,10):
# # # # #     if i % 2 == 0:
# # # # #         print(i)
# # # # #     else:
# # # # #         print('odd')
# # # # # home work for you

# # # # # create a program which will take input from user and check if the number is
# # # # # even or odd

# # # # # evenOrOdd = int(input('enter your number: '))
# # # # # if evenOrOdd == 0:
# # # # #     evenOrOdd = int(input('enter your number: '))
# # # # # else:
# # # # #     if evenOrOdd % 2 == 0:
# # # # #         print('even')
# # # # #     else:
# # # # #         print('odd')

# # # # # 2 create a program which will take input from user and check if the number
# # # # # is prime or not

# # # # # primeOrNot = int(input('enter your number: '))
# # # # # # primeOrNot = primeOrNot + 1
# # # # # if primeOrNot > 1:
# # # # #     for i in range(2, primeOrNot):
# # # # #         if primeOrNot % i == 0:
# # # # #             print('not prime')
# # # # #             break
# # # # #     else:
# # # # #             print('prime')

# # # # #  3 . take input from user as string and check if the string have l or u in
# # # # # it and replase it with *
# # # # # and aleart the user that
# # # # # the word have the u and  l and print the index for these lutters
# # # # # counter = 0
# # # # # while counter < 5:
# # # # #     print('_'*50)
# # # # #     userInput = input('enter your string: ')

# # # # #     for i in range(len(userInput)):
# # # # #         if userInput[i] == 'l' or userInput[i] == 'u':
# # # # #             print('the word have the u and  l and print the index for these
# # # # # lutters')
# # # # #             print(i)
# # # # #             userInput = userInput.replace(userInput[i], '*')
# # # # #             print(userInput)
# # # # #     counter = counter + 1

# # # # # elif  condition syntax
# # # # # what is elif condition in python
# # # # # elif is used to check multiple condition

# # # # # if 1 == 2:
# # # # #     print('1')
# # # # # elif 1 == 3:
# # # # #     print('2')
# # # # # else:
# # # # #     print('unknown')

# # # # # switch case in python
# # # # # what is switch case in python and how to use it

# # # # # switch case is used to check multiple condition

# # # # # switch case syntax

# # # # # switch:
# # # # #     case 1:
# # # # #        print('1')

# # # # #    case 2:
# # # # #       print('2')

# # # # #   default:
# # # # #      print('unknown')

# # # # # while loop in python

# # # # # while loop is used to iterate over a block of code as long as the condition
# # # # # is true

# # # # # while loop syntax
# # # # #  check an input from the user and if the word is == the value that allready
# # # # # stored in the variable
# # # # #  print correct in while loop
# # # # #  else print wrong and ask the user to enter the word again

# # # # # secretWord = 'python'
# # # # # # userInput = input('enter your word: ')
# # # # # c = 0
# # # # # check = True
# # # # # while check:
# # # # #     userInput = input('enter your word: ')
# # # # #     c = c + 1
# # # # #     if userInput == secretWord:
# # # # #         print('correct')
# # # # #         break
# # # # #     else:
# # # # #         print('wrong')
# # # # #         if c == 2:
# # # # #             check = False
# # # # #             print('you have reached the limit')
# # # # #             break

# # # # # home work for you

# # # # # all the last previous home works will be added in 1 while loop
# # # # # the first is to check if the number is even or odd 3 times
# # # # # the second is to check if the number is prime or not 3 times
# # # # # the third is to check if the string have l or u in it and replase it with *
# # # # # 3 times

# # # # # functions in python

# # # # # what is function in python and how to use it

# # # # # function is a block of code which only runs when it is called

# # # # # function syntax
# # # # # 1- function without parameters
# # # # # def myFunction():
# # # # #     print('hello world')
# # # # #     // code here

# # # # # myFunction()

# # # # # def myFunction():
# # # # #     print('hello world')

# # # # # myFunction()

# # # # # 2 - function with parameters

# # # # # def myFunction(partmenter, partmenter2):
# # # # #    print(partmenter)
# # # # #    print(partmenter2)

# # # # # myFunction('hi', 'hello')

# # # # # 3 - function with return

# # # # # def myFunction1():

# # # # #    return 'hello world'

# # # # # print(myFunction1())

# # # # # live example about function in python
# # # # # create a function which will take 2 parameters and return the sum of these 2
# # # # # parameters

# # # # # num1 = int(input('enter your first number: '))
# # # # # num2 = int(input('enter your second number: '))

# # # # # def sum(num1, num2):
# # # # #     return num1 + num2

# # # # # print(sum(num1, num2))

# # # # # home work for you

# # # # # convert the last home work to function (prime number, even or odd, string
# # # # # with l or u)

# # # # # number1 = int(input('enter a number to check if it is prime or not:'))
# # # # # def ifprime(number1):
# # # # #     for i in range(2,number1):
# # # # #       if number1 % i == 0:
# # # # #         print ('the number is not prime')
# # # # #         break
# # # # #       else:
# # # # #         print('the number is not prime')
# # # # #   for i in range(2,number1):
# # # # #     if number1 % i == 0:
# # # # #       print ('the number is not prime')
# # # # #       break
# # # # #     else:
# # # # #       print('the number is not prime')

# # # # # def oddoreven(number2):
# # # # #     if number2 % 2 == 0:
# # # # #       print('even')
# # # # #     else:
# # # # #       print('odd')

# # # # # var1 = input('enter a string to check if it has l or u: ')
# # # # # def str1(var):
# # # # #     for i in range(0,len(var)):
# # # # #       if var[i]=='u' or var[i]=='l':
# # # # #             var=var.replace(var[i] , '*')
# # # # #     print(var)

# # # # # ifprime(number1)
# # # # # oddoreven(number1)
# # # # # str1(var1)

# # # # # #    Alice, that was a great trick!
# # # # # #    I can't wait to see your next trick, Alice.
# # # # # #    David, that was a great trick!
# # # # # #    I can't wait to see your next trick, David.
# # # # # #    Carolina, that was a great trick!
# # # # # #    I can't wait to see your next trick, Carolina.

# # # # # def magicTrick(names):
# # # # #     for i in names:
# # # # #         print(i + ', that was a great trick!')
# # # # #         print("I can't wait to see your next trick, " + i + '.\n')

# # # # # magicTrick(names)

# # # # # counter=0
# # # # # while counter<3:

# # # # #     word=input("enter a word to check")

# # # # #     if "i" in word and "u" in word:

# # # # #         print("the word have a both of letters")

# # # # #         replace_words=word.replace("i", "*").replace("u","*")

# # # # #         print("replace_words", replace_words)

# # # # #         i_indexing=[i for i in range(len(word)) if word [i]=="i"]

# # # # #         u_indexing=[i for i in range(len(word)) if word [i]=="u"]
# # # # #         print("the indexing of i : ",i_indexing)
# # # # #         print("the indexing of u : ",u_indexing)

# # # # #     elif "i" in word:

# # # # #        print("the word have i just")
# # # # #        replace_i=word.replace("i","**")
# # # # #     #    I_indexing=[i for i in range(len(word)) if word (i)=="i"]
# # # # #        print("the indexing of i : "+replace_i)
# # # # #     elif "u" in word:

# # # # #        print("the word have u just")
# # # # #        replace_u=word.replace("u","***")
# # # # #        U_indexing=[i for i in range (len(word)) if word [i]=="u"]
# # # # #        print("the indexing of u :", U_indexing)
# # # # #     else:
# # # # #      print("we dont have the letters ")
# # # # #     counter=counter+1
# # # # #     #task2

# # # # # numTest = int(input("enter a number to check if it is prime or not: "))
# # # # # for i in range(2, numTest):
# # # # #     if numTest % i == 0:
# # # # #         print("the number is not prime")
# # # # #         break
# # # # # else:
# # # # #         print("the number is prime")
# # # # # counter = 0
# # # # # names = ['Alice', 'David', 'Carolina']
# # # # # for i in names:
# # # # #     # print(counter)
# # # # #     # print(i)
# # # # #     if i == 'Alice':
# # # # #         names = names[0:counter] + names[counter + 1:]
# # # # #         print(names)
# # # # #     counter = counter + 1

# # # # # solve the index[0] problem  in the list to print all the names except the
# # # # # first one
# # # # # try to add new value to the list and print it using the user input

# # # # # names = ['Alice', 'David', 'Carolina', 9]
# # # # # test = ['test']
# # # # # names = names+ ['mohammed']
# # # # # print(names)

# # # # # methods for list in python

# # # # # append method : is used to add new value to the list at the end of the list
# # # # # names.append('mohammed')
# # # # # names = names[0:2] +[ 'value'] + names[2:]

# # # # # insert method : is used to add new value to the list at the
# # # # # index that you want
# # # # # names.insert(1, 'mohammed')
# # # # # print(names)

# # # # # list1 = [1, 2, 3, 4, 5, 1, 1, 4]
# # # # # list2 = [6, 7, 8, 9]
# # # # # extend method : is used to add new list to the list at the end of the list

# # # # # sumList= 0
# # # # # for i in list1:
# # # # #     sumList = sumList + i

# # # # # sum  : is used to get the sum of the list
# # # # # print(sum(list1))

# # # # # count : is used to get the count of the value in the list
# # # # # print(list1.count('1'))
# # # # # print(len(list1))   # len : is used to get the length of the list

# # # # # print the index of the value in the list

# # # # # counter = 0

# # # # # for i in list1:
# # # # #     if i == 4:
# # # # #         print(counter)

# # # # #     counter = counter + 1

# # # # # index : is used to get the index of the value in the list

# # # # # print(list1.index('1'))

# # # # # maxValue = 0

# # # # # minValue = 0

# # # # # print(max(list1))
# # # # # print(min(list1))

# # # # # pop : is used to remove the value from the list based on the index

# # # # # print(list1.pop())  # remove the last value from the list
# # # # # print(list1)

# # # # # # remove : is used to remove the value from the list based on the value

# # # # # print(list1.remove(2))
# # # # # print(list1)

# # # # # # reverse : is used to reverse the list
# # # # # # sort : is used to sort the list
# # # # # print(list1.reverse()) # reverse the list
# # # # # print(list1)

# # # # # list1.sort(reverse=True) # sort the list in descending order
# # # # # list1.sort() # sort the list in descending order

# # # # # print(list1)

# # # # # home work for you

# # # # # create a list of 10 numbers and print the sum of these numbers
# # # # # but the list should
# # # # # have 2 numbers as string and the rest as numbers also int and float
# # # # # avarage of the list
# # # # # max and min of the list
# # # # # print the index of the max and min of the list

# # # # #

# # # # # list3 = [1, 2, 3, 4, 5, 6, 7, 'a', 9, '10', '11']

# # # # # Dectonary in python
# # # # # what is dectonary in python and how to use it

# # # # # dectonary is used to store data in key value pair
# # # # # {'key':value , 'key1':value}

# # # # # person1 = {'name': 'mohammed', 'age': 30, 'country': 'jordan'}
# # # # # print(person1)

# # # # # how we can use the dectonary in python in real life

# # # # # create a dectonary which will store the data of the student
# # # # # name1 = 'mohammed'
# # # # # age1 = 30
# # # # # country1 = 'jordan'

# # # # # person1 = [name1, age1, country1]

# # # # # Adding New Key-Value Pairs

# # # # # person1['city'] = 'amman'
# # # # # person1['job'] = 'developer'
# # # # # person1['skills'] = ['python', 'java', 'c++']
# # # # # person1['skills'].append('javascript')
# # # # # person1['perant'] = {'father': 'ali', 'mother': 'sara'}

# # # # # # print(person1['perant'])

# # # # # # print all the person data in  good view

# # # # # print("-" * 50)
# # # # # print('name: ' + person1['name'])
# # # # # print('age: ' + str(person1['age']))
# # # # # print('country: ' + person1['country'])
# # # # # print('city: ' + person1['city'])
# # # # # print('job: ' + person1['job'])
# # # # # print('skills: ' + str(person1['skills']))
# # # # # print('father: ' + person1['perant']['father'])
# # # # # print('mother: ' + person1['perant']['mother'])

# # # # # print("-" * 50)

# # # # # # del person1['perant']['father']
# # # # # person1['perant']['father'] = 'salem'
# # # # # print(person1['perant'])

# # # # # print("-" * 50)

# # # # # for key,value in person1.items():
# # # # #     print("\nKey: " + str(key))
# # # # #     print("Value: " + str(value))

# # # # # print("-" * 50)

# # # # # methods for dectonary in python

# # # # # clear : is used to clear the dectonary
# # # # # person1.clear()
# # # # # print(person1)

# # # # # copy : is used to copy the dectonary
# # # # # person2 = person1.copy()
# # # # # print(person2)

# # # # # fromkeys : is used to create new dectonary from the keys that you want
# # # # # print("-" * 50)

# # # # # keys = ['name', 'age', 'country', 'city', 'job', 'skills']
# # # # # values =
# # # # # ['mohammed', 30, 'jordan', 'amman', 'developer', ['python', 'java', 'c++']]
# # # # # person3 = dict.fromkeys(keys, values)
# # # # # print(person3)

# # # # # print("-" * 50)
# # # # # get : is used to get the value of the key

# # # # # print(person1.get('name'))

# # # # # items : is used to get all the items in the dectonary
# # # # # print(person1.items())

# # # # # keys : is used to get all the keys in the dectonary
# # # # # print(person1.keys())

# # # # # pop : is used to remove the key from the dectonary
# # # # # print(person1.pop('name'))

# # # # # popitem : is used to remove the last key from the dectonary

# # # # # print(person1.popitem())

# # # # # setdefault : is used to set the default value for the key if the key is not
# # # # # exist

# # # # # print(person1.setdefault('name', 'ali'))

# # # # # home work for you

# # # # # create a dectonary which will store the data of the student as a user input
# # # # # (name, age, country, city, job, skills, perant)

# # # # # print all the person data in  good view

# # # # # ask the user if he want to add new student or not if yes add new student if
# # # # # no print the data of the students

# # # # #
# # # # # list3 = ['1', 2.5, 3, 'r', 5, 6.001, 7, 0.02, 9, 6]
# # # # # summation = 0.0

# # # # # for n in  list3 :
# # # # #   print(type(n))

# # # # # #   n = '1'
# # # # #   try:
# # # # #       summation += int(n)
# # # # #       list3[list3.index(n)] = float(n)

# # # # #   except ValueError:
# # # # #       print('not a number')
# # # # #       list3.remove(n)
# # # # #       print(n)

# # # # # print(list3)
# # # # # maxi=max(list3)
# # # # # mini=min(list3)
# # # # # print('Sum=', summation)
# # # # # print('Avg=', summation / 10)
# # # # # print( maxi)
# # # # # print( mini)

# # # # # print('Index of max. value', list3.index(max(list3)))
# # # # # print('Index of min. value', list3.index(min(list3)))

# # # # # Class in python and how to use it oop in python

# # # # # class : is used to create a class in python

# # # # # class person():

# # # # # class Dog():
# # # # #         def __init__(self, name, age):
# # # # #             """Initialize name and age attributes."""
# # # # #             self.name = name
# # # # #             self.age = age
# # # # #         def sit(self):
# # # # #             """Simulate a dog sitting in response to a command."""
# # # # #             print(self.name + " is now sitting.")
# # # # #         def roll_over(self):
# # # # #            """Simulate rolling over in response to a command."""
# # # # #            print(self.name.title() + " rolled over!")

# # # # # dog1 = Dog('rex', 2)
# # # # # print(dog1.name)
# # # # # print(dog1.age)
# # # # # dog1.sit()
# # # # # dog1.roll_over()

# # # # # # print(person.setdefault('name','sami'))

# # # # # n = int(input('enter the number of elements:'))

# # # # #  student={}
# # # # #  ask the user for the key and the type of the value

# # # # # student={'name':'', 'age':0, 'country':'', 'city':'', 'job':'', 'skills':[], 'perant':{'father':'', 'mother':''}}
# # # # # print(student)
# # # # # for i in student:
# # # # #     if type(student[i]) == int:

# # # # #         tryAndExpect = True
# # # # #         while tryAndExpect:
# # # # #                 try:
# # # # #                     student[i] = int(input('enter the ' + i + ':'))
# # # # #                     tryAndExpect = False
# # # # #                 except ValueError:
# # # # #                     print('not a number try again ')

# # # # #     elif type(student[i]) == list:
# # # # #         times = int(input('how many skills do you have?'))
# # # # #         for j in range(times):
# # # # #             student[i].append(input('enter the ' + i + ':'))
# # # # #     elif type(student[i]) == dict:
# # # # #         student[i]['father'] = input('enter the father name:')
# # # # #         student[i]['mother'] = input('enter the mother name:')

# # # # #     else:
# # # # #         student[i] = input('enter the ' + i + ':')

# # # # # # home work for you

# # # # # # add  2 dexonary to the student dectonary (greads:{math:50, english:70} , techers:{math:ahmad, english:reem})
# # # # # time3 = int(input('how many dectonary do you want to add?'))
# # # # # for i in range(time3):
# # # # #         new_dec=input('enter the key:')
# # # # #         student[new_dec]={}
# # # # #         times1 = int(input('how many '+ new_dec +' do you want to add ?'))
# # # # #         for j in range(times1):
# # # # #                     new_sub_key= input('enter the ' + new_dec + 'number:'+str(j+1) + ':')

# # # # #                     student[new_dec][new_sub_key] = input('enter the value:')

# # # # # print('_'*50)

# # # # # for i in student:
# # # # #     print(i, ':', student[i])
# # # # # # for i in range(n):
# # # # # #   key =input('enter the key:')
# # # # # #   value = input ('enter the value :')
# # # # # #   student[key] = value

# # # # # # print(student)

# # # # # # for i in (student):
# # # # # #   print(i , ':', student[i])

# # # # # # an_other_student = bool(input('do you want to add an other student?'))
# # # # # # if an_other_student==True:
# # # # # #   n = int(input('enter the number of elements:'))

# # # # # #   student={}
# # # # # #   for i in range(n):
# # # # # #     key =input('enter the key:')
# # # # # #     value = input ('enter the value :')
# # # # # #     student[key] = value

# # # # # #     print(student)

# # # # # class Person():

# # # # #     def __init__(self, name, age):
# # # # #         self.name = name
# # # # #         self.age = age

# # # # #     def __str__(self):
# # # # #         return f'name is {self.name} and age is {self.age}'

# # # # # obj1=   Person('mohammed', 30)
# # # # # print(obj1)
# # # # # obj109 = Non
# # # # # print(obj109)

















# # # # # student = {}
# # # # # insertTime = int(input('how many key do you want to add?'))
# # # # # for i in range(insertTime):
# # # # #         stKey = input('enter the key:')
# # # # #         keyType = input('enter the type of the key where 1 for Str 2 for int 3 for list 4 for dict:')

# # # # #         if (int(keyType) == 1):
# # # # #             student[stKey] = input('enter the value for ' + stKey + ' :')
# # # # #         elif (int(keyType) == 2):
# # # # #             student[stKey] = int(input('enter the value  for ' + stKey + ' :'))

# # # # #         elif (int(keyType) == 3):

# # # # #                 times = int(input('how many ' + stKey + ' do you have?'))
# # # # #                 student[stKey] = []
# # # # #                 for j in range(times):
# # # # #                     student[stKey].append(input('enter the ' + stKey + ':'))

# # # # #         elif (int(keyType) == 4):
# # # # #             time3 = int(input('how many dectonary do you want to add?'))
# # # # #             for i in range(time3):
# # # # #                     new_dec = input('enter the key:')
# # # # #                     student[new_dec] = {}
# # # # #                     times1 = int(input('how many ' + new_dec + ' do you want to add ?'))
# # # # #                     for j in range(times1):
# # # # #                                 new_sub_key = input('enter the ' + new_dec + 'number :' + str(j + 1) + ':')

# # # # #                                 student[new_dec][new_sub_key] = input('enter the value:')

# # # # # print(student)


# # # students = []

# # # reInter = True

# # # while reInter:
# # #     student= {}



# # #     insertTime = int(input('how many key do you want to add?'))
# # #     for i in range(insertTime):
# # #         decKey = input('enter the key:')
# # #         decValueTybe = int(input('enter the type of the value where 1 for Str 2 for int 3 for list 4 for dict:'))
# # #         if decValueTybe ==1:
# # #             decValue = input('enter the value:')
# # #         elif decValueTybe ==2:
# # #             decValue = int(input('enter the value:'))
# # #         elif decValueTybe ==3:
# # #             decValue = []
# # #             times = int(input('how many ' + decKey + ' do you have?'))
# # #             for j in range(times):
# # #                 decValue.append(input('enter the ' + decKey + ':'))
# # #         elif decValueTybe ==4:
# # #             print('you can not add a dict')
# # #             decValue = {}
# # #             times = int(input('how many ' + decKey + ' do you have?'))
# # #             for j in range(times):
# # #                 keynew = input('enter the key:')
# # #                 newValue = input('enter the value:')
# # #                 decValue[keynew] = newValue

# # #         student[decKey] = decValue
# # #     # print(student)
# # #     anyVar = student
# # #     students.append(student)

# # #     continueOrNot = input('do you want to add an other student?')
# # #     if continueOrNot == 'no':
# # #         reInter = False


# # # print(students)

# # # class person:

# # # #     def __init__(self, name, age, city):
# # # #         self.name = name
# # # #         self.age = age
# # # #         self.city = city

# # # #     def __str__(self):
# # # #         return f'name is {self.name} and age is {self.age} and city is {self.city}'

# # # # obj2 = {'name': 'mohammed', 'age':30, 'city':'riyadh'}
# # # # obj1 = person(age=30,name='mohammed' , city='riyadh')
# # # # print(obj1)
# # # # print(obj2)



# class Client:


#     def __init__(self, NameObj ='deafult', PhoneObj=123456789 , EmailObj="mohd@gmail.com", PurObj=5 ):
#         self.name = NameObj
#         self.phone = PhoneObj
#         self.email = EmailObj
#         self.purchies = PurObj
#     def __str__(self):
#         print('hello')
#         return f'name is {self.name} and phone is {self.phone} and email is {self.email} and purchies is {self.purchies}'

#     def talk(self):
#         return f'hello my name is {self.name}'
# obj1 = Client(EmailObj="asjkhbcda",NameObj='mohammed', PhoneObj=123456789)
# obj2 = Client('ahmed', 123456789)
# print(obj1)

#  function : block of code that do a specific task
#  method : function inside a class

class Student:
    def __init__(self,name="deafult",age=18,grade=1, city='riyadh',speacialise = 'computer'):
        self.name = name
        self.age = age
        self.grade = grade
        self.city = city
        self.speacialise = speacialise
    def __str__(self):
        return f'name is {self.name} and age is {self.age} and grade is {self.grade} and city is {self.city} and speacialise is {self.speacialise}'


    def addCorse(self, newCourse):
        return f'hello {self.name} you have added {newCourse} to your courses'

# display instructions for the user
print('hi to my program')
name = input('enter your name:')
age = int(input('enter your age:'))
grade = int(input('enter your grade:'))
city = input('enter your city:')
speacialise = input('enter your speacialise:')
#  pass the user input to the class
student1= Student(name,age,grade,city,speacialise)
print('information added successfully')
# added new course to the student courses method 
print("add new course ")
course= input('enter the course name:')
print(student1.addCorse(course))
print(student1)

