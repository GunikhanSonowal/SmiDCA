import re
import glob
specialPattern = re.compile(r'\$\d')

def special_character(line):
    if specialPattern.findall(line):
        return 1
    else:
        return 0
fp = glob.glob("*.txt")    
if __name__ == "__main__":
    for file_name in fp:
        fname = open(file_name, "r")
        print file_name, special_character(fname.read())
