#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# FrenchWords. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from random import shuffle, randrange
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Some Verbs.
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
    "like" : "aimer",
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
verbRole = {
    "i" : ( "Je", "e", ),
    "you" : ( "tu", "es", ),
    "he" : ( "il", "e", ),
    "she" : ( "elle", "e", ),
    "we" : ( "nous", "ons", ), 
    "you(p)" : ( "vous", "ez", ),
    "they(m)" : ( "ils", "est", ),
    "they(f)" : ( "elles", "est", ),
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
items = {
    "table" : ( "table", "une" ),
}
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
def getIrregularVerb( role, verb, thing ):
    return "%s %s" % ( verbs[ verb.lower() ][ role.lower() ], thing )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
def getRegularVerb( role, verb, thing ):
    baseWord = verbs[ verb ][ : -2 ]
    start, ending = verbRole[ role ]
    return "%s %s%s %s" % ( start, baseWord, ending, thing, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Simpler input.
def input( output ):
    return raw_input( output ).strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
def getSentence( role, verb, thing ):
    # Add checks.
    try:
        french = getIrregularVerb( role, verb, thing )
    except:
        french = getRegularVerb( role, verb, thing )
    english = "%s %s %s" % ( role.lower(), verb.lower(), thing )
    return french.lower().strip(), english.lower().strip()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
def randomKey():
    index = randrange( len( verbRole ) )
    for i, key in enumerate( verbRole ):
        if i == index:
            return key
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
def basicVerbs( tests = 3, trys = 3 ):
    totalAttempts = 0
    keys = []
    # Get a random selection of the keys.
    for key in verbs:
        for i in range( tests ):
            keys.append( key )
    shuffle( keys )
    keys = [ x for i, x in enumerate( keys ) if i < tests ]
    for key in keys:
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
    printSentence( "she", "be", "blah" )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main test.
if __name__ == "__main__":
    basicVerbs( 5 )
