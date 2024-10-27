# Squaredle-near-misses

Finds all the words in a squaredle board that ***ALMOST*** work

## Motivation:

Me and my friends have been enjoying this game squaredle ([squaredle.app](https://squaredle.app/)) where you connect letter in a grid to form words. However, what's most frustrating about this game is finding a word that almost works but doesn't. This code attempts to find all the words in a given squaredle that almost works.

## What does it mean for a word to almost work?

There's many ways we could define a word that almost works. Some possible definitions are:
- A word that is off by one letter
- All the letters needed for the word are in the grid and connected, but not connected in the right order.
- Proper nouns

For this code, I will define a word that almost work to be words that work for every letter until the very last letter. (So the word "definition" will be a word that almost works if you can make the string "definitio" in the squaredle).