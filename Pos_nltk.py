##########################
# Part of speech
#Here we see that and is CC, a coordinating conjunction; now and completely are RB, or adverbs; for is IN, a preposition; something is NN, a noun; and different is JJ, an adjective.
########################
import nltk
import enchant
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
def pos_token(text):
    text = nltk.tokenize.word_tokenize(text)
    #print text
    noun = conjunction = adverb = preposition = adjective = pronoun = verb = 0
    temp =  nltk.pos_tag(text)
    for line in temp:
        if line[1] == "NN":
            #print "noun"
            noun +=1
        elif line[1] == 'PRP':
            #print "pronoun"
            pronoun += 1
        elif line[1] == 'JJ':
            #print "Ajective"
            adjective += 1
        elif line[1] == "VB":
            #print "verb"
            verb += 1
        elif line[1] == 'RB': # adverbs
            #print "adverb"
            adverb += 1
        elif line[1] == "IN":
            #print "preposition"
            preposition += 1
        elif line[1] == "CC":
            #print "conjunction"
            conjunction += 1
    return [noun, pronoun, adjective, verb, adverb, preposition, conjunction]

if __name__ =="__main__":
    line = "Alas! he go And now for something completely different"
    print pos_token(line)
    

