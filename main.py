import congine, sys, termios, tty

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

screen = congine.Screen((45, 80))
screen.initscr('v')
screen.refresh_rate(0.2)

screen.init_rect((35, 5), (5, 50), "Obstacle", '&')
screen.init_rect((20, 25), (10, 10), "Player", '%')

def draw():
    screen.draw_rect("Player", (20, 20), (10, 10))
    screen.draw_rect("Obstacle", (35, 5), (5, 60))

    screen.updatescr()

def run():
    while True:
        draw()

        key = getch()

        if key == 'q':
            break

if __name__ == "__main__":
    run()