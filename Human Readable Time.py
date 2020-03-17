"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
"""

def make_readable(seconds):
	hours = str(int(seconds/3600))
	minutes = str(int((seconds % 3600)/60))
	seconds = str(int((seconds % 3600)%60))

	if 2 > len(hours):
		hours = "0" + hours

	if 2 > len(minutes):
		minutes = "0" + minutes

	if 2 > len(seconds):
		seconds = "0" + seconds

	time = hours + ":" + minutes + ":" + seconds

	return time

print(make_readable(86399))