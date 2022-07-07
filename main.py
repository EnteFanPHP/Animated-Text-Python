import os, time

os.system("clear")
text = "By EnteFan"; # <- Text goes here
length = len(text);
toPrint = "";
for i in range(length):
    toPrint += text[i]
    print(toPrint)
    time.sleep(25/100) # 1/4 seconds (0,25 miliseconds)
    os.system("clear")
    
print("Finished Text:", text)
print("By EnteFan")
