# doing the same using pytorch

import torch

data = [
    (1, 50),
    (2, 55),
    (3, 65),
    (4, 70),
    (5, 80),
]

x_train = torch.tensor([[x] for x, _ in data], dtype=torch.float32)
y_train = torch.tensor([[y] for _, y in data], dtype=torch.float32)

print (f"x_train: {x_train}")
print (f"y_train: {y_train}")

model = torch.nn.Linear(1, 1)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

for epoch in range(100000):
	y_pred = model(x_train)
	loss = criterion(y_pred, y_train)

	optimizer.zero_grad()
	loss.backward()

	optimizer.step()

w = model.weight.item()
b = model.bias.item()

print(f"w: {w}")
print(f"b: {b}")

for x, y_true in data:
    x_tensor = torch.tensor([[x]], dtype=torch.float32)
    y_pred = model(x_tensor).item()

    print(f"{x} hours: {y_pred}")
    print(f"error: {y_pred - y_true}")