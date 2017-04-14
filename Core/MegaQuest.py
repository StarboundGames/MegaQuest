import time
print "Unknown: Good Morning... OH where are my manners."
name = raw_input("Jeffery: My name is Jeffery, what is your name?")
print "Jeffery: Ah a pleasure to meet you %s." % (name) 
gender = raw_input("Jeffery: How should I adress you?")
print "Jeffery: Ok I will adress you as %s." % (gender)
job = raw_input("Jeffery: I'm a Blacksmith, what are you?")
print "Jeffery: Oh so you're a %s. That sounds like a interesting perfesion." % (job)
print "Jeffery: I heard you were on a quest to get to the King's Castle in the East."
print "Jeffery: I can help you."
print "5 months later"
print "Jeffery: Wow, we made it, we actually made it %s!" % (gender)
print "Jeffery: Here lets get some rest in the INN up the road."
tip = raw_input("You go to the INN and order a pint... the service was bad, how much do you tip?")
print "You leave a tip of %s" % (tip)
print "You get some sleep."
print "It is now morning"
question = raw_input("Jeffery: Good Morning! Are you ready to set forth to the Kings Thone Room?")
print "Jeffery: What? Sorry I didn't hear you but whatever lets get a move on."
print "You head to the Kings Throne Room"
print "2 Guards stop you"
print "Guard 1: HALT! Who goes there?"
print "Jeffery: We wish to see the King."
q2 = raw_input("Guard 2: Who doesn't. Why do you wish to see the King?")
print "Jeffery: I am Jeffery and this is %s." % (name)
print "Guard 1: Fine you may see the King now."
print "You enter the Throne Room"
print "King: What is the meaning of this!"
print "Jeffery: We are here to complete our quest."
quest = raw_input("King: What is this quest you speak of?")
print "You: %s" % (quest)
print "King: That sounds stupid. GUARDS! ARREST THESE FOOLS!"
print "Jeffery: WAIT WHAT! NO PLEASE!"
print "King: You will waste no more of my time."
print "You and Jeffery are thrown into the castles dungeon"
print ""
print "			End Of Prologue				"
time.sleep(3)
print "Chapter 1 | The Escape From Death"
time.sleep(3)
print "Jeffery: %s are you ok, did they hurt you." % (gender) 
print "You: I'm fine."
print "Jeffery: Thank the Gods... What are we gonna do?"
print "You: The only thing we can do... escape."
print "Unknown: HeHe... Is that an escape plan I hear."
print "Jeffery: NO!(Lie)"
print "Unknown: HeHe, theres no use in lying. I've been here longer than anyone else I know."
print "Jeffery: You sound like a pretty bad person."
print "Unknown: HeHe, think what you wish."
print "Jeffery: I don't like that guy."
print"Unknown: Well if you two really want to escape I can help."
friend1 = raw_input("Unknown: But if I'm to join you I need a name.   Care to give me one?")
print "You: We will call you %s." % (friend1)
print "%s: Hmm %s, %s... That could work." % (friend1, friend1, friend1)
print "Jeffery: WAIT ARE YOU REALLY GOING TO LET THIS GUY HELP US!"
print "You: Yes I do plan to let him join us."
print "Jeffery: Fine... I don't trust him though."
print "The three of you devise a plan to break out of jail"
time.sleep(2)
print "Guard 1: (whistling)"
print "%s: NOW!" % (friend1)
print "Jeffery chokes out the guard"
print "Taking the keys, Jeffery unlocks his cell and yours, then unlocks %s's cell" % (friend1)
print "Following the plan the three of you sneak your way around the jail until you finally get to the exit"
print "A guard sees Jeffery and tackles him, and slits Jefferys throat"
print "You try to hold back the tears and the rage and finish your escape"
print "You escape"
print ""
print "						End Of Chapter 1			"
time.sleep(3)
print ""
print "Chapter 2 | Friend or Foe"
from datetime import datetime
now = datetime.now()
print "You are in a forest it's currently %s:%s" % (now.hour, now.minute)
print "You follow a trail until you come across a sign. It says that there is a town up ahead"
def askQ():
	answer = raw_input ('Do you go into town?: ')
	if answer == "Yes":
		print ('You head into town')
	elif answer == "No":
		print ('You don\'t head in and after a while you are killed by a pack of Dire Wolfs\(Please Restart Game\)')
	else:
		print('You have not given a proper response')
		askQ()
		
askQ()
print "After entering town you are greeted by the local sales person"
print "Sales Person: Why welcome to our town! May I intrest you in some potions?"
print "You decline the offer and head to the INN"
time.sleep(1)
print "Keeping to yourself you head up to the bar to grab a drink"
print "You get a room and go to sleep"
time.sleep(2)
print "You are awoken by someone knocking on your door"
print "%s: Come on old pal... you gonna let me in?" % (friend1)
print "You: %s! Is that you?" % (friend1)
print "%s enters your room" % (friend1)
print "%s: HeHe... It's been to long." % (friend1)
print "You: It's been a week."
print "%s: Yes yes, a long time, a week samething." % (friend1)
print "You two talk for a while."
time.sleep(2)
print "%s leaves, and you go back to sleep" % (friend1)
time.sleep(2)
print "You wake up"
print "You head into the main part of town"
q1 = raw_input("Homeless: P-please can you spare some change? ")
print "You give him %s" % (q1)
def askQ():
	answer = raw_input ('You see a shop. Do you go in?: ')
	if answer == "Yes":
		print ('You enter and find many useful things, you have enough money so you buy supplies. You even got a discount')
	elif answer == "No":
		print ('You move on')
	else:
		print('You have not given a proper response')
		askQ()
		
askQ()
print "You see child run into the woods. There are wolves in the direction he is running"
print "You go after him"
print "You are able to catch up with him, and you warn him about the wolves"
print "But in the process you alerted the wolves and they lunge at you"
print "You remember your training"
print "Type \"Defend\" to Defend. Type \"Attack\" to Attack" 
def askQ():
	answer = raw_input ('ENGAGE COMBAT: ')
	if answer == "Defend":
		print ('You are able to dodge the attack. You then couter-attack succsesfuly')
	elif answer == "Attack":
		print ('You stab the wolf... You just had your blade out the wolf ran into it...Those stupid Starks')
	else:
		print('You have not given a proper response')
		askQ()
		
askQ()
print "The rest of the wolves are too frightend and run off"
print "Boy: Th-thank ya %s..." % (gender)
print "You: No problem."
print "You get the boy back into town, then get some rest."
print "You are awoken in the middle of the night by the sounds of two people talking"
print "Guard 1: Oye did ya hear, King Williams bastard son helped two people escape the castles dungeon."
print "Guard 2: Doesn't that mean we can kill his sorry arse?"
print "Guard 1: Sure as hell does!"
print "Commander: Would you two shut it. Remember we are on a mission given directly from his grace."
print "Guard 2: Oh sorry sir."
print "Commander: Our scouts said our... \"targets\" came here."
print "Commander:...Kill everyone."
print "Both: Yes sir."
print "You realize you must escape"
def askQ():
	answer = raw_input ('If you leave everyone will die, but you could warn some, at least its saving some. "Leave" or "Save": ')
	if answer == "Leave":
		print ('You couldn\'t have saved anyone anyway')
	elif answer == "Save":
		print ('You try to wake some people but you made to much noise and alerted the guards...They killed you \(Please Restart Game\)')
	else:
		print('You have not given a proper response')
		askQ()
		
askQ()
print "You ran"
print "Far... far away"
time.sleep(4)
print ""
print "				END OF CHAPTER"
print ""
print "	Chapter 3 | The Not So Grand Escape"
time.sleep(3)
print "You see the sun shinning in through the trees"
print "It's morning"
print "You ran all night and are barely standing as is"
print "You keep moving"
