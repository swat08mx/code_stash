

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
         encryption = encryption + "?"
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

def decrypt(phase):
   decryption = ""
   for letter in phase:
      if letter in "!":
         decryption = decryption + "a"
      elif letter in "J":
         decryption = decryption + "b"
      elif letter in "2":
         decryption = decryption + "c"
      elif letter in "?":
         decryption = decryption + "d"
      elif letter in "6":
         decryption = decryption + "e"
      elif letter in "^":
         decryption = decryption + "f"
      elif letter in "&":
         decryption = decryption + "g"
      elif letter in "*":
         decryption = decryption + "h"
      elif letter in "q":
         decryption = decryption + "i"
      elif letter in "8":
         decryption = decryption + "j"
      elif letter in "$":
         decryption = decryption + "k"
      elif letter in "3":
         decryption = decryption + "l"
      elif letter in "7":
         decryption = decryption + "m"
      elif letter in "t":
         decryption = decryption + "n"
      elif letter in "9":
         decryption = decryption + "o"
      elif letter in "Q":
         decryption = decryption + "p"
      elif letter in "-":
         decryption = decryption + "q"
      elif letter in "%":
         decryption = decryption + "r"
      elif letter in "4":
         decryption = decryption + "s"
      elif letter in "#":
         decryption = decryption + "t"
      elif letter in "/":
         decryption = decryption + "u"
      elif letter in "B":
         decryption = decryption + "v"
      elif letter in ">":
         decryption = decryption + "w"
      elif letter in "f":
         decryption = decryption + "x"
      elif letter in "h":
         decryption = decryption + "y"
      elif letter in "r":
         decryption = decryption + "z"
   
   return decryption
   
print(decrypt(input("Enter the encrypted message: ")))







