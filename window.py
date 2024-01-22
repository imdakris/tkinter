from tkinter import *
from child_window import ChildWindow


class Window:
    """Window Options Builder"""

    def __init__(
        self,
        width: int,
        height: int,
        title="MyWindow",
        resizable=(False, False),
        icon=None,
    ):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

        self.label = Label(
            self.root,
            text="I'm label",
            bg="#4efc03",
            relief="ridge",
            wraplength=50,
            font="Consolas 15",
        )

    def run(self):
        """Launches a window"""
        self.draw_widgets()
        self.root.mainloop()

    def draw_widgets(self):
        self.label.pack(anchor=NW, padx=20, pady=70)

    def create_child(
        self, width, height, title="Child", resizable=(False, False), icon=None
    ):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "Tkinter")
    # window.create_child(200, 100)

    window.run()
