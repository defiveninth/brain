data = [
	(1, 50),
	(2, 55),
	(3, 65),
	(4, 70),
	(5, 80)
]
w = 10
b = 40

def predict(x):
    return min(w * x + b, 100)

for x, y_true in data:
    y_pred = predict(x)
    error = y_pred - y_true
    
    print(f"x={x}")
    print(f"  predicted: {y_pred}")
    print(f"  actual:    {y_true}")
    print(f"  error:     {error}")
