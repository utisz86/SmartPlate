import tkinter as tk


# Main application 
class MainApplication(tk.Frame):
    """[This class holds together the whole application]

    Args:
        tk ([type]): [Tkinter Frame class]
    """
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
        