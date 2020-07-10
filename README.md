# Grammar-Error-Detection
Implementing Grammatical error detection using NLTK and CFG.

This model has been implemented using NLTK's POS Tagger and RecursiveDescent Parser. A CFG is made which includes some English grammar rules and the tags are used as terminals. Not all tags and grammar rules are covered in the CFG.

## To run the project: 
Before running make sure you have NLTK installed in your computer. If not, install it using "pip install nltk" command using terminal.

1. Clone the project and open your terminal.
2. Move to the path where you have cloned it. 
3. Type the command - python Englishprogram.py

### Output:
1. If the sentence is correct: "Correct Grammar!!!". 
2. If the sentence is wrong: "Wrong Grammar!!!". 
3. If the word is not covered in the grammar: "Sorry! Some words are not covered in the grammar yet :)".

Note: This is a sample model to provide a basic idea of how to implement it. You can always add up your own grammar rules for detection.
