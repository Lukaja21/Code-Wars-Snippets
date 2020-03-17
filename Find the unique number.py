"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

def find_uniq(arr):
	uniqueDict = {}
	for item in arr:
		if item in uniqueDict:
			uniqueDict[item] += 1
		else:
			uniqueDict[item] = 1

	for item in arr:
		if item != max(uniqueDict, key=uniqueDict.get):
			return item

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))