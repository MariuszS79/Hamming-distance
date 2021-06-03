print("HAMMING DISTANCE CALCULATOR\n")
print("The calculator compares 2 strings of same length and calculates the Hamming distance.\n")

def strings():
  global a
  global b
  a=input("\nType in first string: ")
  b=input("Type in second string: ")

  while len(a)!=len(b):
    print("The strings are not even length. Please type in equal length strings.")
    a=input("Type in first string: ")
    b=input("Type in second string: ")

def hd(a,b):
  count=0
  for i in range(len(a)):
    if a[i]!=b[i]:
      count=count+1
  return count
  print("The Hammstring distance is: "+count)

run=True
while run:
  strings()
  print("\nThe Hamming distance is",(hd(a,b)))
  again=input("\nWould you like to calculate again? (y/n): ")
  if again=="y" or again=="Y":
    run=True
  else:
    print("Have a nice day. Good bye")
    run=False
