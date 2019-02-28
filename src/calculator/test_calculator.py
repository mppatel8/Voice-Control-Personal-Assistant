import pyttsx3
from calculator import operations
from speak import speech
engine = pyttsx3.init()
engine.setProperty('rate',100)
engine.setProperty('volume',0.9)

command_file  = open('first_input','r')
strr = command_file.readlines()
stt=strr[0]

print(stt)
input_file = open('second_input','r')

with  open('firstlevel','r') as first_level_command:
	lines  =  first_level_command.readlines()
	for sub in lines:
		print(sub)
		if(str(sub) in str(stt)):
			#engine.say('What you want to solve')
			speech.speak('what you want to solve?')
			sub1 = "add"
			str1 = "I want to add"
			if(sub1 in str1):
				#engine.say('Give two numbers')
				speech.speak('give me numbers')
				a = float(input_file.readline())
				b = float(input_file.readline())
				c = sum(a,b)
				engine.say('Your answer is'+str(c))
			else:
				print('OK')
		else:
			print('bad')

#engine.runAndWait()