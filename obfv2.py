import sys
import os
import base64
code = ""
os.system ("clear")
os.system ("sleep 0.50")
print (''' \033[92m
=================================
       .---.        .-----------
      /     \  __  /    ------
     / /     \(  )/    -----
    //////   ' \/ `   ---
   //// / // :    : ---
  // /   /  /`    '--
 //          //..\\
        ====UU====UU====
            '//||\\`
              ''``
=================================
           OBFUSCATEV2
      Creator By CyruxXsec
          Official Team :
         MCT - MCX - IDC
==================================
 ''')
print ("OBFUSCATE adalah tools untuk merubah")
os.system ("sleep 0.15")
print ("codingan menjadi Sulit dipahami!")
os.system ("sleep 0.15")
print ("[ 1 ] OBF untuk php")
os.system ("sleep 0.15")
print ("[ 2 ] OBF untuk python")
os.system ("sleep 0.15")
print ("[ 0 ] EXIT")
pilih = input("masukan pilihan anda : ")
if pilih == 1:
		print ("contoh file.php")
		try:
			file = raw_input("nama file yang mau di obfuscate : ")
			code = open(file,"r").read()
		except IOError :
			print ("[!] FILE TIDAK ADA!!!")
			sys.exit()
		rep = str(code).replace ("<?php","").replace ("?>","")
		enc = base64.b64encode(rep)
		data = """<?php
//    OBFUSCATED BY CyruxXsec
eval(base64_decode('%s'));
?>"""%(enc)
		out = raw_input("OUT : ")
		open(out,"w").write(data)
elif pilih == 2:
		try:
			file1 = raw_input("nama file yang mau di obfuscate : ")
			baca = open(file1,"r").read()
		except IOError :
			print ("[!] FILE TIDAK ADA!!!")
			sys.exit()
		encrypt = base64.b64encode(baca)

		baru = open("obf_"+str(file1),"w")
		baru.write ("import base64 \n")
		baru.write ('exec(base64.b64decode("'+str(encrypt)+'"))')
		print ("success | file save as obf_"+str(file1))
else:
	print ("TERIMA KASIH TELAH MENGGUNAKAN TOOLS INI!")
	os.system("sleep 1")
	print ("TODD :v")
	sys.exit()