#!/usr/bin/python
import sys
import time
import calendar
print "Hello Python!"

abc = 1;
xyz = 2;
if (abc>xyz):
	print "True"
else: 
	print "False"
a=1;
b=2;
c=3;

total = a + \
	b + \
	c

print "The total of a+b+c = ",total;

days = ['Monday', 'Tuesday', 'Wednesday',
'Thursday', 'Friday']
print "The days of the week are", days;

word = 'word'
sentence = "This is a sentence";
paragraph = """Hi There, 
I am Jayesh Chhatpar. How are you doing today???"""

print word
print sentence
print paragraph

#comments in the line

name = raw_input ("\nPlase enter your name: ");
print "You have entered: ",name

if (abc>xyz):
	print "False"
elif(abc<xyz):
	print "True"
else:
	print "Equal"

e,f,g= 4,5,"Jay"
print e 
print f 
print g

#List
mylist = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print mylist          # Prints complete list
print mylist[0]       # Prints first element of the list
print mylist[1:3]     # Prints elements starting from 2nd till 3rd 
print mylist[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print mylist + tinylist # Prints concatenated lists
mylist[2]=777
#Tuples
mytuple = ('abcd', 123 , 456.78, 'john', 772)
tinytuple = (123, 'john')

print mytuple; # Prints complete list
print mytuple[0]; # Prints first element of the list
print mytuple[1:3]; # Prints elements starting from 2nd till 3rd 
print mytuple[2:]; # Prints elements starting from 3rd element
print tinytuple *2 # Prints list two times
print mytuple + tinytuple # Prints concatenated lists
#mytuple[2]=777 
#TypeError: 'tuple' object does not support item assignment

#Note: Important difference between a tuple and list The main differences between lists and tuples are: Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated. Tuples can be thought of as read-only lists.


#Dictionary
#Python's dictionaries are kind of hash table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object. Dictionaries are enclosed by curly braces ({ }) and values can be assigned and accessed using square braces ([]).Dictionaries have no concept of order among elements. It is incorrect to say that the elements are "out of order"; they are simply unordered.

dictry={}
dictry['one']="This is one" 
dictry[2]="This is two" 
tinydict={'name':'john','code':6734, 'dept':'sales'}  
print dictry['one'] # Prints value for 'one' key
print dictry[2] # Prints value for 2 key
print tinydict  # Prints complete dictionary
print tinydict.keys() # Prints all the keys
print tinydict.values()# Prints all the values

#While Loop

count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

#For Loop
for letter in 'Python':     # First Example
   print 'Current Letter :', letter

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # Second Example
   print 'Current fruit :', fruit

print "Good bye!"


for num in range(10,20):  #to iterate between 10 to 20
	for i in range(2,num): #to iterate on the factors of the number
		if num%i == 0:      #to determine the first factor
		        j=num/i          #to calculate the second factor
    		        print '%d equals %d * %d' % (num,i,j)
             		break #to move to the next number, the #first FOR
   		else:                  # else part of the loop
      			print '%d is a prime number' % (num)

#Nested Loops

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
   	if not(i%j): break
      	j = j + 1
   	if (j > i/j) : 
		print i, " is prime"
   i = i + 1

print "Good bye!"

#Break Statement

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'Current Letter :', letter
  
var = 10                    # Second Example
while var > 0:              
   print 'Current variable value :', var
   var = var -1
   if var == 5:
      break

print "Good bye!"

#continue statement

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'Current Letter :', letter

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print 'Current variable value :', var
print "Good bye!"

#Pass Statement

for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'Current Letter :', letter

print "Good bye!"

#Python numbers
var1 = 10
var2 = 100
print var1
print var2
del var1
#	print var1
print var2

#Stirngs
var3='Hello World!'
var4="Python programming" 

print "var3[0]: ", var3[0]
print "var4[1:5]: ",var4[1:5]


var5='Hello World!'
print "Updated String: ", var5[:6]+'Python'


print "My name is %s and age is %d kg!" % ('Jayesh', 30) 

para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print para_str

#Lists
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5, 6, 7 ];
list3 = ["a", "b", "c", "d"]
print "list1[0]: ", list1[0]
print "list2[1:5]: ", list2[1:5]
print list1
del list1[2];
print "After deleting value at index 2 : "
print list1

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.sort();
print "List : ", aList

#Dictionary

dicty = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print "dict['Name']: ", dicty['Name']
print "dict['Age']: ", dicty['Age']

dicty['Age'] = 8; # update existing entry
dicty['School'] = "DPS School"; # Add new entry
print "dict['Age']: ", dicty['Age']
print "dict['School']: ", dicty['School']

del dicty['Name']; # remove entry with key 'Name'
dicty.clear();     # remove all entries in dict
del dicty ;        # delete entire dictionary

#print "dict['Age']: ", dicty['Age']
#print "dict['School']: ", dicty['School']

dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
print "Length : %d" % len (dict1)
print "Equivalent String : %s" % str (dict1)
print "Variable Type : %s" %  type (dict1)

print "Start Len : %d" %  len(dict2)
dict2.clear()
print "Start Len : %d" %  len(dict2)

dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = dict1.copy()
print "New Dictinary : %s" %  str(dict2)

seq = ('name', 'age', 'sex')
dict3 = dict3.fromkeys(seq)
print "New Dictionary : %s" %  str(dict3)
dict3= dict3.fromkeys(seq, 10)
print "New Dictionary : %s" %  str(dict3)
print "Value : %s" %  dict1.get('Age')
print "Value : %s" %  dict1.get('Education', "Never")
print "Value : %s" %  dict2.has_key('Age')
print "Value : %s" %  dict2.has_key('Sex')
print "Value : %s" %  dict3.items()
print "Value : %s" %  dict4.setdefault('Age', None)
print "Value : %s" %  dict4.setdefault('Sex', None)
dict1 = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }
dict1.update(dict2)
print "Value : %s" %  dict1
print "Value : %s" %  dict1.values()

#Time
ticks = time.time()
print "Number of ticks since 12:00am, January 1, 1970:", ticks
localtime = time.localtime(time.time())
print "Local current time :", localtime
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

#Calendar
cal = calendar.month(2017, 5)
print "Here is the calendar:"
print cal

#Functions
def printinfo(name, age=35): #This prints a passed info into this fuctions"
	print "Name: ",name
	print "Age: ", age
	return;

printinfo(age=50, name="miki")
printinfo(name="miki")


#Anonymous Functions/ Lambda Functions
sum = lambda arg1, arg2: arg1 + arg2;
# Now you can call sum as a function
print "Value of total : ", sum( 10, 20 )
print "Value of total : ", sum( 20, 20 )


#Return Statements in Functions
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2
   print "Inside the function : ", total
   return total;

total = sum( 10, 20 );
print "Outside the function : ", total 

#Pass by reference vs value
def changeme( mylist ):
   "This changes a passed list into this function"
   mylist.append([1,2,3,4]);
   print "Values inside the function: ", mylist
   return

mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist

def changeme( mylist ):
   "This changes a passed list into this function"
   mylist = [1,2,3,4]; # This would assig new reference in mylist
   print "Values inside the function: ", mylist
   return

mylist = [10,20,30];
changeme( mylist );
print "Values outside the function: ", mylist


#Default Arguments
def printinfo( name, age = 35 ):
   "This prints a passed info into this function"
   print "Name: ", name
   print "Age ", age
   return;

printinfo( age=50, name="miki" )
printinfo( name="miki" )

#Variable-length arguments
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   return;

printinfo( 10 )
printinfo( 70, 60, 50 )

#Modules
# Import module support
import mod

# Now you can call defined function that module as follows
mod.print_func("Zara")
mod.add(10,2)
mod.subtr(10,2)
mod.multi(10,2)
mod.divi(10,2)

import math
content = dir(math)
print content


#Files I/O
print "Python is really a great language,", "isn't it?"
str = raw_input("Enter your input: ");
print "Received input is : ", str

#Write to file
fo = open("test.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace
fo.write( "Python is a great language.\nYeah its great!!\n");
# Close opend file
fo.close()

#Read a file

fo = open("test.txt", "r+")
str = fo.read(10);
print "Read String is : ", str
# Close opend file
fo.close()

#Import Operating System: Rename file, Remove file, Make directory
import os
#os.rename("test.txt", "test1.txt")
#os.remove("test1.txt")
#s.rename("test.txt", "test1.txt")
#os.mkdir("test")
#os.chdir("test")
#os.getcwd() #getcwd() method displays the current working directory
#os.rmdir('dirname')
#os.rmdir("/tmp/test")

#Exception Handling
def KelvinToFahrenheit(Temperature):
   assert (Temperature >= 0),"Colder than absolute zero!"
   return ((Temperature-273)*1.8)+32
print KelvinToFahrenheit(273)
print int(KelvinToFahrenheit(505.78))
#print KelvinToFahrenheit(-5) #Function bails out when it gets a negative no.

try:
   #fh = open("/test/testfile.txt", "w")
   fh = open("testfile.txt", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print "Error: can\'t find file or read data"
else:
   print "Written content in the file successfully"
   fh.close()

