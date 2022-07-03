# Part 3 - Staff Version with Histogram

print('Staff Version with Histogram')
print()
#Progress=0
#Trailer=0
#Retriever=0
#Excluded=0

def add():
    Progress=0
    Trailer=0
    Retriever=0
    Excluded=0
    num=0
    while num==0:
        a_a=False           # for make a loop for pass
        b_b=False           # for make a loop for defer 
        c_c=False           # for make a loop for  fail

        

        range=(0,20,40,60,80,100,120)  #range of inputs

        total_check=0   # total of pass,defer,fail

        
        while total_check!=120:

            while not a_a:
                try:
                  a=int(input('Please enter your credits at pass: ')) # input pass
                  if a not in range:
                      print('Out of range')
                  else:
                      a_a=True 
              
                except:
                  print('Integer required')
              
            while not b_b:
                try:
                  b=int(input('Please enter your credits at defer: ')) # input defer
                  if b not in range:
                      print('Out of range')
                  else:
                      b_b=True 
                except:
                  print('Integer required')

            while not c_c:
                try:
                  c=int(input('Please enter your credits at fail: '))  # input fail
                  if c not in range:
                      print('Out of range')
                  else:
                      c_c=True
                except:
                  print('Integer required')
            
            if a+b+c==120:
                total_check=120
            else:
                print('Total incorrect')
                print()
                add()
                
                
            
        
        D=(a,b,c) # Credits (pass,defer,fail)

        

        if D==(120,0,0):   #1
            Progress+=1
            print('Progress')
            
        elif D==(100,20,0):   #2
            print('Progress (module trailer)')
            Trailer+=1
        elif D==(100,0,20):  #3
            print('Progress (module trailer)')
            Trailer+=1
        elif D==(80,40,0): #4
            print('Do not Progress – module retriever')
            Retriever+=1
        elif D==(80,20,20): #5
            print('Do not Progress – module retriever')
            Retriever+=1
        elif D==(80,0,40): #6
            print('Do not Progress – module retriever')
            Retriever+=1
        elif D==(60,60,0): #7
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(60,40,20):  #8
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(60,20,40):  #9
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(60,0,60):   #10
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(40,80,0):  #11
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(40,60,20):  #12
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(40,40,40):  #13
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(40,20,60):  #14
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(40,0,80):   #15
            Excluded+=1
            print('Exclude')
        elif D==(20,100,0):  #16
            Excluded+=1
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(20,80,20):  #17
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(20,60,40):  #18
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(20,40,60): #19
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(20,20,80):   #20
            Excluded+=1
            print('Exclude')
        elif D==(20,0,100):  #21
            Excluded+=1
            print('Exclude')
        elif D==(0,120,0):  #22
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(0,100,2):  #23
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(0,80,40):  #24
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(0,60,60):   #25
            print('Do not progress – module retriever')
            Retriever+=1
        elif D==(0,40,80):  #26
            Excluded+=1
            print('Exclude')
        elif D==(0,20,100):  #27
            Excluded+=1
            print('Exclude')
        elif D==(0,0,120):  #28
            Excluded+=1
            print('Exclude')
        


        print()  #blank line
        
        y_n=False
        while not y_n:
            answer=input("Enter 'y' for yes or 'q' to quit and view results: ")
            if answer=='y':
                print()  # blank line
                y_n=True
                
            elif answer=='q':
                print()
                y_n=True
                num=1
                break               




    s1=Progress*"*"
    s2=Trailer*"*"
    s3=Retriever*"*"
    s4=Excluded*"*"
    total_out=Progress+Trailer+Retriever+Excluded

    print()
    print('Horizontal Histogram')
    print('Progress ',Progress,' :',s1)
    print('Trailer ',Trailer,'  :',s2)
    print('Retriever ',Retriever,':',s3)
    print('Excluded ',Excluded,' :',s4)

    print() #blank line
    print(total_out,'outcomes in total')
add()


