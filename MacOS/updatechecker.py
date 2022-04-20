from tkinter import *
import urllib


def update_check(self):
    update = False

    update_window = Toplevel()
    update_window.title(string="Update Checker")
    update_window.resizable(False, False)

    # Gets downloaded version
    version_source = open('version.txt', 'r')
    version_contents = version_source.read()

    # gets newest version
    update_source = urllib.urlopen("http://www.suturesoft.com/Updates/craftbook.txt")
    update_contents = update_source.read()

    # checks for updates
    for i in range(0, 20):
        if update_contents[i] != version_contents[i]:
            dataLabel = Label(update_window, text="\n\nThere are data updates availible.\n\n")
            dataLabel.pack()
            update = True
            break
    for i in range(22, 42):
        if update_contents[i] != version_contents[i]:
            versionLabel = Label(update_window, text="\n\nThere are version updates availible.\n\n")
            versionLabel.pack()
            update = True
            break
    if not update:
        versionLabel = Label(update_window, text="\n\nYou are already running the most up to date version.\n\n")
        versionLabel.pack()
