

def encrypt(phase):
   encryption = ""
   for letter in phase:
      if letter in "aA":
         encryption = encryption + "!"
      elif letter in "bB":
         encryption = encryption + "J"
      elif letter in "cC":
         encryption = encryption + "2"
      elif letter in "dD":
         encryption = encryption + "9"
      elif letter in "eE":
         encryption = encryption + "6"
      elif letter in "fF":
         encryption = encryption + "^"
      elif letter in "gG":
         encryption = encryption + "&"
      elif letter in "hH":
         encryption = encryption + "*"
      elif letter in "iI":
         encryption = encryption + "q"
      elif letter in "jJ":
         encryption = encryption + "8"
      elif letter in "kK":
         encryption = encryption + "$"
      elif letter in "lL":
         encryption = encryption + "3"
      elif letter in "mM":
         encryption = encryption + "7"
      elif letter in "nN":
         encryption = encryption + "t"
      elif letter in "oO":
         encryption = encryption + "9"
      elif letter in "pP":
         encryption = encryption + "Q"
      elif letter in "qQ":
         encryption = encryption + "-"
      elif letter in "rR":
         encryption = encryption + "%"
      elif letter in "sS":
         encryption = encryption + "4"
      elif letter in "tT":
         encryption = encryption + "#"
      elif letter in "uU":
         encryption = encryption + "/"
      elif letter in "vV":
         encryption = encryption + "B"
      elif letter in "wW":
         encryption = encryption + ">"
      elif letter in "xX":
         encryption = encryption + "f"
      elif letter in "yY":
         encryption = encryption + "h"
      elif letter in "zZ":
         encryption = encryption + "r"
    
   return encryption

print(encrypt(input("Enter a message: ")))

def deencrypt(phase):
   deencryption = ""
   for letter in phase:
      if letter in "!":
         deencryption = deencryption + "a"
   return deencryption



print(deencrypt(input("Enter the encrypted message: ")))







