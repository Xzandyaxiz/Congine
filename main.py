import congine

screen = congine.Screen((45, 80))
screen.initscr('v')

screen.init_rect((35, 5), (5, 50), "Obstacle")
screen.init_rect((20, 25), (10, 10), "Player", '/')

def draw():
    screen.draw_rect("Player", (20, 20), (10, 10))
    screen.draw_rect("Obstacle", (50, 10), (5, 50))

draw()