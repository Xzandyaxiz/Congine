class Screen:
    def __init__(self, size: tuple):
        self.height = size[0]
        self.width = size[1]*2

        self.screen_buffer = ''
        self.bg = '\u2588'
        self.bg_color = ''
    
        self.Rect = []
        self.Rect_char = " "

    def initscr(self, bg = None):
        if bg:
            if len(bg) != 1:
                return Error.ThrowIllegalCharacter(message="self.bg")

            self.bg = bg

        for y in range(self.height):
            self.screen_buffer += self.bg * self.width + '\n'

    def updatescr(self):
        print('\033c\033[H' + self.screen_buffer, end='\r', flush=True)

    def draw_rect(self, rect: str, new_pos: tuple = None, new_scale: tuple = None):
        rect_buf = []

        rows_to_print = (0, 0)

        for rect_i, rect_real in enumerate(self.Rect):
            if not rect_real[2] == rect:
                continue

            rect_buf = rect_real
            
            self.Rect[rect_i] = rect_buf

        if new_pos:
            rect_buf[0] = new_pos

        if new_scale:
            rect_buf[1] = new_scale

        rows = self.screen_buffer.split('\n')

        for index, row in enumerate(rows):
            height_s = rect_buf[1][0] + index
            
            if not index == rect_buf[0][0]:
                continue
            
            rows_to_print = (index, height_s)

        for row_num in range(rows_to_print[1] - rows_to_print[0]):
            current_row_index = rows_to_print[0] + row_num
            current_row_chars = [char for char in rows[current_row_index]]

            for index, char in enumerate(current_row_chars):
                if index >= rect_buf[0][1] and index <= rect_buf[1][1] + rect_buf[0][1]:
                    current_row_chars[index] = f'{rect_buf[3]}'

            rows[current_row_index] = ''.join(current_row_chars)
            self.screen_buffer = '\n'.join(rows)

        return self.updatescr()

    def init_rect(self, position: tuple, size: tuple, id: str, char: str = ' '):
        if len(char) != 1:
            return Error.ThrowIllegalCharacter('Character must be 1 in length.')

        self.Rect.append([position, size, id, char])

class Error:
    def ThrowIllegalCharacter(message=None):
        return print(f"Illegal character: '{message}'\n")