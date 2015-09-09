#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# _testing. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from os import walk
from os.path import realpath, splitext, split
# local imports
from PathWalker import PathWalker
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A to test all scripts in this folder.
class Tester( PathWalker ):
    seperator = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Pass in a root folder to test
    def __init__( self, root ):
        PathWalker.__init__( self, root )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # All files which are python scripts, excluding "_test" files.
    def yieldScripts( self ):
        def format( path, file ):
            return splitext( file )[ 0 ]
        def reject( path, item ):
            hidden = self.rejectHidden( path, item )
            notPyfile = splitext( item )[ 1 ] != ".py"
            testFile = item[ 0 ] == "_"
            return hidden or notPyfile or testFile
        for item in self.yieldFiles( reject = reject, format = format ):
            yield item
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Run the scriptTestRun() function in each file.
    def runScript( self, script ):
        print(self.seperator)
        print("Running", script)
        s = script
        command = "%s.%sTestRun()" % ( s, s[ 0 ].lower() + s[ 1: ], )
        exec( "import %s;%s" % ( script, command, ) )
        print("%s\n" %( self.seperator, ))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Test all the scripts.
    def runAllScripts( self ):
        for script in self.yieldScripts():
            self.runScript( script )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def doTestRun():
    print("Starting Tests.")
    walker = Tester( split( realpath( __file__ ) )[ 0 ] )
    walker.runAllScripts()
    print("Tests done!")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    doTestRun()
