import os
from tkinter import messagebox

dnsIP = "192.168.1.205"


def btn_dns_settings_home():
    # os.system("dnshome")
    os.system("networksetup -setdnsservers Wi-Fi " + dnsIP)  # RPi DNS server
    # Windows: os.system('netsh interface ip set dns "Local Area Connection" static 192.168.0.200')
    os.system("echo Setting home DNS server")

    messagebox.showinfo("showinfo", "Setting home DNS Server to: " + dnsIP)


def btn_dns_settings_out():
    # os.system("dnsout")
    os.system("networksetup -setdnsservers Wi-Fi empty")  # Clearing custom DNS settings
    os.system("echo Clearing custom DNS settings")

    messagebox.showinfo("Info", "Clearing custom DNS settings!")
