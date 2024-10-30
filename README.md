# Squaredle-near-misses

Finds all the words in a squaredle board that ***ALMOST*** work

## Motivation:

Me and my friends have been enjoying this game squaredle ([squaredle.app](https://squaredle.app/)) where you connect letter in a grid to form words. However, what's most frustrating about this game is finding a word that almost works but doesn't. This code attempts to find all the words in a given squaredle that almost works.

## What does it mean for a word to almost work?

There's many ways we could define a word that almost works. Some possible definitions are:
- A word that is off by one letter
- All the letters needed for the word are in the grid and connected, but not connected in the right order.
- Proper nouns

For this code, I will define a word that almost work to be 6 or more lettered words that work for every letter until the very last letter. (So the word "definition" will be a word that almost works if you can make the string "definitio" but not "defenition" in the squaredle).

## How to run the program.
Just download dictionary.txt, project.py and main.py and run main.py. The program will ask you to input the number of rows and columns of the squaredle, then input the letters in each position on the squaredle (not case sensitive). For empty tiles, write a "#". Then it'll find and output all the near miss words it finds.

## Things I would like to change about this code in the future.
Currently, the code finds a lot of words that are also words in the squaredle but with a "s" at the end. I wouldn't really say that these words "almost work" as the singular version of the word does infact work. The code right now also outputs the words from longest to shortest. This isn't bad but in the future, it'll be good if the words are instead outputted in order of how much use the word gets (how common the word is).