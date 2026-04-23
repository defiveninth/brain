# import matplotlib.pyplot as plt
# import matplotlib

# matplotlib.use("Agg")

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

print(f"w: {w}")
print(f"b: {b}")

for x, y_true in data:
    y_pred = predict(x)

    print(f"{x} hours: {y_pred} points")
    print(f"error: {y_pred - y_true}")

# x_values = [x for x, _ in data]
# y_actual = [y for _, y in data]
# y_predicted = [predict(x) for x in x_values]

# plt.figure(figsize=(8, 5))
# plt.scatter(x_values, y_actual, color="blue", label="Actual (x, y)")
# plt.plot(x_values, y_predicted, color="red", linewidth=2, label="Linear fit")
# plt.xlabel("x (hours)")
# plt.ylabel("y (points)")
# plt.title("Grade Guess v3: Linear Relationship")
# plt.legend()
# plt.grid(True, alpha=0.3)
# plt.tight_layout()
# plt.savefig("output/grade-guess-v3-plot.png")
# print("Saved plot: output/grade-guess-v3-plot.png")
