import pandas as pd
import sys

"""

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

"""

if __name__ == "__main__":   
    language=sys.argv[1]
    if language=="e":
        data=pd.read_csv("words.txt", sep='\t',names=["words"])
        letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    else:
        data=pd.read_csv("sve_ord.txt", sep='\t',names=["words"])
        letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','å','ä','ö']


    alphabet=pd.DataFrame()
    alphabet["ch"]=letters
    letters=["","","","",""]

    corr=sys.argv[2]

    for ind,val in enumerate(corr):
        if val != "*":
            letters[ind]=val

    fail_words=(sys.argv[3]).split(",")
    fail_pos={}
    for word in fail_words:
        for ind,ch in enumerate(word):
            if not ch.islower():
                if ch.lower() not in fail_pos.keys():
                    fail_pos[ch.lower()]=[ind]
                else:
                    if ind not in fail_pos[ch.lower()]:
                        fail_pos[ch.lower()].append(ind)
    fail_words=[word.lower() for word in fail_words]
    failed_letters="".join(fail_words)
    failed_letters=[ch for ch in failed_letters if ch not in fail_pos.keys() and ch not in corr]
    alphabet = [ch for ch in alphabet['ch'] if ch not in failed_letters]
    wordlist=[]

    print(alphabet)
    print(fail_words)
    print(fail_pos)

    for ch1 in alphabet:
        if letters[0] != "": 
            ch1=letters[0]
        for ch2 in alphabet:
            if letters[1] != "": 
                ch2=letters[1]
            for ch3 in alphabet:
                if letters[2] != "": 
                    ch3=letters[2]
                for ch4 in alphabet:
                    if letters[3] != "": 
                        ch4=letters[3]
                    for ch5 in alphabet:
                        if letters[4] != "": 
                            ch5=letters[4]
                        word=ch1+ch2+ch3+ch4+ch5
                        wordlist.append(word)

    final=pd.DataFrame()
    final["words"]=wordlist
    print(len(final))
    final = final[final["words"].isin(data["words"])]
    final.reset_index(drop=True,inplace=True)
    final=final["words"]
    finalfinal=[]
#ord lista
    for i in range(0,len(final)):
        flag=False
        #par i lexikon
        for items in fail_pos.items():
            #index per unknown bostav
            for index in items[1]:
                #om index för bokstaven finns i ordet 
                if  items[0] == final[i][index]:
                    flag=True
                    pass
        if flag is False:
            finalfinal.append(final[i])

    finalfinal = list(dict.fromkeys(finalfinal))
    print(len(final))
    print(len(finalfinal))

    #prints final list of possible words
    print(finalfinal)
