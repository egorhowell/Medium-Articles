# Import packages
import torch
from torchvision import datasets, transforms
from hyperopt import fmin, tpe, hp, STATUS_OK, Trials


def get_data(batch_size):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,))
    ])

    train_dataset = datasets.MNIST('./data', train=True, download=True, transform=transform)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    return train_loader


class Model(torch.nn.Module):
    def __init__(self, layers, neurons):
        super(Model, self).__init__()
        self.layers = torch.nn.ModuleList()
        input_dim = 784  # MNIST images are 28x28 pixels
        for i in range(layers):
            self.layers.append(torch.nn.Linear(input_dim, neurons))
            input_dim = neurons
        self.out_layer = torch.nn.Linear(neurons, 10)  # 10 digits

    def forward(self, x):
        x = x.view(-1, 784)
        for layer in self.layers:
            x = torch.relu(layer(x))
        x = self.out_layer(x)
        return torch.nn.functional.log_softmax(x, dim=1)


def objective(params):
    batch_size = params['batch_size']
    learning_rate = params['learning_rate']
    layers = params['layers']
    neurons = params['neurons']

    train_loader = get_data(batch_size)
    model = Model(layers, neurons)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    # Foward and backward pass
    for epoch in range(5):
        for data, target in train_loader:
            optimizer.zero_grad()
            output = model(data)
            loss = torch.nn.functional.nll_loss(output, target)
            loss.backward()
            optimizer.step()

    return {'loss': loss.item(), 'status': STATUS_OK}


# Define the space of hyperparameters to search
search_space = {
    'batch_size': hp.choice('batch_size', [32, 64, 128, 256]),
    'learning_rate': hp.loguniform('learning_rate', -5, 0),  # 10^-5 to 10^0
    'layers': hp.choice('layers', [1, 2, 3, 4]),
    'neurons': hp.choice('neurons', [64, 128, 256, 512])
}

# Run the optimizer
trials = Trials()
best = fmin(objective, search_space, algo=tpe.suggest, max_evals=10, trials=trials)
print(best)
