import sys
if(__name__=="__main__"):
	print ("Moo ba - la la la !!!\n")
	try:
		if(sys.argv[1]=="./shell"):
			print ("Congo!! so you got me, Now what??\n")
			if(raw_input("enter the word which is still a word(9 letter) even when u remove a letter???(always)\n")=="startling"):
				print ("Here is your flag!!  hsCTF{B!NAR!ES_C4N _B_0RE4DFUL}\n")
	except:
		print ("How does a pig do?? - Oink!!\n")
