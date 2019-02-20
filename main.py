import crypt

def testPass(cryptP):
  salt=cryptP[0:2]
  dicti=open("dictionary.txt", 'r')
  for word in dicti.readlines():
    word=word.strip("\n")
    cryptWord=crypt.crypt(word, salt)
    if (cryptWord == cryptP):
      print("[+] Found Password: ", word, "\n")
      return
  
  print("[-] Password Not Found. \n")
  return

def main():
  passF = open('passwords.txt')
  for line in passF.readlines():
    if ":" in line:
      user = line.split(":")[0]
      cryptP = line.split(':')[1].strip(' ')
      print("[*] Cracking Password For: ", user)
      testPass(cryptP)
  passF.close()

if __name__ == '__main__':
  main()
