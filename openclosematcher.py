#!/usr/bin/python
# -*- coding: latin-1 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# openclosematcher.py Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
from os import walk as os_walk, path as os_path, sep as os_seperator
from re import compile as regex, VERBOSE as re_verbose
from time import strftime as time_format, time as time_stamp
from multiprocessing import Pool as multi_pool, cpu_count as multi_cpu_count
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Globals.
line_format = "--------------------------------------------------------------"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class for regex matching.
class OpenCloseMatcher:
    pattern = """  .*?         # All before the function name, not greedy    
                   %s          # Format in the function name as a string
                   \(          # The opening bracket
                   ( .*? )     # Capture everything, not greedy
                   \)       """# The closing bracket
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def __init__( self, opening, closing ):
        self.opening_pattern = regex( self.pattern % ( opening,), re_verbose )
        self.closing_pattern = regex( self.pattern % ( closing,), re_verbose )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def _get_match( self, pattern, line ):
        match = pattern.match( line )
        try:
            return match.group( 1 ).strip()
        except:
            return None
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def get_opening( self, line ):
        return self._get_match( self.opening_pattern, line )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def get_closing( self, line ):
        return self._get_match( self.closing_pattern, line )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class for checking for nested matches and their equality.
class ParseFileForMatches:
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def __init__( self, file_info, matcher ):
        self.file_info = file_info
        self.matcher = matcher
        self.errors = []
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def store( self, data, match ):
            return dict( data.items() + { "match" : match.strip() }.items() )
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    #
    def run( self ):
        matchStack = []
        for data in self.file_info:
            text = data[ "text" ]
            openMatch = self.matcher.get_opening( text )
            if openMatch:
                matchStack.append( self.store( data, openMatch ) )
            elif len( matchStack ) > 0:
                closeMatch = self.matcher.get_closing( text )
                if closeMatch:
                    popped = matchStack.pop()
                    if closeMatch != popped[ "match" ]:
                        error = ( popped, self.store( data, closeMatch ) )
                        self.errors.append( error )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Create a dictionary of filename, line number and line data.
def make_line_data( f ):
    def s( line ): 
        return line.strip()
    with open( f, 'r' ) as file_stream:
        l = file_stream.readlines()
    e = enumerate
    d = ( { "line" : i+1, "text" : s( t ), "file" : f } for i, t in e( l ) )
    return d
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Walk all the directories to generate all files with the correct extensions.
def get_all_files( directories, ext_list ):
    for directory in directories:
        if os_path.isdir( directory ):
            for dirpath, dir, filenames in os_walk( directory ):
                for file in filenames:
                    path = os_path.abspath( os_path.join( dirpath, file ) )
                    junk, ext = os_path.splitext( path )
                    if ext in ext_list:
                        yield path
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Makes a generator combinations of file and matcher class.
def generate_all_combinations( directories, etx_list, match ):
    files = get_all_files( directories, etx_list )
    matchers = ( OpenCloseMatcher( o, c ) for o, c in match )
    g = ( ( file, matcher ) for file in files for matcher in matchers )
    return g
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The function to distribute in the pools, reports if needed.
def run_match( args ):
    file, matcher = args
    file_info = make_line_data( file )
    parse = ParseFileForMatches( file_info, matcher )
    parse.run()
    if parse.errors != []:
        return parse.errors
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Logging the errors a file as human readable instructions.
def log_errors( errors, do_printing=False ):
    def write_line( log, text ):
        if do_printing:
            print text
        log.write( "%s%s" % ( text, os_seperator ) )
    timestamp = time_format("%Y-%m-%d-%H-%M-%S")
    log_file = "openclosematcher-log-%s.txt" % ( timestamp, )
    with open( log_file, 'w' ) as log:
        for errorlist in errors:
            for opened, closed in errorlist:
                write_line( log, make_error_line( opened, closed ) )
            write_line( log, line_format )
    if do_printing:
        print line_format
    print "Errors logged to", log_file
def make_error_line( opened, closed ):
    format = "Use %s on line %s %s"
    error = ( opened[ "match" ], closed[ "line" ], closed[ "file" ] )
    return format % error
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The main function to call if this file is imported.
def execute( match, directories, etx_list, do_printing=False ):
    if do_printing:
        print line_format
        print "Matching:"
        for m in match:
            print "  %s with %s" % m
        print "In directories:"
        for d in directories:
            print "  %s" % ( d, )
        print "For extensions:"
        for e in etx_list:
            print "  %s" % ( e, )
        print line_format
        print "Checkign all files now..."
    try:
        generator = generate_all_combinations( directories, etx_list, match )
        processes = multi_cpu_count() / 2 # Don't know the best value
        pool = multi_pool( processes )
        results = pool.map( run_match, generator )
        errors = [ x for x in results if not x is None ]
        log_errors( errors, do_printing )
    except:
        raise # Kills all the processes when we do the keyboard interupt.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Run if this file is executed
if __name__ == "__main__":
    # List of tuples of opening and closing tags.
    match = (
        #( "open", "close" ),
        ( "NOMAD_BEGIN_NEW_EVENT_MAP", "NOMAD_END_NEW_EVENT_MAP" ),
    )
    # List of all directories to check inside of (recursively).
    directories = (
        #"my_root",
        "F:\mytest\folder\somewhere",
    )
    # list of all the file types we will check.
    etx_list = ( 
        ".cpp",
        ".h",
    )
    do_printing = True
    # Time the function with timestamps
    if do_printing:
        start = time_stamp()
    try:
        execute( match, directories, etx_list, do_printing=do_printing )
    except:
        print "Execute failed"
    if do_printing:
        end = time_stamp()
        print line_format
        print '%s function took %0.3f s' % ( execute.__name__, end - start )
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
