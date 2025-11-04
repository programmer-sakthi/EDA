import matplotlib.pyplot as plt

# create a plot
plt.plot([1,2,3,4], [1,4,9,16])
plt.show()

# customize the plot
plt.plot([1,2,3,4], [1,4,9,16], 'ro')  # red circles
plt.title('Square Numbers')
plt.xlabel('Value')
plt.ylabel('Square')
plt.grid(True)
plt.show()

# plotting multiple sets of data
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.plot([1,2,3,4], [1,8,27,64], 'bx')
plt.legend(['Square', 'Cube'])
plt.show()

# plotting data from a list
data = [1, 2, 3, 4, 5]
plt.plot(data)
plt.show()

# plotting a scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.show()

# plotting a bar chart
labels = ['A', 'B', 'C', 'D', 'E']
values = [10, 20, 30, 40, 50]
plt.bar(labels, values)
plt.show()

# plotting a histogram
data = [1, 2, 3, 4, 5, 6]
plt.hist(data)
plt.show()

# plotting a box plot
data = [1, 2, 3, 4, 5, 6]
plt.boxplot(data)
plt.show()

# plotting a line with error bars
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
yerr = [0.5, 1, 0.5, 1, 0.5]
plt.errorbar(x, y, yerr=yerr, fmt='o')
plt.show()

# plotting a line with markers and error bars
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
yerr = [0.5, 1, 0.5, 1, 0.5]
plt.errorbar(x, y, yerr=yerr, fmt='o', markersize=10)
plt.show()

# plotting subplots
fig, axs = plt.subplots(2, 2)
axs[0,0].plot([1,2,3,4], [1,4,9,16])
axs[0,1].scatter([1,2,3,4], [1,4,9,16])
axs[1,0].bar([1,2,3,4], [1,4,9,16])
axs[1,1].hist([1,2,3,4,5,6])
plt.show()


# saving a plot to a file
plt.plot([1,2,3,4], [1,4,9,16])
plt.savefig('plot.png')
