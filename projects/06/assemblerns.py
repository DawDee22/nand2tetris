#!/usr/bin/env python3

# Assembler program for hack platform

# Open requested file and produce list containing the text
import htables
from sys import argv

def openhack(filename):
	with open(filename, 'r') as hackfile:
		commands = hackfile.readlines()
	strippedlist = []
	for line in commands:
		strippedlist.append(line.strip())
	print(strippedlist)
	#print(commands)
	commands = [x for x in strippedlist if x]
	return(commands)

# March through commands and parse
def readcommands(commandlist):
	binarycommands = []
	for command in commandlist:
		if determinecommandtype(command) == 'A_command':
			binarycommands.append(Aparser(command))
		elif determinecommandtype(command) == 'C_command':
			binarycommands.append(Cparser(command))
		elif determinecommandtype(command) == 'L_command':
			binarycommands.append(command + ' L')
	print(binarycommands)
	return(binarycommands)

# Determines the type of command
def determinecommandtype(command):
	if '=' in command or ';' in command:
		return('C_command')
	elif command.startswith('@'):
		return('A_command')
	else:
		return('L_command')

# Removes the comments and white space from a command list
def removecomments(commandlist):	
	return(x for x in commandlist if not x.startswith('//'))

#A instruction parser
def Aparser(command):
	number = int(command[1:])
	return('0' + "{0:015b}".format(int(command[1:])))

#C instruction parser
def Cparser(command):
	if '=' in command and ';' in command:
		dest = command[0:command.find('=')]
		comp = command[command.find('=')+1:command.find(';')]
		jump = command[command.find(';')+1:]
	elif '=' in command and not(';' in command):
		dest = command[0:command.find('=')]
		comp = command[command.find('=')+1:]
		jump = 'null'
	elif ';' in command and not('=' in command):
		dest = 'null'
		comp = command[0:command.find(';')]
		jump = command[command.find(';')+1:]
	return(Cbinaryconvert(dest, comp, jump))

# converts c command to 6 bit binary
def Cbinaryconvert(dest, comp, jump):
	destbin = htables.dest[dest]
	compbin = htables.comp[comp]
	jumpbin = htables.jump[jump]
	return('111' + compbin + destbin + jumpbin)

# write new hack file
def writehackfile(binlist, filename):
	newfilename = filename[:-3] + 'hack'
	with open(newfilename, 'w') as f:
		for item in binlist:
  			f.write("%s\n" % item)


if __name__ == "__main__":
    # execute only if run as a script
	script, filename = argv
	commandlist = openhack(filename)
	writehackfile(readcommands(removecomments(commandlist)), filename)
