import matplotlib.pyplot as plt
x_values=[1,2,3,4,5,6,7]
y_values =[1,4,9,16,25,36,56]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values,y_values,s=200, marker='*')
# ax.scatter(2,4, s=200)

#set chart title and label axes.
ax.set_title("Sueare number of ", fontsize= 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Squares of values", fontsize = 14)

#Set size to tick labels.
ax.tick_params(axis= 'both', which='major', labelsize=14)



plt.show()
