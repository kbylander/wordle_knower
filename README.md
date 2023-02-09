# wordle_knower


A unintuitive solution for wordle game, requires you to download a lexicon of words as a textfile, see words.txt and sve_ord.txt

Note that some words don't exist in the lexicons, and others have a different inflection and will not be found. 

To run: Make a guess in ordel.se or wordle. 

for example in english: 
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

sys.argv[1] : language (e for english, s for swedish)
sys.argv[2] : [correct words with * where unknown]
sys.argv[3] : [guessed words separated by comma, unknown letters uppercase,correct leters lowercase]


Note that the script can be optimised drastically to improve computation time.
