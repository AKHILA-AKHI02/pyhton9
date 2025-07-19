def most_frequent_char(text:str)->str:
    text=text.upper()
    text=text.replace(" ","")
    freq_dict={}
    for char in text:
        if char in freq_dict:
            freq_dict[char]+=1
        else:
            freq_dict[char]=1
    max_freq=max(freq_dict.values())
    most_frequent_chars=[
        char for char,freq in freq_dict.items()
                        if freq==max_freq]
    for char in text:
        if char in most_frequent_chars:
            return char
inp=input()
print(most_frequent_char(inp))

#o/p:
#HELLO WORLD
#l
