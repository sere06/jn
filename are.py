analyzed=""
text=""" i
am
siddhi"""
for char in text:
    print("\nchar in f :",char)
    if char !="\n":
        analyzed=analyzed+char
        print("\n word after if : ",analyzed)
print("\nafter for",analyzed)