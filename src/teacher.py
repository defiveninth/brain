w = 10
b = 40

# nobody cant get more that 100 points
# render good table from 1 to 10 hours
def predict(x):
	return min(w * x + b, 100)

for i in range(1, 11):
	print(f"{i} hours: {predict(i)} points")
