#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OutputProgress. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
units = (
	"zero",
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
tens = (
	"",
	"",
	"vingt",
	"trente",
	"quarante",
	"cinqanyte",
	"sixante",
	( "soixante-dix", "soixante-" )
	"quatre-vingts",
	( "quatre-vingts-dix", "quatre-vingts-" ),
)
hundred = "cent"
thousand = "mile"
million = "million"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Digit to word.
def getWord( number):
	strnum = str( number )[ :: -1 ]
	word = ""
	usedAnd = False
	for i in range( len( strnum ) - 1, -1, -1 ):
		n = int( strnum[ i ] )
		if n == 0:
			continue
		if i == 3:
			word += " %s %s" % ( units[ n ], thousand )
		elif i == 2:
			word += " %s %s" % ( units[ n ], hundred )
		elif i == 1:
			if len( word ) > 0 and not usedAnd: 
				word += " et"
				usedAnd = True 
			if n > 1:
				word += " %s" % ( tens[ n ], )
			else:

				n2 = int( strnum[ :2 ][ :: -1 ] )
				print "n2", n2
				word += " %s" % ( units[ n2 ], )
				break
		else:
			if len( strnum ) > 2 and not usedAnd: 
				word += " and"
				usedAnd = True 
			word += " %s" % ( units[ n ], )
	return word
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
	for i in xrange( 1, 1001 ): 
		print getWord( i )

