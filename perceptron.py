class Perceptron():
    def __init__(self, num_features):
        self.weights = [random.random() * 2 -1 for i in range(num_features)]
        self.bias = 0

    def forward(self, x:list):
        linear = 0
        linear = self.weights[0] * x[0] + self.weights[1] * x[1]+ self.bias
        if linear >= 0:
            prediction = 1
        else:
            prediction = 0
        return prediction
        
    def backward(self, x:list, y:float):
        # <your code> to compute the pr(ediction error
        errors =y - self.forward(x)
        return errors
    
    def train(self,x:list,y:list,epochs:int):
        # epochs 만큼 학습
        for e in range(epochs):
            # 데이터 하나씩 학습
            for i in range(len(y)):
                update = self.backward(x[i],y[i])
        
                self.weights[0] = self.weights[0] + update*x[i][0]
                self.weights[1] = self.weights[1] + update*x[i][1]
        
                self.bias = self.bias + update
                
    def evaluate(self,x:list,y:list)->float:
        count = 0
        for i in range(len(x)):
            if(y[i] == self.forward(x[i])):
                count += 1
        accuracy = float(count/len(x))
        return accuracy
