 #Part 1 - Student Version

num=0
while num==0:
  a=int(input('Please enter your credits at pass: ')) #pass
  b=int(input('Please enter your credits at defer: ')) #defer
  c=int(input('Please enter your credits at fail: '))  #fail

  D=(a,b,c) # Credits (pass,defer,fail)

  if D==(120,0,0):    #1
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
  print() # blank line
