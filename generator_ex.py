#!/usr/local/bin/python3
'''
Credit to ThatJuanGuy on se7en sins for original redbull script

xxx-xxx-xxx format
Uses the valid format for |3ung1e codes
TODO: further investigation needed,
	Automated implementation:
		https://www.bungie.net/Platform/Tokens/ClaimAndApplyToken/0/
		headers={} #include login cookie or post xbl/psn credentials in setup
		params={'lc':'en', 'fmt':'true', 'lcin':'true'}
		json={<valid_code_here>}
Does not always produce working tokens
Can/Will result in token throttling - with multiple failed attempts - not ip/cookie based - your account
Check positional substr validation
'''
from random import sample, shuffle, randint
from itertools import repeat
invalids_chars = ['B','E','8','I','1','O','Q','0','S','5','U','W','Z','2'] # grabbed from https://www.bungie.net/Scripts/bungienet/coderedemption/coderedemption.js
valid_codes = [
	'9GC-F4L-DJA',     #A C D F G J L 4 9
	'VMC-JF6-AJJ',     #A C F J M V 6
	'CFJ-AYC-TRY',     #A C F J R T Y
	'GHC-NJM-T7A',     #A C G H J M N T 7
	'RHG-ACX-NJR',     #A C G H J N R X
	'JKC-AGX-7JK',     #A C G J K X 7
	'LLA-XPY-3RC',     #A C L P R X Y 3
	'AGJ-6ND-F6P',     #A D F G J N P 6
	'GDL-JVY-NA7',     #A D G J L N V Y 7 
	'76A-JKK-9DY',     #A D J K Y 6 7 9
	'7DL-9TN-A7V',     #A D L N T V 7 9
	'FAM-MYJ-XTG',     #A F G J M T X Y
	'7TH-VFA-LN6',     #A F H L N T V 6 7
	'AMP-TTM-LAF',     #A F L M P T
	'6FY-L7A-FRX',     #A F L R X Y 6 7 
	'GAN-LYJ-TJG',     #A G J L N T Y
	'MTT-AA4-RGY',     #A G M R T Y 4
	'9R3-RGA-G34',     #A G R 3 4 9
	'AMN-TPJ-VHV',     #A H J M N P T V
	'PAR-HKA-HRX',     #A H K P R X
	'ALL-9LJ-N94',     #A J L N 4 9
	'LM4-6AM-RKV',     #A K L M R V 4 6
	'7A4-VM3-K67',     #A K M V 3 4 6 7
	'9LR-AX9-AAN',     #A L N R X 9
	'VN7-V6L-AL7',     #A L N V 6 7

	'MHC-NDT-RFR',     #C D F H M N R T
	'743-DC9-4FK',     #C D F K 3 4 7 9
	'3XR-FN6-DTC',     #C D F N X R 3 6
	'MPD-CHC-TKV',     #C D H K M P T V
	'VH7-JKD-7CH',     #C D H J K V 7
	'7T7-VXN-LDC',     #C D L N T V X 7
	#XCG-LN8-PLF,      #C F G L N P X 8  invalid - no 8 (4+4)
	'C6X-CFR-K7M',     #C F K M R X 6 7
	'9VC-PY6-FH3',     #C F H P V Y 3 6 9
	'FTV-XX4-CM6',     #C F M T V X 4 6
	'MCY-FVM-YC4',     #C F M V Y 4
	'R96-H3L-HC6',     #C H L R 3 6 9
	'M3J-VMC-9L4',     #C J L M V 3 4 9
	'K9M-6M3-CVT',     #C K M T V 3 6 9

	'J99-H4J-DFT',     #D F H J T 4 9
	'HD4-P43-RXP',     #D G H P R X 3 4
	'4DJ-K7H-9L7',     #D H J K L 4 7 9
	'PKP-HPX-RD3',     #D H K P R X 3
	'YD4-YYN-DHY',     #D H N Y 4
	'V7K-3J3-P4D',     #D J K P V 3 4 7
	'JTX-YD3-9TX',     #D J X T Y 3 9
	'6K6-V4D-VK6',     #D K V 4 6
	'L6D-4VT-7XY',     #D L T V X Y 4 6 7
	'NFN-LVH-4RG',     #F G H L N V R 4
	'FFP-FXG-9L4',     #F G L P X 4 9
	'G7T-FNV-7NR',     #F G N R T V 7
	'79Y-VJF-NF3',     #F J N V Y 3 7 9
	'FTF-L73-TYM',     #F L M T Y 3 7

	'7VH-JHT-YGY',     #G H J T V Y 7
	'J7P-7RG-LPX',     #G J L P R X 7
	'R6T-G33-Y4R',     #G R T Y 3 4 6

	'JNK-9NL-HMJ',     #H J K L M N 9
	'3TH-TN9-M4R',     #H M N R T 3 4 9

	'7PX-JLM-74R',     #J L M P R X 4 7

	'Y43-YKR-KVV'      #K R V Y 3 4
]

numbers = ['3','4','6','7','9'] # 3 4 7 - put acceptable numbers here
letters = ['A','C','D','F','G','H','J','K','L','M','N','P','R','T','V','X','Y'] # C K R V - put acceptable chars here

for code in valid_codes: # ensures that previous codes are valid, this is redundant in that conditions were originally derived form the list but helps with future code additions/requirements 
	for char in code.replace('-',''):
		assert char in letters or char in numbers, "{0} has a '{1}' in it but {0} is not in the valid characters list".format(code, char)
		assert char not in invalids_chars, "{0} has a '{1}' in it but '{1}' is in the invalid characters list".format(code,char)

for i in repeat(None, 5): #(None, <How many to be generated>)
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
