import tkinter as tk
import tkinter.ttk as ttk
import webbrowser


# create window
class ThumbGet(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ThumbGet v0.0.1")
        self.resizable(width=False, height=False)
        self.geometry("300x200+500+50")
        self.setup_ui()


    def setup_ui(self):

        # set ui stuff up

        frame = tk.Frame(self)

        # begin horrible code

        def return_press(event):
            user_id = enterid.get()
            print("Opening ID", user_id) 
            
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/sddefault.jpg")

            print("Opened page, success")

        tk.Label(self, text="Youtube Thumbnail Downloader (ThumbGet)").pack()

        enterid = tk.Entry(self)
        enterid.insert(0, "Enter Youtube ID")
        enterid.bind("<Return>", return_press)
        enterid.pack(padx=2, pady=2, fill="x")
        
        
if __name__ == "__main__":
    pro = ThumbGet()
    pro.mainloop()