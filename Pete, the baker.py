def cakes(recipe, available):
	iterations = []

	for item in recipe:
		if item in available:
			iterations.append(int(available[item]/recipe[item]))
        
		else:
			print(item)
			return 0

	return min(iterations)
	
print(cakes({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}))