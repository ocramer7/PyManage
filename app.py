import tkinter as tk
import windows_functions as winfc

root = tk.Tk()
root.title("PyManage")
frame = tk.Frame()
root.geometry("1280x720")

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=winfc.btn_nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)


class App:

    def handle_click(self):
        print("The button was clicked!")


    label = tk.Label(
        master=frame,
        text="DNS Server Set:"
    )

    button = tk.Button(
        master=frame,
        text="DNS_Home",
        command=winfc.btn_dns_settings_home,
        height=5,
        width=25,
        bg="#808080"
    )

    button2 = tk.Button(
        master=frame,
        text="DNS_Out",
        command=winfc.btn_dns_settings_out,
        height=5,
        width=25,
        background="#808080"
    )
    button.bind("<Button-1>", handle_click)
    button2.bind("<Button-1>", handle_click)

    label.pack(side=tk.TOP)
    button.pack(side=tk.LEFT)
    button2.pack()

    frame.place(x=720, y=10)

    root.config(menu=menubar)
    root.mainloop()


if __name__ == "__main__":
    App()
