import matplotlib.pyplot as plt
import pandas as pd

x = [0,2,4,6,8,10,12,14,16]
y = [0,4,16,36,64,100,144,196,256]

#plt.plot(x,y)
plt.title("Example data - Line plot")
#print(plt.show())

#plt.scatter(x,y)
plt.title("Example data - Line plot")
#print(plt.show())

#plt.bar(x,y)
plt.title("Example data - Line plot")
#print(plt.show())
'''
fig = plt.figure(figsize =(18,5))
first_plot = fig.add_subplot(1,3,1)
first_plot.plot(x,y,color ="red")
first_plot.set_title("Example data - Line plot")
second_plot = fig.add_subplot(1,3,2)
second_plot.scatter(x,y, color ="green")
second_plot.set_title("Example data - Line plot")
third_plot = fig.add_subplot(1,3,3)
third_plot.bar(x,y,color = "orange")
third_plot.set_title("Example data - Line plot")
print(plt.show())
'''
data = pd.read_csv("employee_performance.csv")
print(data.head())
educational_level = data["Education"].value_counts()
print(educational_level)

#plt.pie(educational_level,labels=educational_level.index)
#print(plt.show())

plt.bar(data["Name"], data["Revenue"])
print(plt.show())
'''
plt.bar(data["Name"],data["Revenue"],label = "Revenues")
plt.bar(data["Name"],data["Number of calls"],label = "Number of calls")
plt.legend()
plt.grid()
print(plt.show())
'''