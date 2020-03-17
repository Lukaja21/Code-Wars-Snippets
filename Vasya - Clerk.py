"""
The new "Avengers" movie has just been released! There are a lot of people at the cinema box office standing in a huge line. Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.
"""

def tickets(people):
	change = {"hundred": 0, "fifty": 0, "twenty-five": 0}
	
	for person in people:
		if person == 100:
			change["hundred"] += 1
			if change["fifty"] >= 1 and change["twenty-five"] >= 1:
				change["fifty"] -= 1
				change["twenty-five"] -= 1

			elif change["twenty-five"] >= 3:
				change["twenty-five"] -= 3

			else:
				return "NO"

		elif person == 50:
			change["fifty"] += 1
			if change["twenty-five"] >= 1:
				change["twenty-five"] -= 1

			else:
				return "NO"

		else:
			change["twenty-five"] += 1

	return "YES"

print(tickets([25, 25, 50, 50, 100]))