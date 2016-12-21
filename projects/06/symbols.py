#! /usr/bin/env python3

# Create symbol table for hack assembly files

from sys import argv
import assemblerns

def initialisetable():
	symbols = {'SP':'0', 'LCL':'1', 'ARG':'2', 'THIS':'3', 'THAT':'4', 'SCREEN':'16384', 'KBD':'24576'}
	for i in range(0, 16):
		symbols['R' + str(i)] = str(i)
	return(symbols)

def is_symbol(s):
	try:
		int(s)
		return False
	except ValueError:
		return True

#scans through looking for 
def firstpass(symboltable, commandlist):
	count = 0
	for command in commandlist:
		if '=' in command or ';' in command or command.startswith('@'):
			count += 1
		else:
			symboltable[command.strip('()')] = str(count)
	return(symboltable)

# Scans through looking for value symbols	
def secondpass(symboltable, commandlist):
	ramaddress = 16
	for i in range(len(commandlist)):
		command = commandlist[i]
		if command.startswith('@') and is_symbol(command[1:]):
			try:
				commandlist[i] = '@' + symboltable[command[1:]]
			except KeyError:
				symboltable[command[1:]] = str(ramaddress)
				ramaddress += 1
				commandlist[i] = '@' + symboltable[command[1:]]
	return(symboltable)
				

if __name__ == "__main__":
    # execute only if run as a script
	#sys.argv = ["symbols.py", "max/Max.asm"]
	script, filename = argv
	commandlist = assemblerns.removecomments(assemblerns.openhack(filename))
	symboltable = secondpass(firstpass(initialisetable(), commandlist), commandlist)
	assemblerns.writehackfile(assemblerns.readcommands(commandlist), filename)
