# Imagine GUI programming for Linux, Windows and OSX
# Every Window can have a border (bordered) or not (plain)
# It is then easy to end up with following classes:

class MacPlainWindow:
    pass

class LinuxPlainWindow:
    pass

class WindowsPlainWindow:
    pass

class MacBorderedWindow:
    pass

class LinuxBorderedWindow:
    pass

class WindowsBorderedWindow:
    pass


class WindowsManager:
    def __init__(self):
        if os == 'Linux' and border == 'bordered':
            self.window = LinuxBorderedWindow()
        ...


# Better

class BorderedDrawer:
    def __init__(self, window):
        self.window = window
    def draw(self):
        self.window.createBorder()
        self.window.createBody()
        ...

class PlainDrawer:
    def __init__(self, window):
        self.window = window
    def draw(self):
        self.window.createBody()
        ...


class MacWindow:
    pass

class WindowsWindow:
    pass

class LinuxWindow:
    pass


class WindowManager:
    def __init__():
        if os == 'linux':
            window = LinuxWindow()
        elif os == 'mac':
            ...

        if border == 'bordered':
            drawer = BorderedDrawer(window)
        else:
            drawer = PlainDrawer(window)
