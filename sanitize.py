import re

filePath = "tweets.txt" 
filep = open("clean_tweets.txt", "w", encoding="utf-8")
print("Starting sanitization...")
count = 0

f = open(filePath, encoding="utf-8")

line = f.readline()
while line:
    line = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",line).split())
    filep.write(line + "\n")
    line = f.readline()

print("Finished")
filep.close()




