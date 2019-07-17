# mplot3d_dragger
Allow dragging in matplotlib 3d plots.

## Why this

It seems that dragging is not support by matplotlib when drawing and visualizing 3D plots interactively, though rotating and zooming are supported. This can be very inconvenient when you want to visualize and observe a small part of a 3D plot with large range, e.g., a large point cloud scene. Thus, if you also meet this problem like I do, have a try of this one. 

## Install
```bash
pip install mplot3d-dragger
```

## Usage
```Python
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# import Dragger3D
from mplot3d_dragger import Dragger3D

fig = plt.figure()
ax = Axes3D(fig)

# ... (your plotting) ...

# wrap your axes with Dragger3D
dr = Dragger3D(ax) 
# or for real-time dragging
# dr = Dragger3D(ax, real_time=True)
# but this can be stuttering 
# when you have a lot of objects in one figure

# show()
plt.show()
```

Press SPACE, drag 3D objects by moving your cursor on figure (do not press mouse key), and release SPACE.

# To do list
- Drag alone z axis