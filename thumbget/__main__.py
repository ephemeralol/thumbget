import tkinter as tk
import tkinter.ttk as ttk
import webbrowser



# create window
class ThumbGet(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ThumbGet")
        self.resizable(width=False, height=False)
        self.geometry("300x200+500+50")
        self.setup_ui()

    def setup_ui(self):

        # set ui stuff up

        frame = tk.Frame(self)

        # begin horrible code


        tk.Label(self, text="Youtube Thumbnail Downloader (ThumbGet)").pack()

        enterid = tk.Entry(self)
        enterid.insert(0, "Enter Youtube ID")
        enterid.pack(padx=2, pady=2, fill="x")

        def maxres():
            user_id = enterid.get()
            print("Opening ID Maxres", user_id) 
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/maxresdefault.jpg")

        def sd():
            user_id = enterid.get()
            print("Opening ID SD", user_id) 
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/sddefault.jpg")

        def hqd():
            user_id = enterid.get()
            print("Opening ID HQD", user_id) 
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/hqdefault.jpg")

        def mqd():
            user_id = enterid.get()
            print("Opening ID MQD", user_id) 
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/mqdefault.jpg")

        def lqd():
            user_id = enterid.get()
            print("Opening ID LQD", user_id) 
            webbrowser.open_new_tab(f"https://img.youtube.com/vi/{user_id}/default.jpg")

        tk.Button(self, text="Max Resolution", command=maxres).pack()
        tk.Button(self, text="Standard Definition", command=sd).pack()
        tk.Button(self, text="Default (HQ)", command=hqd).pack()
        tk.Button(self, text="Default (MQ)", command=mqd).pack()
        tk.Button(self, text="Default (LQ)", command=lqd).pack()
        
        
if __name__ == "__main__":
    pro = ThumbGet()
    pro.mainloop()