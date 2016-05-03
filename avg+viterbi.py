import nltk
from nltk.corpus import treebank
from nltk.probability import *
from nltk.grammar import *

### RETRIEVE ALL TREES AND THEN SELECT THE FIRST 100.
all_trees = treebank.parsed_sents()
trees_100 = all_trees[0:100]

### FUNCTION EXTRACTING LEAVES OF NODES WITH LABEL AS A PARAMETER OF getAvgNodeLength().
def getAvgNodeLength(label):

    l_leaves = list()
    for tree in trees_100:
        for node in tree:
            if node.label() == label:
                l_leaves.append(node.leaves())

### CREATED OWN LIST OF PUNCTUATION TO EXCLUDE SINCE USING string.punctuation WOULD
### HAVE DELETED WORDS SUCH AS "Dr.", "World-Wide", "U.S.", etc. WHICH ARE OF INTEREST.
    punct = [u"*", u",", u"&", u"'"]

    for wordlist in l_sbj:
        for word in wordlist:
            for i in punct:
                if i in word:
                    wordlist.remove(word)

### CREATE LIST OF LENGTHS (IN WORDS) OF NODES.
    l_len = list()
    for wordlist in l_leaves:
        l_len.append(len(wordlist))

### REMOVE ITEMS OF LENGTH 0 WHICH WOULD OTHERWISE AFFECT AVERGAGE.
    l_len = [i for i in l_len if i != 0]
    
### CALCULATE AVERAGE LENGTH ROUNDED TO 3 DECIMAL PLACES AND RETURN THE VALUE.
    avg_len = round(int(sum(l_len))/float(len(l_len)), 3)
    return avg_len
    
def pcfgParse(sentence):
    
    productions = list()
    root = nltk.Nonterminal('S')
    
    for tree in nltk.corpus.treebank.parsed_sents():
        productions += tree.productions()

    grammar = nltk.induce_pcfg(root, productions)
    PCFGParser = nltk.ViterbiParser(grammar)

    s_sent = sentence.split()
    parsed_sent = PCFGParser.parse(s_sent)

    for p in parsed_sent:
        print p
