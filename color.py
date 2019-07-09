from colorconsole import terminal

screen = terminal.get_terminal(conEmu=False)

screen.cprint(4, 0, "This is red\n")
screen.cprint(10, 0, "This is light green\n")
screen.cprint(0, 11, "This is black on light cyan\n")

