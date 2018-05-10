import subprocess
from tkinter import *
import os


def create_menu_bar(window):
    """Draw menu bar to the main window."""
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save")
    filemenu.add_separator()
    filemenu.add_command(label="Exit")
    menubar.add_cascade(label="File", menu=filemenu)


def add_video(eplist, playlist, current_playlist, var):
    """Add video to playlist being created."""
    current = eplist.get(ACTIVE)
    playlist.insert(END, current)
    current_playlist.append(current)  # adds the video to playback list.
    var.set(1)  # selects Create Playlist button automatically.


def remove_video(playlist):
    """Remove video from playlist."""
    current = playlist.index(ACTIVE)
    playlist.delete(current)


def move_up_list(playlist):
    """Move highlighted video file up on the playlist."""
    current = playlist.index(ACTIVE)
    if current != 0:
        playlist.insert(current - 1, playlist.get(current))
        playlist.delete(current + 1)


def move_down_list(playlist):
    """Move highlighted video file down on the playlist."""
    current = playlist.index(ACTIVE)
    if current != playlist.index(-1):
        playlist.insert(current + 2, playlist.get(current))
        playlist.delete(current)


def create_run_button(window):
    """Draw the run button to the main window."""
    run_btn = Button(window, text="Play", command=run_program)
    run_btn.grid(row=3, column=1)


def run_program(var, playlist, ep_dir):
    """Run the program depending on the player option selected."""
    option_chosen = var.get()

    if option_chosen == 1:
        # Create file path for videos in playlist.
        new_string = ''
        for file in playlist:
            new_string += '%s%s ' % (ep_dir, file)
        new_string = new_string.rstrip()
        new_string = new_string.replace(' ', '\ ')
        new_string = new_string.replace('mp4\\', 'mp4')

        # Run the playlist.
        subprocess.call(['castnow --address 192.168.2.178 %s' % (new_string)],
                        shell=True)

    else:
        # Play the shuffle episode list.
        subprocess.call(['castnow --address 192.168.2.178 '
            '/Users/justinlaureano/Movies/Its\ Always\ Sunny\ '
            'In\ Philadelphia/All --shuffle'], shell=True)