#The mathematician Srinivasa Ramanujan found an infinite series that can be used to generate a numerical approximation of 1 / π:
# Write a function called estimate_pi that uses this formula to compute and return an estimate of π. It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.
import math
def fact(k):
  f=1
  if(k==0 or k==1):
    f=1
  else:
    for i in range(1,k+1):
      f=f*i
  return f


def est():
  sum=0
  fc=(2*math.sqrt(2))/9801
  print("fc=",fc)
  ip=1/math.pi
  print("1/pi=",ip)
  print("pi=",math.pi)
  k=0
  while (True):
    num=(fact(4*k))*(1103+(26890*k))
    den=((fact(k))**4)*(396**(4*k))
    term=fc*(num/den)
    sum=sum+term
    if(abs(term)<1e-15):
      break
    k=k+1
  print("calculated 1/pi",sum)
  pi=1/sum
  return(pi)
print("calculated pi",est())

    
#adding suffix to words
fruit="banana"
i=0
while i<len(fruit):
  letter=fruit[i]
  print(letter)
  i=i+1
pr='JKLMNOPQ'
su='ack'
for letter in pr:
  if(letter=='O' or letter=='Q'):
    print(letter+'uack')
  else:
   print(letter+su)
#finding total number of given character in word
def fin(word,letter):
  i=0
  char=0
  while i<len(word):
    if word[i]==letter:
      char=char+1
      
    i=i+1
  return char
  return -1
print(fin('mridaiini','i'))



#finding if two words are reverse of each other and finding if its a palindrome
def rev(word1,word2):
  if len(word1)!=len(word2):
    return False
  word3=word1[::-1]
  if(word1==word3):
    print("pali")
  i=0
  j=len(word2)-1
  while(j>=0):
    if word1[i]!=word2[j]:
      return False
    i=i+1
    j=j-1
  return True
  
  
print(rev('dad','dad')) 