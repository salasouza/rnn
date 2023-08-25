# step 1: importing libraries  
import torch 
import torch.nn as nn

#step 3: creATING THE MODEL
class LSTMModel(nn.Module):
    def __init__(self, input_d, hidden_d, layer_d, output_d):
        super(LSTMModel, self).__init__()
        
        self.hidden_dim = hidden_d
        self.layer_dim = layer_d

        # LSTM model 
        self.lstm = nn.LSTM(input_d, hidden_d, layer_d, batch_first=True) 

        self.fc = nn.Linear(hidden_d, output_d)

    def forward(self, x):
    
        h0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()

        c0 = torch.zeros(self.layer_dim, x.size(0), self.hidden_dim).requires_grad_()

        out, (hn, cn) = self.lstm(x, (h0.detach(), c0.detach()))

        out = self.fc(out[:, -1, :]) 
        return out
    
input_dim = 30
hidden_dim = 120
output_dim = 15
layer_dim = 1

model = LSTMModel(input_dim, hidden_dim, layer_dim, output_dim)

#step 4: calculating cross entropy loss
error = nn.CrossEntropyLoss()

#step 5: optimizer 
learning_rate = 0.1
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)