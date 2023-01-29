import congine

HEIGHT = 50
WIDTH = 70

screen = congine.Screen((HEIGHT, WIDTH))
screen.initscr('/')
screen.refresh_rate(0.02)

position = (0, 0)
position_increase = (1, 1)
scale = (4, 8)

screen.init_rect(position, scale, "Player")

while True:
    if position[0] + scale[0] >= HEIGHT:
        position_increase = (-1, position_increase[1])

    if position[0] <= 0:
        position_increase = (1, position_increase[1])

    if position[1] + scale[1] >= WIDTH:
        position_increase = (position_increase[0], -1)

    if position[1] <= 0:
        position_increase = (position_increase[0], 1)

    position = (position[0]+position_increase[0], position[1]+position_increase[1])

    screen.draw_rect("Player", position, scale)
    screen.updatescr()