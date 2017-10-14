from spy_details import spy_age, spy_name, spy_rating




print 'Hello'
print 'let\'s get started'

spy_ques =raw_input('are you existing user? Y/N ')

if spy_ques == 'Y'or spy_ques== 'y':
    print spy_name
else:
    spy_name = raw_input('what is your name? ')

    if len(spy_name)>0:
        print 'welcome '+ spy_name +' nice to meet you'
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

        else:
            print 'youre age is not eligible to be a spy'

    else:
        print 'please enter your name'