#############################################
## Smishing
#########################################
import glob
import csv
from Character_count import character_count # size of email
from Email_check import email_check # check availability of email
from Http_check import http_check # check the hyperlink
from Phone_number import phoneNumber_check # phone number check
from Suspicious_symbol import special_character # special symbol
from keyword_feature import get_feature
from Misspelled import misspell
from Pos_nltk import pos_token
from readability import readabilitySmishing

fp = glob.glob("*.txt") 
def feature_extract(test):
    email = email_check(test)
    size = character_count(test)
    http = http_check(test)
    phone = phoneNumber_check(test)
    special = special_character(test)
    keyword = get_feature(test)
    misspel = misspell(test)
    post = pos_token(test)
    reada = readabilitySmishing(test)
    return ([keyword+[size]+[email]+[http]+[phone]+[special]+ [misspel] + post + reada])

if __name__ == "__main__":
    fp = open("test1.txt", "r")
    feature_extract(fp.read())
    

    
