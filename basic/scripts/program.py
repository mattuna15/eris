# *****************************************************************************
# *****************************************************************************
#
#		Name:		program.py
#		Purpose:	Convert ASCII to tokenised BASIC
#		Created:	3rd March 2020
#		Author:		Paul Robson (paul@robsons.org.uk)
#
# *****************************************************************************
# *****************************************************************************

import os,re
from convert import *

# *****************************************************************************
#
#							Basic Program class
#
# *****************************************************************************

class Program(object):
	def __init__(self):
		self.tokeniser = Tokeniser()
		self.code = []
		self.nextLine = 1000
		self.lastLine = 0
	#
	#		Import a file
	#
	def append(self,srcFile):
		for s in open(srcFile).readlines():
			s = s.strip()
			if not s.startswith(";") and s != "":
				self.addLine(s)
	#
	#		Append a line
	#
	def addLine(self,s):
		lineNumber = self.nextLine 											# default line #
		m = re.match("^(\\d+)\\s+(.*)$",s)									# do we have a line number.
		if m is not None:
			lineNumber = int(m.group(1))									# get it
			assert lineNumber > self.lastLine,"Lines out of sequence"		# check order.
			s = m.group(2).strip()											# line body.
		assert lineNumber > 0 and lineNumber < 32768,"Bad line number" 		# must be 1-32767
		self.lastLine = lineNumber 											# update state
		self.nextLine = lineNumber+10
		#
		code = self.tokeniser.tokenise(s)									# convert line to code.
		code.append(0)														# add end of line marker.
		code.insert(0,lineNumber)											# add line number
		code.insert(0,len(code)+1)											# add offset.
		assert code[0] == len(code)										
		self.code += code
	#
	#		Output source with test label
	#
	def write(self,tgtFile,label = None,forceAddress = None):
		h = open(tgtFile,"w")
		h.write(";\n;\tAutomatically generated\n;\n")
		c = ",".join(["${0:04x}".format(c) for c in self.code])
		if forceAddress is not None:
			h.write("\torg\t\t${0:04x}\n".format(forceAddress))
		if label is not None:
			h.write("."+label+"\n")
		h.write("\tword\t{0}\n".format(c))
		h.write("\tword\t$0000\n")
		h.write(".EndBasicProgram\n")
		h.close()

		h = open("basiccode.prg","wb")
		h.write(bytes([0]))
		h.write(bytes([0x42]))
		for i in self.code:
			h.write(bytes([i & 0xFF]))
			h.write(bytes([i >> 8]))
		h.write(bytes([0]))
		h.write(bytes([0]))
		h.close()

if __name__ == "__main__":	
	program = Program()
	program.append("test.bas")		
	program.write(".."+os.sep+"generated"+os.sep+"test_program.inc","basicProgram",None)