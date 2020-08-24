def checkPalindrome(word1,word2):
  word1=word1.split()
  word2=word2.split()
  print(word1,word2)
  x=0
  y=0
  for i in range(len(word1)) : 
    if word1[i] in word2: 
  
       print(f'The word {word1[i]} is palindrome') 
       x +=1
    
    else :
       print(f'The word {word1[i]} not palindrome')
       y +=1
    
  if x > 0 and y==0 :
    return "The Phrase/Word is/are Palindrome "
  else : 
    return "The Phrase/Word is/are Not Palindrome "


first= input("enter a word").lower()
reversed_=first[::-1]
answer= checkPalindrome(first,reversed_)
print(answer)
