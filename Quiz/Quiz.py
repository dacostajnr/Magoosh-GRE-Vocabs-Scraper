import random
fullset={}
wrongs=0
correct=0
questions_answered=0
def write_to_file(text):
    file=open("wordss.txt","a")
    file.write(text)
    file.write("\n")
    file.close()
f=open("data.json","r")
data=f.readlines()
data=eval(data[0])
for i in data:
    # get word here
    word = i["slug"]
    # get meaning here 
    meaning = i["back"][1]["content"]
    try:
    	for j in meaning:
    		if(j=="/"):
    			meaning = meaning[meaning.index(j):]
    			meaning = meaning[meaning.index(">")+1:]
    except:
    	pass
    # get example here
    example = i["back"][2]["content"].replace(r"<strong>","").replace(r"</strong>","")
    fullset[word]={}
    fullset[word]["example"]=example
    fullset[word]["meaning"]=meaning
OPTIONS = {0:"A",1:"B",2:"C",3:"D",4:"E"}
_OPTIONS = {"A":0,"B":1,"C":2,"D":3,"E":4}
# get a random word:
def get_rand_sent():
    all_words = list(fullset.keys())    
    random_word = random.choice(all_words)     
    # get the sentence of the word 
    sentence = fullset[random_word]["example"]
    if random_word in sentence:
        sentence = sentence.replace(random_word,"_____________") # sentence 
    else:
        sentence.replace(random_word[0:(len(random_word)//2)])            
    choices = [] 
    choices.append(random_word)  
    for i in range(0,4):
        choices.append(random.choice(all_words)) # answer choices         
    random.shuffle(choices)
    return (sentence,random_word,choices)
def main():    
    global wrongs
    global correct
    while True:
        try:
            sentence,correct_answer,choices=get_rand_sent()
            # print sentence 
            print(" "+sentence)  
            print("\n")
            # print options
            #choices = [one,two,three]
            for i in range(len(choices)):
                print(OPTIONS[i]+"."+choices[i])        
            print("\n")
            # get user input
            user_choice = input("Choose option: ").upper()            
            if choices[_OPTIONS[user_choice]]==correct_answer:
                print("Correct")
                correct+=1
            else:
                print("Wrong")
                print("Correct Answer is :{}".format(correct_answer)) 
                wrong+=1
            print("\n")
            print("\t\t"+"correct:{}\t\t wrongs:{}".format(correct,wrongs))                        
        except:
            print("\t\t WARNING !!! Only 'A' 'B' 'C' 'D' allowed ")
        print("\n\n\n")
main()
