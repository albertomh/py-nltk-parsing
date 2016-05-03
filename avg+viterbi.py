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
