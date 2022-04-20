import os
from tkinter import messagebox

dnsIP = "192.168.1.205"


def btn_dns_settings_home():
    os.system('netsh interface ip set dns name="Ethernet" static ' + dnsIP)  # RPi DNS server
    os.system("echo Setting home DNS server")

    messagebox.showinfo("Info", "Setting home DNS Server to: " + dnsIP)


def btn_dns_settings_out():
    os.system('netsh interface ip set dnsservers name="Ethernet" source=dhcp')  # Clearing custom DNS settings
    os.system("echo Clearing custom DNS settings")

    messagebox.showinfo("Info", "Clearing custom DNS settings!")


def btn_nothing():
    messagebox.showinfo("showinfo", "Button does nothing...")
