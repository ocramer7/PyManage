import os
from tkinter import messagebox

dnsIP = "192.168.1.205"


def btn_dns_settings_home():
    os.system("networksetup -setdnsservers Wi-Fi " + dnsIP)  # RPi DNS server
    os.system("echo Setting home DNS server")
    os.system("echo")

    messagebox.showinfo("showinfo", "Setting home DNS Server to: " + dnsIP)


def btn_dns_settings_out():
    os.system("networksetup -setdnsservers Wi-Fi empty")  # Clearing custom DNS settings
    os.system("echo Clearing custom DNS settings")

    messagebox.showinfo("Info", "Clearing custom DNS settings!")
