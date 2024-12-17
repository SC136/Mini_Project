import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class bar:
    def __init__(self,data):
        self.data=data

    def plot_sales(self):
        sns.barplot(x='region', y='sales', data=self.data, color='skyblue')
        plt.xlabel('Region')
        plt.ylabel('Sales')
        plt.show()
        
class line:
    def __init__(self,data):
        self.data=data
    
    def line(self):
        sns.lineplot(x='day',y='temp',data=self.data)
        plt.xlabel('Day')
        plt.ylabel('Temp')
        plt.show()

        
        

data=pd.read_csv(r'd:\Downloads\sales.csv')
a=bar(data)
a.plot_sales()

temp=pd.read_csv(r'd:\Downloads\temp.csv')
b=line(temp)
b.line()