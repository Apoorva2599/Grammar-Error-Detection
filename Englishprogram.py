import nltk

#loading cfg file 
grammar = nltk.data.load('file:MyGrammar.cfg') 

#Taking input sentences from user
for _ in range(int(input("Enter number of sentences you want to check: "))):
    sentence = input("Enter Your Sentence: ")
    
    #a flag for wrong syntax
    wrong=1
    #splitting sentences into words
    sent_split = sentence.split()
    #POS tagging each word  
    tagged = nltk.pos_tag(sent_split) 
    #converting tags to lowercase
    tags = [x[1].lower() for x in tagged] 
    #print(tags)
    
    #Using a Recursive Descent Parser for parsing sentences through cfg
    try:
        parser = nltk.RecursiveDescentParser(grammar)
        
        #If the tags are parsed it will return a tree and hence it is a correct sentence else not
        for tree in parser.parse(tags):
            s = tree
            #print(s)
            wrong=0
            print("Correct Grammar!!!!")
            print("*"*20)
        
        if wrong==1:
            print("Wrong Grammar!!!")
            print("*"*20)
    
    except ValueError:
        print("Sorry! Some words are not covered in the grammar yet :)")
        
        
''' 
TAGS that are not covered:
    
Card_No -> 'cd'
VBN -> 'vbn' 
Adj_S -> 'jjs'
CC -> 'cc'
EX -> 'ex'
FW -> 'fw'
LS -> 'ls'
PDT -> 'pdt'
POS -> 'pos'
RBR -> 'rbr'
RBS -> 'rbs'
RP -> 'rp'
SYM -> 'sym'
UH -> 'uh'
WDT -> 'wdt'
WP -> 'wp'
WP_D -> 'wp$'
WRB -> 'wrb'

'''  
