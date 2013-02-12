#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FrenchNumbers. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle
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
    # Special case for numbers under 20 and those which are using the +10 rule
    # eg. 70 = 60 + 10, 90 = 4 * 20 + 10
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
# Simpler input.
def input( output ):
    return raw_input( output ).strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a number.
def quizNumber( number, trys = 3 ):
    word = getWord( number )
    print "What number is '%s'" % ( word, )
    answer = False
    totalAttempts = 0
    while trys > 0 and answer is False:
        totalAttempts += 1
        answerWord = input( "Answer> " )
        try: 
            answerNumber = int( answerWord )
            if answerNumber == number:
                answer = True
                print "Well done!"
            else:
                trys -= 1
                print "Incorrect."
                if trys > 0:
                    print "Please try again."
        except:
            print "Please entre a number."
    print "'%s' is the number %d" % ( word, number, )
    return answer, totalAttempts
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Quiz a range .
def quizNumberRange( numberRange, trys = 3, shuffleThem = True ):
    if shuffleThem:
        shuffle( numberRange )
    items = len( numberRange )
    print "%s items in test" % ( items, )
    correct = 0
    totalAttempts = 0
    for i, number in enumerate( numberRange ):
        print "%s) " % ( i + 1, ),
        answer, attempts = quizNumber( number, trys )
        totalAttempts += attempts
        if answer:
            correct += 1
    print "Score: %d/%d, total attempts: %d" % ( correct, items, totalAttempts, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A bunch of quiz functions
def quizLowNumbers( trys = 3 ):
    quizNumberRange( range( 20 ), trys )
def quizTensNumbers( trys = 3 ):
    quizNumberRange( range( 20 ), trys )
def quizRandom( maxNumber, total, trys = 3 ):
    nums = range( maxNumber + 1 )
    shuffle( nums )
    nums = [ x for i, x in enumerate( nums ) if i < total ]
    quizNumberRange( nums, trys, shuffleThem = False )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    for i in xrange( 101 ): 
        print str( i ).rjust( 4 ), "=",  getWord( i )
    quizRandom( 5 )
