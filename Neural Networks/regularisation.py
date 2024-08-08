import plotly.graph_objects as go
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from torch.utils.data import DataLoader, TensorDataset


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.input_layer = nn.Linear(4, 10)
        self.output_layer = nn.Linear(10, 3)

    def forward(self, x):
        x = torch.relu(self.input_layer(x))
        x = self.output_layer(x)
        return x


# Training function
def train_one_epoch(model, data_loader, optimiser, criterion):
    model.train()
    for inputs, targets in data_loader:
        optimiser.zero_grad()
        preds = model(inputs)
        loss = criterion(preds, targets)
        loss.backward()
        optimiser.step()


# Validation function
def validate(model, data_loader, criterion):
    model.eval()
    total_loss = 0
    with torch.no_grad():
        for inputs, targets in data_loader:
            preds = model(inputs)
            loss = criterion(preds, targets)
            total_loss += loss.item()
    return total_loss / len(data_loader)


# Main Training Function with Early Stopping
def train_model(
    model, train_loader, val_loader, optimiser, criterion, epochs, patience
):
    best_val_loss = float("inf")
    epochs_no_improve = 0
    train_losses = []
    val_losses = []
    early_stop = 0

    for epoch in range(epochs):
        train_loss = 0
        for inputs, targets in train_loader:
            optimiser.zero_grad()
            preds = model(inputs)
            loss = criterion(preds, targets)
            loss.backward()
            optimiser.step()
            train_loss += loss.item()
        train_loss /= len(train_loader)
        train_losses.append(train_loss)

        # Get the validation dataset loss
        val_loss = validate(model, val_loader, criterion)
        val_losses.append(val_loss)

        # Early stopping check
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1
        if epochs_no_improve == patience:
            early_stop = epoch + 1
            break

    # Plot the early stopping
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(range(1, epochs)), y=train_losses, mode="lines", name="Training Loss"
        )
    )
    fig.add_trace(
        go.Scatter(
            x=list(range(1, epochs)), y=val_losses, mode="lines", name="Validation Loss"
        )
    )

    if early_stop:
        fig.add_vline(x=early_stop, line_width=3, line_dash="dash", line_color="red")
        fig.add_annotation(
            x=early_stop,
            y=max(max(train_losses), max(val_losses)),
            text="Early Stopping",
            showarrow=True,
            arrowhead=1,
            ax=-50,
            ay=-100,
        )

    fig.update_layout(
        title="Early Stopping Example",
        xaxis_title="Epoch",
        yaxis_title="Loss",
        template="plotly_white",
        width=900,
        height=600,
        font=dict(size=18),
        xaxis=dict(tickfont=dict(size=16)),
        yaxis=dict(tickfont=dict(size=16)),
        title_font_size=24,
    )
    fig.show()

    return train_losses, val_losses


# Load and split the data
iris = load_iris()
X = iris.data
y = iris.target
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalise the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)

# Convert the data into PyTorch Tensors
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
X_val_tensor = torch.tensor(X_val, dtype=torch.float32)
y_val_tensor = torch.tensor(y_val, dtype=torch.long)

# Load the data into PyTorch DataLoaders to allow mini-batch training
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True)
val_loader = DataLoader(val_dataset, batch_size=8)

# Model initialisation
model = Model()
optimiser = optim.Adam(model.parameters(), lr=0.001)
criterion = nn.CrossEntropyLoss()

# Train and visualise results
train_losses, val_losses = train_model(
    model, train_loader, val_loader, optimiser, criterion, epochs=800, patience=10
)
