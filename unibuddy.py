'''
Beginning programming: personalised chat bot (UniBuddy)

    - Create a simple chat bot. This could be for a specific purpose for example, banking help bot.
    - Personalised greetings system: a program that gathers a user's name, favourite
      colour, age, then offers a personalised greeting and comment based on the input.
    - Shopping budget tool: an application that assists users in managing their
      shopping budget, calculating remaining funds, and warning if they've overspent.

    Case study story:
    Imagine the first day of university for a freshman named Alex. 
    Alex is excited but also overwhelmed by the vast campus, numerous courses,
    and the sea of new faces. To aid new students like Alex, the university's IT 
    department has developed a personalised chatbot. This chatbot, named 
    "UniBuddy", is designed to make the transition smoother for freshmen. Upon
    accessing the chatbot, Alex is prompted to enter their name, favourite colour, and
    age. Based on this input, UniBuddy offers a personalised greeting. For instance, if 
    Alex's favourite colour is blue, UniBuddy might suggest joing the university's "Blue 
    Art Club". If Alex is 18, the chatbot might provide information about 
    freshman-specific events. The chatbot also offers a feature where Alex can input
    specific queries, like "Where is the library?" or "How do I joing the debate club?" and
    UniBuddy responds with relevant information, all while adhering to a friendly tone,
    using string transformation metods to ensure the responses feel personalised and engaging
'''
#initialise message for first time start

print('''
Welcome to UniBuddy! Your personalised chat bot dedicated to making 
your freshman experience as care free as possible!!
''')

user_name = input("Who do I have the pleasure of speaking to? (Please enter your name): ").capitalize()
user_age = int(input("How old are you? "))
fav_colour = input("What is your favourite colour? ").capitalize()

print(f'''
Nice to meet you {user_name}! You mentioned that your favourite colour is {fav_colour}.
I have a few suggestions based on your choice!
''')

if fav_colour == 'Red':
    print('''If you like the colour RED, I have the following for you! Check out: 
1. Our vampire themed society
2. Our red wine club.
3. Our apple picking club (dependent on the season)''')

elif fav_colour == 'Blue':
    print('''If you like the colour BLUE, I have the following for you! Check out:
1. Our rhythm and blues club.
2. Our deep sea exploration club.
3. Our bird watching club.
    ''')

elif fav_colour == 'Yellow':
    print('''If you like the colour YELLOW, I have the following for you! Check out:
1. Our suntan society.
2. Our hiking club.
3. Our yellow themed netball club.
    ''')

elif fav_colour == 'Orange':
    print('''If you like the colour ORANGE, I have the following for you! Check out:
1. Our sunset photography club.
2. Our camping club (you will learn key survival techniques such as fire starting).
3. Our Halloween society.
    ''')

elif fav_colour == 'Green':
    print('''If you like the colour GREEN, I have the following for you! Check out:
1. Our gardening club.
2. Our vegan society.
3. Our "Save the planet" club.
    ''')

elif fav_colour == 'Pink':
    print('''If you like the colour PINK, I have the following for you! Check out:
1. Our romantic novels discussion club.
2. Our pink themed art club.
3. Our baking club.
    ''')

elif fav_colour == 'Purple':
    print('''If you like the colour PURPLE, I have the following for you! Check out:
1. Our purple themed football club
2. Our fantasy club
3. Our magic club
    ''')
    
else: 
    print(f'''Hmm... I am sorry, but we do not have any clubs related to that colour. 
Why dont you create your own club for all the students that also love {fav_colour}?!''')
    
if user_age <=22:
    print('''Here are some freshman specific events:
1.  MEET NEW FRIENDS: Making new friends in a strange environment can be pretty daunting, 
so why not check out the dates for our meet-ups and make some new friends?
    
2.  FRESHERS PARTY: Book your tickets now!! We have a different genre of music in every room (Pop, Hip-hop, R&B, Afrobeats, Jazz, Heavy Metal, Indie).

3.  FRESHERS FAIR: Come to our freshers fair and enjoy our live entertainment and collect plent of discounts and freebies to help kickstart your university experience!
''')

else: 
    print('''Here are some event suggestions that might be to your liking: 
1. CHANGING CAREERS PANEL DISCUSSION: Changing careers can be a difficult process. We have a number of alumni 
who were in the same boat as you speaking about their experiences. 
Get some questions answered and feel certain that you made the right choice for you! 
    
2. SIP AND PAINT: Book your tickets for our sip and paint events where you can enjoy a number our 
delicious cocktails and mocktails whilst embracing your creative side!
    
3. POETRY READING: Want to express yourself or simply enjoy listening to poetry? Then check out the dates for our poetry reading events!!

''')
#FAQs

while True: 
    question = input("Is there anything you would like to ask me? (Type Q to quit)")
    
    if question == "How is your day?":
        print(f"I am learning all about my new friend {user_name}, so it is a great day!")
    
    elif question == "I have gotten my timetable. How do I find my classes?":
        print("If you check out our university home page, you will find a downloadable map of our campus.")
    
    elif question == "How do I join the magic club?":
        print('''To join the magic club or any of our clubs or societies, go to our university website and click on the
"Clubs and Societies" tab. There you will find a list of clubs and societies. Click on the one you are interested 
in and you will be given a descrption and will be prompted to sign up. Have fun!''')
    
    elif question == "Q":
        break
    
    else:
        print("Hmm... I don't understand that question. Please contact this email: help@university.co.uk to get a response.")
    
#shopping budget
budget = float(input("Please enter your monthly budget: "))
total = float(0)
count = 0

while True:
    spent = float(input ("Please enter how much your purchase cost: "))
    
    count += 1
    total += spent
    overspent = total - budget
    
    if total == budget:
        print("You have reached your budget")
        print(f" You have made {count} transactions and have spent £{total:.2f}.")
        break
    
    elif total > budget:
        print("You have gone over your budget. Please stop spending money for the rest of the month")
        print(f"You have made {count} transactions and have spent £{total:.2f}. That is £{overspent:.2f} overbudget.")
        break 