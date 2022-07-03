 #Part 2 - Student Version(Validation)

def add():
      num=0
      while num==0:
        a_a=False           # for make a loop for pass
        b_b=False           # for make a loop for defer 
        c_c=False           # for make a loop for  fsil

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
                break  #break loop
            
    
        D=(a,b,c) # Credits (pass,defer,fail)

        if D==(120,0,0):   #1 
            print('Progress')
        elif D==(100,20,0):   #2
            print('Progress (module trailer)')
        elif D==(100,0,20):  #3
            print('Progress (module trailer)')
        elif D==(80,40,0): #4
            print('Do not Progress – module retriever')
        elif D==(80,20,20): #5
            print('Do not Progress – module retriever')
        elif D==(80,0,40): #6
            print('Do not Progress – module retriever')
        elif D==(60,60,0): #7
            print('Do not progress – module retriever')
        elif D==(60,40,20):  #8
            print('Do not progress – module retriever')
        elif D==(60,20,40):  #9
            print('Do not progress – module retriever')
        elif D==(60,0,60):   #10
            print('Do not progress – module retriever')
        elif D==(40,80,0):  #11
            print('Do not progress – module retriever')
        elif D==(40,60,20):  #12
            print('Do not progress – module retriever')
        elif D==(40,40,40):  #13
            print('Do not progress – module retriever')
        elif D==(40,20,60):  #14
            print('Do not progress – module retriever')
        elif D==(40,0,80):   #15
            print('Exclude')
        elif D==(20,100,0):  #16
            print('Do not progress – module retriever')
        elif D==(20,80,20):  #17
            print('Do not progress – module retriever')
        elif D==(20,60,40):  #18
            print('Do not progress – module retriever')
        elif D==(20,40,60): #19
            print('Do not progress – module retriever')
        elif D==(20,20,80):   #20
            print('Exclude')
        elif D==(20,0,100):  #21
            print('Exclude')
        elif D==(0,120,0):  #22
            print('Do not progress – module retriever')
        elif D==(0,100,2):  #23
            print('Do not progress – module retriever')
        elif D==(0,80,40):  #24
            print('Do not progress – module retriever')
        elif D==(0,60,60):   #25
            print('Do not progress – module retriever')
        elif D==(0,40,80):  #26
            print('Exclude')
        elif D==(0,20,100):  #27
            print('Exclude')
        elif D==(0,0,120):  #28
            print('Exclude')
add()
            

