import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axes for the plot
fig, ax = plt.subplots()

# Set the axis labels and limits
ax.set_xlabel('Time (s)')
ax.set_ylabel('CPU usage (%)')
ax.set_ylim(0, 100)

# Initialize the plot
line, = ax.plot([], [], lw=2)

# Create a function to update the plot
def update_plot(frame):
    # Get the current CPU usage and time
    cpu_percent = psutil.cpu_percent()
    current_time = frame / 10.0
    
    # Add the new data point to the plot
    line.set_xdata(list(line.get_xdata()) + [current_time])
    line.set_ydata(list(line.get_ydata()) + [cpu_percent])
    
    # Update the plot title with the current CPU usage
    ax.set_title(f"Current CPU usage: {cpu_percent}%")
    
    # Only show the last 10 seconds of data in the plot
    ax.set_xlim(max(0, current_time - 10), current_time)
    
    return line,

# Create an animation using the update_plot function and a 100ms interval
ani = animation.FuncAnimation(fig, update_plot, interval=100)

# Show the plot
plt.show()
