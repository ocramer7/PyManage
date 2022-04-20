import tkinter as tk
from MacOS import macos_functions as macfc

root = tk.Tk(className='PyManage')
frame = tk.Frame()
root.geometry("1280x720")


class App():
    def handle_click(event):
        print("The button was clicked!")

    button = tk.Button(
        master=frame,
        text="DNS_Home",
        command=macfc.btn_dns_settings_home,
        height=5,
        width=25,
        bg="#808080"
    )

    button2 = tk.Button(
        master=frame,
        text="DNS_Out",
        command=macfc.btn_dns_settings_out,
        height=5,
        width=25,
        background="#808080"
    )
    button.bind("<Button-1>", handle_click)
    button2.bind("<Button-2>", handle_click)

    button.pack()
    button2.pack()

    frame.pack()

    root.mainloop()


if __name__ == "__main__":
    App()