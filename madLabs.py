n = int(input('Which story would you like to play? '))
q= exit
for i in range(0,n):
    print ('Enter 1 for story number 1/n')
    print ('Enter 2 for story number 2/n')
    print ('Enter 3 for story number 3/n')
    print ('Enter Q to quit/n')
choice = int(input('Enter your choice'))

if (choice ==1):
    adj = input('Enter an adjective: ')
    fm= input('Enter a female name: ')
    adj1= input('Enter an adjcetive: ')
    noun= input('Enter a noun: ')
    pod= input('Enter part of a body : ')

    print(f"The last time i went to a sleepover a/an {adj} pillow fight broke out. Out of nowhere {fm} grabbed her \
       {adj1} fluffy{noun} and swinging it at everyone, soon everyone joined in. Suddenly her {noun} hit my \
       {pod} and I passed out.")

if (choice ==2):
    country= input('Enter a foreign country: ')
    adv= input('Enter an adverb: ')
    adj= input('Enter an adjective: ')
    animal= input('Enter an animal: ')
    verb= input('Enter a verb eding with ing: ')
    verb1= input('Enter a verb: ')

    print(f"If you are travelling in {country} an find yourself having to cross a piranha-filled river, here's how to do it {adv}: Piranha are more {adj} during the day so you can cross the river at; night Avoid area with netted {animal} traps- piranha may be {verb} there looking to {verb1} them. ")


if (choice ==3):
    adj= input('Enter an adjective: ')
    adj1= input('Enter an adjective: ')
    bird= input('Enter a type of bird: ')
    room= input('Enter a room in the house: ')
    verb= input('Enter a verb in past tense: ')
    verb1= input('Enter a verb: ')
    rn= input('Enter a name: ')
    liquid= input('Enter a type of liquid: ')
    verb3= input('Enter a verb ending with ing: ')
    pod= input('Enter a part of body: ')
    pn= input('Enter a plural noun: ')
    verb4= input('Enter a verb ending with ing: ')
    noun= input('Enter a noun: ')

    print(f"It was a {adj}, cold December day. I woke up to the smell of {bird} roasting in the {room} downstairs. I {verb} down the stairs to see If I could help {verb1} the dinner. My mom said If {rn} needs fresh carrot. So I carried a tray of glasses full of {liquid} into the {verb3} room. When I got there I couldnt believe my {pod}, there were {pn} {verb4} on the {noun} ")


if (choice ==q):
    exit()

else: 
    print ("invalid")
