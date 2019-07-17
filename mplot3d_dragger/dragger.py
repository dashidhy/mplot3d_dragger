class Dragger3D(object):

    def __init__(self, ax, real_time=False, speed=80):
        self.ax = ax
        self.real_time = real_time
        self.speed = speed

        self.cidpress = self.ax.figure.canvas.mpl_connect('key_press_event', self.on_press)
        self.cidrelease = self.ax.figure.canvas.mpl_connect('key_release_event', self.on_release)
        if self.real_time:
            self.cidmotion = self.ax.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)

        self.press = None

    def on_press(self, event):
        if event.inaxes == self.ax and event.key == ' ':
            self.press = (event.xdata, event.ydata)
        return
    
    def on_motion(self, event):
        if self.press is not None and event.inaxes == self.ax:
            self.draw(event)
            self.press = (event.xdata, event.ydata)
        return

    def on_release(self, event):
        if event.inaxes == self.ax and event.key == ' ' and not self.real_time:
            self.draw(event)
        self.press = None
        return

    def draw(self, event):
        dx = (event.xdata - self.press[0]) * self.speed
        dy = (event.ydata - self.press[1]) * self.speed
        old_x_left, old_x_right = self.ax.get_xlim()
        old_y_left, old_y_right = self.ax.get_ylim()
        self.ax.set_xlim(old_x_left - dx, old_x_right - dx)
        self.ax.set_ylim(old_y_left - dy, old_y_right - dy)
        self.ax.figure.canvas.draw()
        return