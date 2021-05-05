# Risk-Dice

--- Why? 🤷‍ ---

A friend introduced me to the board game Risk a little while ago - for those who have never played the game before, you attack other 
players by choosing how many units (and therefore dice) you would like to attack with - depending on the number of units you have,
this will either be 1, 2, or 3 dice (red dice for attacker). The defending player must also choose how many dice to roll, again
based on how many units they have - they may only chose 1 or 2 dice to defend with (blue dice for defender). It's a simple (ish) 
case of highest number wins, except with a couple of caveats:

- the dice are paired up in order of highest to lowest, e.g. if red rolls a 3 and 2, and blue rolls a 1 and 5, then the 3 and 5 are paired
up and the 2 and 1 are paired up. In this case each player would lose a unit (red winning the 2v1 pairing, and blue winning the 5v3 pairing).

- in the event of a draw between a pairing of dice, the attacking player will win.

While playing, I found myself wondering what the probabilities of winning a 'skirmish' would be depending on whether you attack with
1, 2, or 3 dice. It would seem obvious that the battle would always be in the favour of the attacker, since they win any draws; but how much
in the favour of the attacker would it be? And what about cases when the attacker only has one die, and the defender has 2?

Naturally, I determined the most fun way to figure this out would be to create a Risk Dice Simulator, then run it many times to see the
results!

--- How? ---

"riskdice.py" (working and complete ✅) -  is a program which will give you the option to choose which combination of dice rolls you 
would like, and this can be repeated as many times as you like - the program will infinitely loop back to the selection menu. This means 
it can be used to play an actual game of risk as a substitute for dice, if you so wished.

"risk dice probability.py" (in progress, currently not functional ❌) - calls "riskdice.py" and runs it a specified number of times, 
returning the number of wins for each. Will have a menu to select dice roll combination, as well as number of times to run simulation, as
can be seen in the commented out code. As it is at the moment, both of these variables must be changed within the code and saved.
