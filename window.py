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
        # self.root.geometry(f"{width}x{height}+200+200")
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
        # self.label.pack(anchor=NW, padx=20, pady=70)
        top_frame = LabelFrame(self.root, text="Top frame")
        bottom_frame = LabelFrame(self.root, text="Bottom frame")
        top_frame.pack(padx=10, pady=10)
        bottom_frame.pack(ipadx=10, ipady=10)
        Label(top_frame, width=30, height=2, bg="red", text="First").pack(side="left", padx=10)
        Label(top_frame, width=30, height=2, bg="orange", text="Second").pack(
            side="left"
        )
        Label(bottom_frame, width=30, height=2, bg="yellow", text="Third").pack(
            side="left"
        )
        Label(bottom_frame, width=30, height=2, bg="green", text="Fourth").pack(
            side="left"
        )

    def create_child(
        self, width, height, title="Child", resizable=(False, False), icon=None
    ):
        ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
    window = Window(500, 500, "Tkinter")
    # window.create_child(200, 100)

    window.run()
