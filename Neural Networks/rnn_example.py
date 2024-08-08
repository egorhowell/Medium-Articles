import torch
import torch.nn as nn
import torch.optim as optim


# RNN Model Definition
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = x.unsqueeze(-1)
        h_0 = torch.zeros(1, x.size(0), self.hidden_size)
        rnn_out, _ = self.rnn(x, h_0)
        out = self.fc(rnn_out[:, -1, :])
        return out


# Dataset
train = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
target = torch.tensor([5], dtype=torch.float32)

# Model Configuration
input_size = 1
hidden_size = 1
output_size = 1
model = SimpleRNN(input_size, hidden_size, output_size)

# Loss and Optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

for epoch in range(1000):
    optimizer.zero_grad()
    output = model(
        train.unsqueeze(0)
    ).squeeze()  # Add batch dimension and squeeze to match target shape
    loss = criterion(output, target)
    loss.backward()
    optimizer.step()


# Function to Predict Next Number
def predict(model, input_seq):
    with torch.no_grad():
        input_seq = torch.tensor(input_seq, dtype=torch.float32).unsqueeze(0)
        output = model(input_seq).squeeze().item()
    return output


# Example Test Set
test = [2, 3, 4]
predicted = predict(model, test)
print(f"Input: {test}, Predicted Next Number: {predicted:.2f}")
