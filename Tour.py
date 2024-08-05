
import pyttsx3
engine=pyttsx3.init()
engine.say('Hello...I am your alexa..Welcome')
engine.say('opening alpha travels...')
engine.runAndWait()

import turtle 
pen = turtle.Turtle()
turtle.bgcolor('white')
pen.write("LOADING...", font=("Times New Roman", 22, "italic"),align='left')  
def draw(space,x,y):
  for i in range(x):
    for j in range(y):
        pen.dot()
        pen.forward(space)
    pen.backward(space*y)
      
    turtle.bgcolor('violet')
    pen.right(60)
    pen.forward(space)
    turtle.bgcolor('red')
    pen.left(5)
    turtle.bgcolor('white')
pen.penup()
draw(10,6,10)
turtle.bgcolor('pink')


engine=pyttsx3.init()
engine.say('Here it is..\nEnter the appropriate details')
engine.runAndWait()

print('---------------------------------------------------------------------------------')
print("                                  WELCOME TO ALPHA'S TRAVELS                   ")
print('---------------------------------------------------------------------------------')
print(' ')
print('Life is a journey, not a destination')
print('')
print('ENTER THE REQUIRED INFORMATION- ')
print('')
a=input('Enter your Name: ')
print('')
while True:
    b=int(input('Enter age: '))
    if b<100:
        break

    else:
        
        print('Pls Enter Proper Age')
        continue
print('')
while True:
    c=input('Enter your contact number: ')
    if len(c)==10:
        break
    else:
        import pyttsx3
        engine=pyttsx3.init()
        engine.say('Please Enter 10 digit contact number')
        engine.runAndWait()
        continue
print('')
d=input('Enter your email id-')
print('')
print('Thank you for sharing your details,we will try our best to provide our service')
print('')
print('Here are some tourist places that you would love to travel-')
print('')
print('-------------------------------------------------------------------------------')
print('            1.KERALA                  ')
print('            2.ANDAMAN AND NICOBAR ISLAND      ')
print('            3.MALDIVES  ')
print('            4.THAILAND'          )
print('            5.DARJEELING')
print('            6.SRI-LANKA')
print('------------------------------------------------------------------------------')
print('')
print('')
f=True
while f==True:
    e=input('Enter the city or country number that you would like to visit - ')
    if e=='1':
        print('')
        print('KERALA For 3 days 2 nights:\n HOTEL:  Sara devan \n PLACES:\n Kerala backwaters \n Tea Gardens \n Lulu mall \n leisure time walking with family \n TOTAL PACKAGE:Rs 20,000')
    elif e=='2':
        print('')
        print('ANDAMAN AND NICOBAR ISLAND For 3 days 2 nights:\n HOTEL:  Neon bay beach resort \n PLACES:\n Havelock island \n The Cellular Jail \n Diglipur \n leisure time walking with family \n TOTAL PACKAGE:Rs 35,000')
    elif e=='3':

        print('MALDIVES For 3 days 2 nights:\n HOTEL:  Lily beach resort and spa \n PLACES: \n Hulhumde \n Male(Water rides) \n Artificial beach \n leisure time walking with family \n TOTAL PACKAGE:Rs 1,00,000')
    elif e=='4':

        print('THAILAND For 3 days 2 nights:\n HOTEL:  Golden sea Pataya \n PLACES: pearl museum\n Jomtien beach  \n Nong Nooch tropical garden \n leisure time walking with family \n TOTAL PACKAGE:Rs 67,000')
    elif e=='5':
        
        print('DARJEELING For 3 days 2 nights:\n HOTEL : Darjeeling International \n PLACES: Tiger Hill \n Bataria loop \n The Himalaya Hifhway \n leisure time walking with family \n TOTAL PACKAGE:Rs 34,000')
    elif e=='6':
        
        print('SRI-LANKA For 3 days 2 nights:\n HOTEL:  Kandy house \n PLACES:Kandy \n Galle \n Udawalawe National Park \n leisure time walking with family \n TOTAL PACKAGE:Rs 52,000')
    else:
        print('')
        print('You have choosen an incorrect option.Please retry.')
    print('')

    g=input('Do you want to repeat[YES/NO](in caps):')
    if g=='YES':
        
        continue
    else:
         break
    
print(' 1-Looking forward to book \n 2-For Inquiry')
print('')
h=input('Enter your choice 1 or 2: ')
print('')
if h=='1':
    j=int(input('ENTER TOTAL NUMBER OF PERSONS: '))
    engine.say('Enter number of adults to travel whose age in plus 5')
    engine.runAndWait()
    z=input('ADULTS(+5): ')
    engine.say('Enter number of child to travel whose age is below 5     If  none Enter none')
    engine.runAndWait()
    x=input('CHILD(below 5 years): ')
    print('')
    r=input('ENTER YOUR FULL ADDRESS WITH CITY: ')
    print('')
    i=input('Enter the city number that you want to visit: ')
    print('')
    if i=='1':
        print('In kerala total package for single person trip for 3 days 2 nights is 20,000 for 5 days 4 nights its + 10,000(for children under 5 years its free)')
        '''engine=pyttsx3.init()
        engine.say('In kerala total package for single person trip for 3 days 2 nights is 20,000 for 5 days 4 nights its +10,000(children under 5 years its free)')
        engine.runAndWait()'''
        first=j*20000
        first2=j*30000
    elif i=='2':
        print('In Andaman total package for single person trip for 3 days 2 nights is 35,000 for 5 days 4 nights its +23,000(children under 5 years its free)')
        first=j*35000
        first2=j*58000
    elif i=='3':
        print('In maldives total package for single person trip for 3 days 2 nights is 1,00,000 for 5 days 4 nights its +35,000(children under 5 years its free)')
        first=j*100000
        first2=j*135000
    elif i=='4':
        print('In Thailand(pataya) total package for single person trip for 3 days 2 nights is 67,000 for 5 days 4 nights its +25,000(children under 5 years its free)')
        first=j*67000
        first2=j*92000
    elif i=='5':
        print('In Darjeeling total package for single person trip for 3 days 2 nights is 34,000 for 5 days 4 nights its +12,000(children under 5 years its free)')
        first=j*34000
        first2=j*46000
    elif i=='6':
        print('In Sri-lanka total package for single person trip for 3 days 2 nights is 52,000 for 5 days 4 nights its +29,000(children under 5 years its free)')
        first=j*52000
        first2=j*81000
    else:
         print(' Please Enter Correct Option')
    print('')
    
    print('')
    import pyttsx3
    engine=pyttsx3.init()
    engine.say("AIR or TRAIN PACKAGE and other VEHICLE charges will be discussed with you and informed finally once after you book \nThe cost will be exactly added up to your final cost that you'll receive below")
    engine.runAndWait()
    #print("AIR/TRAIN PACKAGE and other VEHICLE charges will be discussed with you and informed finally once after you book .The cost will be exactly added up to your final cost that you'll receive below")
    print('')
    
    print('Enter your card information-')
    print("")
    k=input('Enter card holders name: ')
    while True:
        L=input("Enter card no. :")
        if len(L)==12:
            break
        else:
            import pyttsx3
            engine=pyttsx3.init()
            engine.say('Please Enter 12 digit card number')
            engine.runAndWait()
           
            continue
    print('')
    
    print('THE TOTAL COST FOR 3 DAYS 2 NIGHTS IS',first,'FOR 5 DAYS 4 NIGHTS IS',first2)
    
    print("")
    p=input('Enter the number of days that you want to go(3 or 5) : ')
    
    print("")
    if p=='3':
        t=first
    elif p=='5':
        t=first2
    
    while True:
        o=input('Do you want to make payment(yes/no)?').lower()
        if o=='yes':
            
            print(j,'persons are going for',p,'days from',r,'for a total cost of',t)
            print('')
            import pyttsx3
            engine=pyttsx3.init()
            engine.say('Your booking have been successfully completed (EXCLUSIVE OF AIR/TRAIN and other vehicle package )THANK YOU!')
            engine.runAndWait()           
            print('Your booking have been successfully completed (EXCLUSIVE OF AIR/TRAIN and other vehicle package )THANK YOU!')
            engine.say('Final booking and payment shall be done once discussed.\nA call from the travels will be made soon.')
            engine.runAndWait()
            print('Final booking and payment shall be done once discussed.A call from the travels will be made soon.')
            
            
            break
        else:
            engine=pyttsx3.init()
            engine.say('ThankS for visiting our website.\nTRAVEL!!Before you run out of life.')
            engine.runAndWait()
            print('ThankS for visiting our website. \nTRAVEL!!Before you run out of life.')
            break
elif h=='2':
    import pyttsx3
    engine=pyttsx3.init()
    engine.say('I hope you found this website helpful.\n If you want to give your feedback or want to ask any Quiry,Please contact us:\n MOBILE NUMBER:9840657200 \n EMAIL:amalpha90@gmail.com \n We will try our best in contacting with you as soon as possible.')

    engine.runAndWait()
    print('I hope you found this website helpful.\n If you want to give your feedback or want to ask any Quiry,Please contact us:\n MOBILE NUMBER:9840657200 \n EMAIL:amalpha90@gmail.com \n We will try our best in contacting with you as soon as possible.')
    
   
