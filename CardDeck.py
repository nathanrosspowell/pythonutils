#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CmdColors. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
import os
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def dec2hex( n ):
    """return the hexadecimal string representation of integer n"""
    return "%X" % ( n, )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def hex2dec( s ):
    """return the integer value of a hexadecimal string s"""
    return int( s, 16 )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def setColor( a, b ):
    string = "COLOR %s%s" % ( str( a ), str( b ), )
    print(string)
    os.system( string )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def loopColours():
    for i in range( 16 ):
        for j in range(16):
            a = dec2hex( i )
            b = dec2hex( j )
            setColor( a, b )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def cmdColorsTestRun():
    print( "Starting operation.")
    loopColours()
    # Reset
    setColor( 0, 7 )
    print("\nOperation done!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    cmdColorsTestRun()
