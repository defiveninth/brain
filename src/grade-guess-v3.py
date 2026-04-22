w = 10
b = 40
data = [
    (1, 50),
    (2, 55),
    (3, 65),
    (4, 70),
    (5, 80),
]


def predict(x):
    return w * x + b


for epoch in range(100):
    for x, y_true in data:
        y_pred = predict(x)
        error = y_pred - y_true

        w -= 0.001 * error * x
        b -= 0.001 * error

        if (epoch % 10 == 0):
            print(f"epoch: {epoch}")
            print(error)

print(f"w: {w}")
print(f"b: {b}")

for x, y_true in data:
    y_pred = predict(x)

    print(f"{x} hours: {y_pred} points")
    print(f"error: {y_pred - y_true}")
