#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OutputProgress. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# First 19 numbers by index.
units = (
	"", # zero
	"un",
	"deux",
	"troi",
	"quatre",
	"cinq",
	"six",
	"sept",
	"huit",
	"neuf",
	"dix",
	"onze",
	"douze",
	"treize",
	"quatorze",
	"quinze",
	"seize",
	"dix-sept",
	"dix-huit",
	"dix-neuf",
)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# All of the unique tens by digit index.
tens = (
	"",
	"",
	"vingt",
	"trente",
	"quarante",
	"cinqanyte",
	"soixante",
	( "soixante", True ),
	"quatre vingts",
	( "quatre vingts", True ),
)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Further measures.
hundred = "cent"
thousand = "mile"
#million = "million"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Index names.
ThousandsIndex = 0
HundredsIndex = 1
TensIndex = 2
UnitsIndex = 3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Digit to word. Work for up to four digit numbers
def getWord( number):
	# Special case for '0'.
	if int( number ) is 0:
		return "zero"
	# Get a four digit string.
	strnum = str( number ).zfill( 4 )
	# The string to build.
	word = ""
	# Get the digits for each coloumn.
	digitThousands = int( strnum[ ThousandsIndex ] )
	digitHundreds = int( strnum[ HundredsIndex ] )
	digitTens = int( strnum[ TensIndex ] )
	digitUnits = int( strnum[ UnitsIndex ] )
	# Variables to track the quirks of the number system.
	funnyPlusTenRule = False
	andOne = False
	# Handle thousands.
	if digitThousands > 0:
		wordThousands = "%s %s " % ( units[ digitThousands ], thousand, )
		word += wordThousands
	# Handle hundreds.
	if digitHundreds > 0:
		wordHundreds = "%s %s " % ( units[ digitHundreds ], hundred, )
		word += wordHundreds
	# Handle tens that are outside of the 'teens' range.
	if digitTens > 1:
		funnyPlusTenRule = len( tens[ digitTens ] ) is 2
		if digitUnits is 0 and funnyPlusTenRule:
				wordTens = tens[ digitTens ][ 0 ]
		else:
			andOne = digitTens < 7
			if funnyPlusTenRule:
				wordTens = tens[ digitTens ][ 0 ]
			else:
				wordTens = tens[ digitTens ]
		word += "%s " % ( wordTens, )
	# Special case for numbers under 20 and those which are using the +10 rule, eg. 70 = 60 + 10
	if digitTens is 1 or ( digitTens is not 0 and funnyPlusTenRule ):
		digitTeen = int( "1%d" % ( digitUnits, ) ) 
		teenWord = ""
		if digitUnits is 1 and andOne:
			teenWord = "et "
		teenWord += "%s " % ( units[ digitTeen ], )
		word += teenWord
	else:
		# Normal less than 10 digit.
		unitWord = ""
		if digitUnits is 1 and andOne:
			unitWord = "et "
		unitWord += "%s " % ( units[ digitUnits ], )
		word += unitWord
	# Return the word without any extra whitespaces.
	return word.strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
	for i in xrange( 101 ): 
		print str( i ).rjust( 4 ), "=",  getWord( i )
