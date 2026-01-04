import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('Qt5Agg')  

squares = [1,4,9,16,25]

fig, ax = plt.subplots()
ax.plot(squares,linewidth = 3)
ax.set_title("Square Numbers",fontsize = 24)
ax.set_ylabel("Square of Value",fontsize = 14)
ax.tick_params(labelsize=14)

plt.show(block=True)

plt.show()
plt.tight_layout()
plt.savefig('squares_subplots.png', dpi=150, 
bbox_inches='tight')
print("Plot saved as squares_subplots.png") 