from tkinter import *


class Window:
    def __init__(
        self,
        width: int,
        height: int,
        title="MyWindow",
        resizable=(False, False),
        icon=None,
    ) -> None:
        """Window Options Builder"""
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        """Launches a window"""
        self.root.mainloop()


