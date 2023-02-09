# wordle_knower


A unintuitive solution for wordle game, requires you to download a lexicon of words as a textfile, see words.txt and sve_ord.txt

Note that some words don't exist in the lexicons, and others have a different inflection and will not be found. 

To run: Make a guess in ordel.se or wordle. 

for example in english

1st guess: opera

O is at the correct place

a is correct but in wrong place
   
Write in terminal to find possible words in that combination:

python wordle.py e o**** operA
    
Then the script will know the position of O and that A is in the word but not in the 5th position. 

And write all possible corresponding words (in the word file)

2nd Guess: oatly

write in terminal:

python wordle.py e o**** operA,oAtly

    and the game goes on. 

Note that the script can be optimised drastically to improve computation time, also not fully tested for bugs.

Swedish dictionary at:
https://github.com/titoBouzout/Dictionaries/blob/master/Swedish.dic 

English dictionary:
https://github.com/dwyl/english-words/blob/master/words.txt
