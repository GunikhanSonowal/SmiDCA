###################################
## Character count
############################

##############################
# import glob
# import csv
# outfile = open("Character_in_file.csv", "w")
# writer = csv.writer(outfile)
# file_name = glob.glob("*.txt")
# for f in file_name:
#     infile = open(f, "r")
#     line = f, str(len(infile.read()))
#     writer.writerow(line)
####################################
     
def character_count(line):
     return str(len(line))
     
if __name__ == "__main__":
     test = "hello how are you"
     print character_count(test)


