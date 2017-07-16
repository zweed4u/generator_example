#!/usr/local/bin/python3
'''
Credit to ThatJuanGuy on se7en sins for original redbull script

xxx-xxx-xxx format
Uses the valid format for |3ung1e codes
TODO: further investigation needed - does not always produce working tokens
Check positional substr validation
'''
from random import sample, shuffle, randint
from itertools import repeat
for i in repeat(None, 5): #(None, <How many to be generated>)
	numbers = ['3','4','6','7','9'] # 3 4 7 - put acceptable numbers here
	letters = ['A','C','D','F','G','H','J','K','L','M','N','P','R','T','V','X','Y'] # C K R V - put acceptable chars here
	num_of_numbers_in_str = randint(0,9)
	num_of_chars_in_str = (9 - num_of_numbers_in_str) # must be exactly 9 chars
	quest = sample(letters,num_of_chars_in_str)+sample(numbers*3,num_of_numbers_in_str)  # (letters, <number of letters to be in str>). (numbers*3, <number of numbers to be in str>))
	shuffle(quest)
	index_counter=0
	for char in quest:
		if index_counter==0:
			pass
		elif index_counter%3==0:
			print('-',end='')
		print(char,end='')
		index_counter+=1
	print()

'''
GHC-NJM-T7A
YD4-YYN-DHY
FAM-MYJ-XTG
7PX-JLM-74R
6FY-L7A-FRX
G7T-FNV-7NR
VH7-JKD-7CH
JNK-9NL-HMJ
743-DC9-4FK
K9M-6M3-CVT
J7P-7RG-LPX
MTT-AA4-RGY
MCY-FVM-YC4
GDL-JVY-NA7
FTF-L73-TYM
MHC-NDT-RFR
CFJ-AYC-TRY
79Y-VJF-NF3
J99-H4J-DFT
ALL-9LJ-N94.     A J L N 4 9
76A-JKK-9DY.     A D J K Y 6 7 9
9GC-F4L-DJA.     A C D F G J L 4 9
XCG-LN8-PLF.     C F G L N P X 8  invalid - no 8 (4+4)
7A4-VM3-K67.     A K M V 3 4 6 7
PKP-HPX-RD3.     D H K P R X 3
9R3-RGA-G34.     A G R 3 4 9
GAN-LYJ-TJG.     A G J L N T Y
LM4-6AM-RKV.     A K L M R V 4 6
R6T-G33-Y4R.     G R T Y 3 4 6
HD4-P43-RXP      D G H P R X 3 4
Y43-YKR-KVV.     K R V Y 3 4
MPD-CHC-TKV.     C D H K M P T V
R96-H3L-HC6.     C H L R 3 6 9
RHG-ACX-NJR.     A C G H J N R X
9VC-PY6-FH3.     C F H P V Y 3 6 9
VN7-V6L-AL7.     A L N V 6 7
6K6-V4D-VK6.     D K V 4 6
PAR-HKA-HRX.     A H K P R X
FFP-FXG-9L4.     F G L P X 4 9
AMN-TPJ-VHV.     A H J M N P T V
3TH-TN9-M4R.     H M N R T 3 4 9
LLA-XPY-3RC      A C L P R X Y 3
AGJ-6ND-F6P.     A D F G J N P 6
M3J-VMC-9L4.     C J L M V 3 4 9
3XR-FN6-DTC.     C D F N X R 3 6
'''