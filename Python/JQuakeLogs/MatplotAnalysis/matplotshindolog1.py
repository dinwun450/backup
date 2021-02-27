import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
shindo = ['S1', 'S2', 'S3', 'S4']
count = [15,8,4,1]
ax.bar(shindo,count)
plt.show()