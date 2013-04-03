#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FrenchWords. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Verbs, irregular ones have the variations in a dict. 
verbs = {
    "have" : {
        "i" : "j'ai",
        "you" : "tu as",
        "he" : "il a",
        "she" : "elle a",
        "we" : "nous avons", 
        "you(p)" : "vous avez",
        "they(m)" : "ils ont",
        "they(f)" : "elles ont",
    },
    "be" : {
        "i" : "je suis",
        "you" : "tu es",
        "he" : "il est",
        "she" : "elle est",
        "we" : "nous sommes", 
        "you(p)" : "vous etes",
        "they(m)" : "ils sont",
        "they(f)" : "elles sont",
    },
    "go" : {
        "i" : "je vais",
        "you" : "tu vais",
        "he" : "il va",
        "she" : "elle va",
        "we" : "nous allons", 
        "you(p)" : "vous allez",
        "they(m)" : "ils vont",
        "they(f)" : "elle vont",
    },
    # Group 1
    "like" : "aimer",
    "work" : "travailler",
    "eat" : "manager",
    "draw" : "dessiner",
    "bring" : "apporter",
    "sing" : "chanter",
    "compose" : "composer",
    "create" : "creer",
    "scream" : "crier",
    "give" : "donner",
    "study" : "etudier",
    "freeze" : "geler",
    "scratch" : "frotter",
    "play" : "jouer",
    "pardon" : "pardonner",
    "speak" : "parler",
    "share" : "partager",
    "jump" : "sauter",
    "carry" : "transporter",
	# Group 2
    "hate" : "hair",
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Regular verb roles. 
verb1Role = {
    "i" : ( "Je", "e", ),
    "you" : ( "tu", "es", ),
    "he" : ( "il", "e", ),
    "she" : ( "elle", "e", ),
    "we" : ( "nous", "ons", ), 
    "you(p)" : ( "vous", "ez", ),
    "they(m)" : ( "ils", "est", ),
    "they(f)" : ( "elles", "est", ),
}
# Regular verb roles. 
verb2Role = {
    "i" : ( "Je", "is", ),
    "you" : ( "tu", "is", ),
    "he" : ( "il", "it", ),
    "she" : ( "elle", "it", ),
    "we" : ( "nous", "essons", ), 
    "you(p)" : ( "vous", "essez", ),
    "they(m)" : ( "ils", "essent", ),
    "they(f)" : ( "elles", "essent", ),
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Some French words with gender. 
items = {
    "table" : ( "table", "une" ),
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a irregular sentence. 
def getIrregularVerb( role, verb, thing ):
    return "%s %s" % ( verbs[ verb.lower() ][ role.lower() ], thing )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a regular sentence.
def getRegularVerb( role, verb, thing ):
    verb = verbs[ verb ]
    baseWord = verb[ : -2 ]
    ending = verb[ -2 : ]
    if ending == "er":
        verbRole = verb1Role
    elif ending == "ir":
        verbRole = verb2Role
    else:
        raise Exception( "Bad verb '%s'. No case for it." % ( verb, ) )
    start, ending = verbRole[ role ]
    return "%s %s%s %s" % ( start, baseWord, ending, thing, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simpler input.
def input( output ):
    return raw_input( output ).strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build a sentence. 
def getSentence( role, verb, thing ):
    # Add checks.
    try:
        french = getIrregularVerb( role, verb, thing )
    except:
        french = getRegularVerb( role, verb, thing )
    english = "%s %s %s" % ( role.lower(), verb.lower(), thing )
    return french.lower().strip(), english.lower().strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Helper to pick a random key. 
def randomKey():
    index = randrange( len( verb1Role ) )
    for i, key in enumerate( verb1Role ):
        if i == index:
            return key
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pick a bunch even distibution of verbs then. 
def testVerbs( tests = 3, trys = 3 ):
    totalAttempts = 0
    # Make a list of all of the keys.
    keys = verbs.keys() 
    # Append the list until we have more items that the number of test.
    keysList = keys
    while len( keysList ) < tests:
        keysList += keys
    shuffle( keysList )
    randomKeys = [ x for i, x in enumerate( keysList ) if i < tests ]
    for key in randomKeys:
        answer = False
        theseTrys = trys
        actionKey = randomKey()
        french, english = getSentence( actionKey, key, "" )
        print "What is the french for '%s'?" % ( english, )
        while theseTrys > 0 and answer is False:
            totalAttempts += 1
            answerWord = input( "Answer> " )
            if answerWord == french:
                answer = True
                print "Well done!"
            else:
                theseTrys -= 1
                print "Incorrect."
                if theseTrys > 0:
                    print "Please try again."
        print "The French for '%s' is '%s'." % ( english, french, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def frenchWordsTestRun():
    getSentence( "she", "be", "blah" )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    print getRegularVerb( "she", "hate", "you" )
