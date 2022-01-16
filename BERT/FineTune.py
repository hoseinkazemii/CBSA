from transformers import AutoModel
import torch




class FineTune(nn.Module):
		
    def __init__(self, bert, checkpoint):
      
      super(FineTune, self).__init__()

      self.bert = bert 
      self.dropout = nn.Dropout(0.1)     
      self.relu =  nn.ReLU()
      self.fc1 = nn.Linear(768,512)     
      self.fc2 = nn.Linear(512,1)
      self.sigmoid = nn.Sigmoid()

    def forward(self, sent_id, mask):

      #pass the inputs to the model  
      _, X = self.bert(sent_id, attention_mask = mask)
      
      X = self.fc1(X)

      X = self.relu(X)

      X = self.dropout(X)

      # output layer
      X = self.fc2(X)
      
      # apply softmax activation
      X = self.sigmoid(X)

      return X



	bert = AutoModel.from_pretrained('bert-base-uncased')
