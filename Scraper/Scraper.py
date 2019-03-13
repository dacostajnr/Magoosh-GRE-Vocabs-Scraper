def write_to_file(text):
    file=open("wordss.txt","a")
    file.write(text)
    file.write("\n")
    file.close()

f=open("data.json","r")
data=f.readlines()
data=eval(data[0])

for i in data:
    word = i["slug"]
    meaning = i["back"][1]["content"]
    try:
    	for j in meaning:
    		if(j=="/"):
    			meaning = meaning[meaning.index(j):]
    			meaning = meaning[meaning.index(">")+1:]
    except:
    	pass
    example = i["back"][2]["content"].replace(r"<strong>","").replace(r"</strong>","")
    if True or len(word)>=15 or ("magoosh" not in word.lower()):
    	if 'a'==word.lower()[0]:
    		print(word)
    	# if "--" in example:
    	# 	print(example)
    	# 	print("\n\n")
	    # print("-----------------------------------------------------------------------------------------")
	    # print("word====={}".format(word))
	    # print("meaning====={}".format(meaning))
	    # print("example====={}".format(example))
	    # print("-----------------------------------------------------------------------------------------") 
	   #write_to_file(word+"----->"+meaning+"\n"+"[{}]".format(example)+"\n\n")

