from spy_details import spy_age, spy_name, spy_rating

STATUS_MESSAGE = ["hey there i am using spychat ","can't talk spychat only","available"]

friends_name = ["Tabish"]
friends_age = [25]
friends_rating = [5.5]
friends_is_online = [True]

def start_chat(spy_name,spy_age, spy_rating):
    current_status_message = None
    show_menu = True
    while show_menu:
        menu_choice = input("What do you want to do? \n 1. Add a status update \n 2. Add a friend\n 3. Send message\n 4. exit")
        if menu_choice == 1:
           print  "Time to update your status"
           add_status(current_status_message)
        elif menu_choice==2:
            add_friend()
        elif menu_choice == 4:
           show_menu = False
        else:
            print "enter right menu option"

def add_status (current_status_message):
    if current_status_message != None:
      print "Your current status message is " + current_status_message + "\n"
    else:
      print 'You don\'t have any status message currently \n'

    query = raw_input ("do you want to select from the older status (y/n)? ")


    if query=="y"or query=="Y":
        print "select from your old status"
        number=1
        for new_status in STATUS_MESSAGE:
            print str(number) + ". " + new_status
            number+=1

        user_selection= input ("choose any no")
        if len (STATUS_MESSAGE)>=user_selection:
            new_user_selection=user_selection-1
            current_status=STATUS_MESSAGE[new_user_selection]
            print current_status + " " + "is our current status"
        else:
            print "your entry is invalid"
    elif query=="n" or query =="N":
        new_status=raw_input("please enter the new status ")
        if len (new_status)>0:
            STATUS_MESSAGE.append(new_status)
            print new_status + " " +"is our current status"

        else:
            print "please enter something"
    else:
        print " please enter y or n"

def add_friend():
    new_name = raw_input("Please add your friend's name:")
    new_salutation = raw_input("Are they Mr. or Ms.?: ")
    new_name = new_salutation + " " + new_name
    new_age = input("Age?")
    new_rating = input("Spy rating?")
    if len(new_name)>0 and 12< new_age<50 and new_rating>=spy_rating:
        friends_name.append(new_name)
        friends_age.append(new_age)
        friends_rating.append(new_rating)
        friends_is_online.append(True)
    else:
        print 'Cannot add this friend as a SPY'

print 'Hello'
print 'let\'s get started'

spy_ques =raw_input('are you existing user? Y/N ')

if spy_ques == 'Y'or spy_ques== 'y':
    print spy_name
    start_chat(spy_name,spy_age,spy_rating)

else:
    spy_name = raw_input('what is your name? ')

    if len(spy_name)>0:
        print 'Hi,welcome '+ spy_name +' nice to meet you'
        spy_salutation =raw_input('what should we call you (mr. or ms.)?')
        spy_name = spy_salutation + ' ' + spy_name
        print 'Alright ' + spy_name + ' i\'d like to know more about you'
        spy_age = input( 'what is your age? ' )
        if spy_age>12 and spy_age<50:
            spy_rating = input ('what is your rating? ')
            if spy_rating >4.5:
                print 'very good spy'
            elif spy_rating >3.5 and spy_rating<=4.5:
                print 'good spy'
            elif spy_rating >2.5 and spy_rating <=3.5:
                print 'average spy'
            else:
                print 'bad spy'
            print 'authentication complete. welcome ' + spy_name + ' age: ' + str(spy_age) + ' and rating : ' + str(spy_rating) + " Proud to have you onboard"
            start_chat(spy_name,spy_age,spy_rating)
        else:
            print 'youre age is not eligible to be a spy'
    else:
        print 'please enter your name'