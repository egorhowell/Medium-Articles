# Import the required libraries
import torch
import torch.nn as nn
import torch.optim as optim


# Define a custom neural network model using nn.Module
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden_layer = nn.Linear(2, 2)
        self.output_layer = nn.Linear(2, 1)

    def forward(self, x):
        x = self.hidden_layer(x)
        x = torch.relu(x)
        x = self.output_layer(x)
        return x


# Define the inputs and true target
inputs = torch.tensor([[0.9, 1.0]], requires_grad=False)
target = torch.tensor([[2.0]], requires_grad=False)

# Initialise the neural network
model = NeuralNetwork()

# Set the initial weights and biases
model.hidden_layer.weight.data = torch.Tensor([[0.2, 0.3], [0.4, 0.5]])
model.hidden_layer.bias.data = torch.Tensor([0.1, 0.2])
model.output_layer.weight.data = torch.Tensor([[0.5, 0.6]])
model.output_layer.bias.data = torch.Tensor([0.4])

# Define the Mean Squared Error loss
criterion = nn.MSELoss()

# Set the learning rate
learning_rate = 0.1

# Create the optimiser
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Perform the first forward pass
output = model(inputs)
loss = criterion(output, target)

# Perform the backward pass
optimizer.zero_grad()
loss.backward()

# Update the network parameters
optimizer.step()

# Perform the forward pass for update values
output = model(inputs)


