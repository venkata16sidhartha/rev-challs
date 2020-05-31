
import sys
if(__name__=="__main__"):
	try:
		 import pydevd
    		 DEBUGGING = True
	except ImportError:
    		 DEBUGGING = False
	if(DEBUGGING==True):
		exit()
	data=["e4da3b7fbbce2345d7772b0674a318d5","69691c7bdcc3ce6d5d8a1361f22d04ac","e1e1d3d40573127e9ee0480caf1283d6","8f14e45fceea167a5a36dedd4bea2543","b14a7b8059d9c055954c92674ce60032","0d61f8370cad1d412f80b84d143e1257","CFCD208495D565EF66E7DFF9F98764DA","8D9C307CB7F3C4A32822A51922D1CEAA","800618943025315F869E4E1F09471012","9033E0E305F247C0C3C80D0C7848C8B3","DFCF28D0734569A6A693BC8194DE62BF"]
	print len(data)	
	print ("Usage: ./rev  <flag-part-1> <flag-part-2>")
	try:
		if(sys.argv[1]=="hsCTF{" and sys.argv[2]=="}"):
			print ("".join(data))
			exit()
	except:
		print ("")

