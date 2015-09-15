#!/usr/bin/python
# -*- coding: latin-1 -*-
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# generategrid.py Authored by Nathan Ross Powell.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Generates a random grid (world) with a path through it to an exit point.
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports.
import random
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Globals.
GridSize = 30
TileChance = 0.35
Spacing = 1
# Tiles.
EdgeTile = "#"
BlockedTile = "."
EmptyTile = " "
StartTile = "S"
EndTile = "E"
UsedTile = "o"
PlayerTile = "@"
RouteTile = "."
# Directions.
Up = ( 0, 1 )
Down = ( 0, -1 )
Left = ( -1, 0 )
Right = ( 1, 0 )
Quit = "QUIT"
InputUp = ( "w", "up" )
InputLeft = ( "a", "left" )
InputDown = ( "s", "down" )
InputRight = ( "d", "right" )
InputQuit = ( "q", "quit" )
# Usage.
Usage = """Usage:
  Directions:
    Up    = %s
    Left  = %s
    Down  = %s
    Right = %s
  Quit :
    Quit option = %s
    Cmd quit = ctrl+c""" % ( 
    InputUp, 
    InputLeft, 
    InputDown, 
    InputRight, 
    InputQuit
)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test fucntions.
def RandomTile():
    #return BlockedTile if bool( random.getrandbits( 1 ) ) else EmptyTile
    return BlockedTile if random.random() < TileChance else EmptyTile
def RandomLine():
    return [ RandomTile() for i in range( GridSize ) ]
def RandomGrid():
    return [ RandomLine() for i in range( GridSize ) ]
def RandomGoals( grid ):
    width = len( grid )
    def SetGoalTile( goalTile, tileIndex ):
        row = int( tileIndex % width)
        col = int(tileIndex / width)
        grid[ row ][ col ] = goalTile
        return ( row, col )
    tiles = [ i for i in range( width ** 2 ) ]
    random.shuffle( tiles )
    #SetGoalTile( StartTile, tiles[ 0 ] )
    goalXY = SetGoalTile( EndTile, tiles[ 1 ] )
    return goalXY
def RandomPlayerPosition( grid ):   
    width = len( grid )
    def TileIsFree( tileIndex ):
        tile = None
        row = int( tileIndex % width)
        col = int(tileIndex / width)
        if grid[ row ][ col ] == EmptyTile:
            tile = ( row, col )
        return tile
    tiles = [ i for i in range( width ** 2 ) ]
    random.shuffle( tiles )
    for tileIndex in tiles:
        locationForPlayer = TileIsFree( tileIndex )
        if locationForPlayer is not None:
            SetGridLocation( grid, locationForPlayer, PlayerTile )
            return locationForPlayer
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Grid maneuvering.
def SetGridLocation( grid, location, tile ):
    try:
        oldTile = grid[ location[ 0 ] ][ location[ 1 ] ] 
        grid[ location[ 0 ] ][ location[ 1 ] ] = tile
        return oldTile
    except:
        print("ERROR:SetGridLocation")
    return EdgeTile
def ValidGridLocation( grid, locationXY, testTiles = None ):
    valid = False
    try:
        tile = grid[ locationXY[ 0 ] ][ locationXY[ 1 ] ]
        if testTiles is None or tile in testTiles:
            valid = True
    except:
        pass
    return valid
def TestMove( grid, toMoveXY, direction, testTiles = None ):
    x = toMoveXY[ 0 ] + direction[ 0 ]
    y = toMoveXY[ 1 ] + direction[ 1 ]
    location = ( x, y )
    if ValidGridLocation( grid, location, testTiles ):
        return location
def MoveLocation( grid, toMoveXY, direction ):
    validTiles = ( EmptyTile, EndTile )
    newLocation = None
    isEndTile = False
    if ValidGridLocation( grid, toMoveXY ):
        newLocation = TestMove( grid, toMoveXY, direction, validTiles )
        if newLocation is not None:
            prevTile = SetGridLocation( grid, toMoveXY, EmptyTile )
            finishingTile = SetGridLocation( grid, newLocation, prevTile )
            isEndTile = finishingTile == EndTile
    return newLocation, isEndTile
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Path finding.
def PathFind( grid, startXY, goalXY ):
    return False
def VerifyPath( grid, startXY, goalXY ):
    result = PathFind( grid, startXY, goalXY )
    if result:
        # test more stuff.
        pass
    return result
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Player input.
def PlayerInput( text ):
    try:
        return input( text ).strip()
    except (KeyboardInterrupt, SystemExit):
        return Quit
    except:
        raise
def GetDirection( input ):
    text = input.lower()
    direction = None
    if text in InputUp:
        direction = Up
    elif text in InputDown:
        direction = Down
    elif text in InputLeft:
        direction = Left
    elif text in InputRight:
        direction = Right
    elif text in InputQuit:
        text = Quit
    return text, direction
def PlayerMoveMentLoop( grid ):
    goalPos = RandomGoals( grid )
    playerPos = RandomPlayerPosition( grid )
    print("Verified path :", str( VerifyPath( grid, playerPos, goalPos ) ))
    print("Character tile = %s" % ( PlayerTile, ))
    print("Maze exit tile = %s" % ( EndTile, ))
    PrintGrid( grid )
    while True:
        text, direction = GetDirection( PlayerInput( "Direction >" ) )
        if text != Quit:
            if direction is not None:
                newPosition, end = MoveLocation( grid, playerPos, direction )
                if newPosition is not None:
                    playerPos = newPosition
                    PrintGrid( grid )
                    if end:
                        print("Well played, sir.")
                        break
                else:
                    print("Can't let you do that")
            else:
                print(Usage)
        else:
            print("Quitter")
            break
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Print utils.
def RotateGrid( grid ):
    def GetLine( i ):
        return [ line[ i ] for line in grid ]
    return [ GetLine( i ) for i in reversed( range( len( grid ) ) ) ]
def PrintGrid( grid ):
    space = " " * Spacing
    newGrid = RotateGrid( grid ) 
    def PrintLine():
        print(( EdgeTile + space ) * ( len( newGrid ) + 2 ))
    lineNum = 0
    PrintLine()
    for line in newGrid:
        toPrint = EdgeTile
        for tile in line:
            toPrint += space + tile
        toPrint += space + EdgeTile
        print(toPrint)
        lineNum += 1
    PrintLine()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Main logic.
if __name__ == "__main__":
    try:
        import sys
        random.seed(  sys.argv[ 1 ] )
    except:
       pass
    grid = RandomGrid()
    PlayerMoveMentLoop( grid )
