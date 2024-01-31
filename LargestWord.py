string = input("Enter a string :")
s = string.split()
max = 0

for ele in s:
    if(len(ele)>max):
        max = len(ele)
        max_word = ele

print("Largest word in given string is :",max_word)
print("The length of largest word is :",len(max_word))