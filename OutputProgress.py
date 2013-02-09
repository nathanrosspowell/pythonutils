#!/usr/bin/python
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# OutputProgress. Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from sys import stdout
from time import sleep
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Give a class to manage printing out a ASCII progress bar.
class ProgressBar():
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Pass in an operation name and max size of the progress bar.
	def __init__( self, barName, barSize ):
		self.barName = barName
		self.barSize = barSize - 2
		# Ascii icons
		self.segment = {
			'fin' : '=',
			'todo' : ' ',
			'mark' : "|"
		}
		# Build the information bar
		self.infoStart = "%s0%% %s" % ( 
			self.segment[ 'mark' ], 
			self.barName,
		)
		self.infoEnd = "100%%%s" % ( self.segment[ 'mark' ], )
		gap = self.barSize - len( self.infoStart + self.infoEnd ) + 2
		self.info = "%s%s%s" % (
			self.infoStart,
			gap * self.segment[ 'todo' ],
			self.infoEnd,
		)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Print the information bar
	def printInfo( self ):
		print self.info
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Write out using stdout.write so the buffer overwites itself
	def progress( self, ratio ):
		ratio = max( min( ratio, 1.0 ), 0.0)
		# Get the two halfs of the bar
		complete = int( self.barSize * ratio ) 
		uncomplete = self.barSize - complete
		status = "%.2f%%" % ( ratio * 100.0, )
		completeBar = self.segment[ 'fin' ] * complete
		statusLen = len( status )
		# Put the current percentage in the biggest space.
		if ratio < 0.5:
			completeBar = "%s%s%s" % (
				completeBar[ :-1 ] if complete > 1 else "",
				self.segment[ 'mark' ] ,
				self.segment[ 'todo' ],
			)
			completeBar += status
			uncomplete -= statusLen + 1
			if complete < 1:
				uncomplete -= 1 
		elif ratio < 1.0:
			completeBar = "%s%s%s%s" % ( 
				completeBar[ : -( statusLen + 2 ) ],
				status,
				self.segment[ 'fin' ],
				self.segment[ 'mark' ],
			)
		# Build the final output.
		bar = "%s%s%s%s\r" % (
			self.segment[ 'mark' ],
			completeBar, 
			self.segment[ 'todo' ] * uncomplete,
			self.segment[ 'mark' ],
		)
		stdout.write( bar )

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test run.
def outputProgressTestRun():
	print "Starting operation."
	bar = ProgressBar( "Copy stuff", 70 )
	bar.printInfo()
	percentage = 0.0
	while percentage < 1.0:
		percentage += 0.0064
		bar.progress( percentage )
		sleep( 0.01 )
		
	print "\nOperation done!"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Direct run of the file, invoke test.
if __name__ == "__main__":
	outputProgressTestRun()
