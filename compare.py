import json
import string
import re

with open('ViveWordDict.txt','r') as file1:
	dict1 = json.load(file1)

with open('occulusdict.txt','r') as file2:
	dict2 = json.load(file2)

diff = dict()
for key in dict1:
	if key not in dict2:
		diff[key]=dict1[key]

json = json.dumps(diff)
f = open('diff.txt', 'w')
f.write(json)
f.close
#distinct_word = {k: dict1[k] for k in set(dict1)-set(dict2)}
#with open('distin.txt', 'w') as f:
#	json.dump(diff, f)
