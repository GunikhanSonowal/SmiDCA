import csv
import glob

keyword = ["Please", "Sms", "Account","Customer",
           "Card","Email","Apple","Details","Update",
           "Iphone","Online","Bank","Link"," Message",
           "Call","Store","Today","Nationwide","Refund","Due"]

def get_feature(row):
    feature = []
    # temp = row.split()
    for key in keyword:
        if key in row:
            feature.append(1)
        else:
            feature.append(0)
    return feature

fp = glob.glob("*.txt")

if __name__ == "__main__":
    for row in fp:
        with open(row, 'r') as infile:
            fname = infile.read()
            writer.writerow(get_feature(fname))
