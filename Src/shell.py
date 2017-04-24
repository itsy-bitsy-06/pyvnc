"""
Command line shell for VNC automation interface.

"""
import os
import sys
import click
import StringIO
import click_shell
from vncdotool import api
from screen import CaptureUtil

CLIENT = None

@click_shell.shell(prompt='caesg > ')
def main():
    """
    Initialize shell.

    """
    click.echo("Initializing shell.")


@main.command()
@click.option('--host', help='host to connect to')
@click.option('--display', help='display to connect to')
@click.option('--password', default=None, help='Password to connect to host')
def connect(host, display, password):
    """
    Connects to the server.

    """
    global CLIENT
    host = str(host) + ':' + str(display)
    CLIENT = api.connect(host, password)

@main.command()
@click.option('--outfile', default='screenshot.png', help='outfile to save screenshot to')
def screenshot(outfile):
    """
    Captures a screenshot of the session.

    """
    CLIENT.captureScreen(outfile)

@main.command()
@click.option('--string', help='text to type')
def typekeys(string):
    """
    Send key press to vnc session

    """
    for k in string:
        CLIENT.keyPress(k)

@main.command()
def imagetext():
    """
    Echo the text processed out of an image.
    Needs the application tesseract-ocr installed.
    On ubuntu : sudo apt-get install tesseract-ocr

    """
    cap = CaptureUtil()
    click.echo(cap.get_string())

@main.command()
def pressenter():
    """
    clears the screen

    """
    CLIENT.keyPress('enter')

@main.command()
def clear():
    """
    clears the screen

    """
    click.clear()

if __name__ == '__main__':
    # Extra argument is assumed to be a script file to run.
    # python shell.py my_saved_script.txt
    if len(sys.argv) > 1:
        INPUT = open(sys.argv[1], 'rt')
        del sys.argv[1]
        sys.stdin = INPUT
    main()

