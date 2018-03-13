####################################
## Spell checker
####################################
import enchant
import re
def misspell(text):
    d = enchant.Dict("en_US")
    
    text_str = re.sub(r'[?|$|.|!|,|@|#|^|*]',r'', text) # remove the special character
    line = text_str.split(" ") # creating token
    #print line
    len_line = len(line)
    #print "length",  len_line
    count = 0
    for word in line:
    #print d.check(word)
    	if word == "":
    		pass
    	else:
        	if d.check(word) == False:
		        #print d.check(word)
		        count += 1
		        #print "total misspell", count
    temp = (float(count) / len_line)*100
    return round(temp,2)

if __name__ =="__main__":
    text = "hello how are you, my name gunikhan sonowal"
    print misspell(text)
    
