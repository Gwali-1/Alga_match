
class patternAlga():
    """
        CLASS:
            PatternAlga
        
        FUNCTIONS:
        Is_Word_in(string , string2) 
        [
        string => piece of text to search through
        string2 => word string to locate in  passage or text

        "--" shows position(s) of matched words
        ]

        is_phrase_in(string , phrase)
        [
            string => larger text or passage to search through
            phrase => phrase to locate in "string"
            "--" shows position(s) of matched phrase
        ]

        //all parameters must be strings

        [Description]
        A SIMPLE PATTERN MATCHING ALGORITHM IMPLEMENTED WITH NO LIBRARIES
        JUST NATIVE FUCTIONS AND LOOPS
        CLASS HAS 2 FUNCTIONS 
        CAPABLE OF LOCATING A WORD IN A LARGE TEXT
        CAPABLE OF LOCATING A PIECE OF PHRASE IN A LARGE TEXT


    """
    ##initiatlizer method
    def __init__(self):
        pass
        # for i in tqdm(range(30)):
        #     time.sleep(0.03)
    ##fistmethod that checks for match of word in a string

    def Is_Word_In(self,string,word):
     
        temp_1 = [x for x in string.lower()]   #turn passage into list

        #turn word into list 
        word_container =[x for x in word.lower()]

        #empty list to contain spaces to be removed
        temp_2 =[]
        #getting length of both word and string

        sequence_length = len(temp_1)
        word_length = len(word)
       
        count = 0  #helper variable => to help keep track of shifts in text when spaces are removed

        #loop to identify spaces is string
        for i in range(sequence_length - 1):
            if temp_1[i] == " ":
                #storing indexes of spaces in list temp_2
                temp_2.append(i)
            #loop to remove spaces from string
        for i in temp_2: 
            temp_1.remove(temp_1[i -count])
            count+= 1
        #loop to locate  word in string
        for i in range(sequence_length):
            
            start = i 
            end = start + word_length
            if temp_1[start:end] == word_container:
                temp_1[start:end] = "-" * len(temp_1[start:end])
                #if found
                check = "True"
        if check == "True":
            print("Found!")
            for i in temp_2:
                temp_1.insert(i ," ")
            print("Location:","".join(temp_1))
            return 1
        else:
            print("Not Found")
            return 0
   

    

    def is_phrase_in(self,string,phrase):
        temp1 = [ x for x in string.lower()]
        temp2 = [x for x in phrase.lower()]
        temp1_spaces = list()
        temp2_spaces = list()
        string_len = len(temp1)
        phrase_len = len(temp2)
        count = 0
        for ele in range(string_len - 1):
            if temp1[ele] == " ":
                temp1_spaces.append(ele)
        for ele in range (phrase_len):
            if temp2[ele] == " ":
                temp2_spaces.append(ele)
        for i in temp1_spaces:
            temp1.remove(temp1[i - count])
            count+=1
        count = 0
       

        for i in temp2_spaces:
            temp2.remove(temp2[i - count])
            count+=1
        phrase_len = phrase_len - count

        check = False
        for i in range(string_len):
            start = i
            end = start + phrase_len
            
            if temp1[start:end] == temp2:
                temp1[start:end] = "-" * len(temp1[start:end]) 
                check =  "True"
                break
        if check == "True":
            print("Found!")
            for i in temp1_spaces:
                temp1.insert(i ," ")
            print("location:","".join(temp1))
            return 1
        else:
            print("Not Found")
            return 0
                  
test = patternAlga()



##test case 
foo = " the man is the one we want "
bar = " one we"
print(test.is_phrase_in(foo,bar))  #Returns 1 , and prints  Found and the location of word or phrase

