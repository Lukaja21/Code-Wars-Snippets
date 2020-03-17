"""
Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.
Rules for a smiling face:
-Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
-A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
-Every smiling face must have a smiling mouth that should be marked with either ) or D.
No additional characters are allowed except for those mentioned.
"""

def count_smileys(arr):
	faceCount = 0

	for face in arr:
		if face[0] == ":" or face[0]  == ";":
			if face[-1] == "D" or face[-1] == ")":
				if len(face) == 2:
					faceCount += 1
				elif len(face) == 3:
					if face[1] == "-" or face[1] == "~":
						faceCount += 1

	return faceCount

print(count_smileys([':D',':~)',';~D',':)']))