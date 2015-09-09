#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PathWalker. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from os import walk
from os.path import join
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# A helper to easily work with walking a folder structure
class PathWalker():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Pass in an operation name and max size of the progress bar.
    def __init__( self, root ):
        self.root = root
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Write out all the structure
    def printAll( self ):
        for path, dirs, files in walk( self.root ):
            print(path)
            print(dirs)
            print(files)
            print("----")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # All files with full paths.
    def yieldFolders( self, reject = None ):
        for path, dirs, files in walk( self.root ):
            for dir in dirs:
                if reject is None or not reject( path, dir ):
                    yield join( path, dir )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # All files with full paths.
    def yieldFiles( self, reject = None, format = None):
        for path, dirs, files in walk( self.root ):
            for file in files:
                if reject is None or not reject( path, file ):
                    if format is None:
                        yield join( path, file )
                    else:
                        yield format( path, file )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # All files with full paths.
    def getDict( self, reject = None ):
        structure = {}
        for path, dirs, files in walk( self.root ):
            if reject is None or not reject( path ):
                fileList = []
                for file in files:
                    if reject is None or not reject( path, file ):
                        fileList.append( file )
                if fileList != []:
                    structure[ path ] = fileList
        return structure
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Helepr function to identify hidden  files.
    def rejectHidden( self, path, item = None ):
        hiddenFolder = "\." in path
        hiddenFile = item[ 0 ] == "." if item is not None else False
        return hiddenFolder or hiddenFile

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def pathWalkerTestRun():
    print("Starting walker.")
    walker = PathWalker( "D:\\junk" )
    print(walker.getDict())
    print("nOperation done!")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
    pathWalkerTestRun()
