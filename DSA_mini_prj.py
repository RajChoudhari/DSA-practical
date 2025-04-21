import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 10
SIDEBAR_WIDTH = SCREEN_WIDTH - BOARD_SIZE

NUM_PLAYERS = 2
PLAYER_COLORS = [arcade.color.RED, arcade.coimport arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 10
SIDEBAR_WIDTH = SCREEN_WIDTH - BOARD_SIZE

NUM_PLAYERS = 2
PLAYER_COLORS = [arcade.color.RED, arcade.color.BLUE]

class SnakeLadderGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "🎲 Snake & Ladders - Arcade Edition")
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        self.positions = [1 for _ in range(NUM_PLAYERS)]
        self.turn = 0
        self.dice_result = None

        self.snakes, self.ladders = self.generate_snakes_and_ladders()

    def generate_snakes_and_ladders(self):
        import random
        all_pos = list(range(2, 100))
        random.shuffle(all_pos)
        snakes = {}
        ladders = {}
        used = set()

        while len(ladders) < 8:
            start, end = random.sample(all_pos, 2)
            if start < end and start not in used and end not in used:
                ladders[start] = end
                used.update([start, end])

        while len(snakes) < 8:
            start, end = random.sample(all_pos, 2)
            if start > end and start not in used and end not in used:
                snakes[start] = end
                used.update([start, end])

        return snakes, ladders

    def get_square_coords(self, position):
        row = (position - 1) // 10
        col = (position - 1) % 10
        if row % 2 == 1:
            col = 9 - col
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = (9 - row) * SQUARE_SIZE + SQUARE_SIZE // 2
        return x, y

    def on_draw(self):
        arcade.start_render()
        self.draw_board()
        self.draw_snakes_and_ladders()
        self.draw_players()
        self.draw_sidebar()

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = arcade.color.WHITE if (row + col) % 2 == 0 else arcade.color.LIGHT_GRAY
                arcade.draw_rectangle_filled(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE, color)

                number = 100 - (row * 10 + (col if row % 2 == 0 else 9 - col))
                arcade.draw_text(str(number), x + 5, y + 5, arcade.color.BLACK, 12)

    def draw_players(self):
        for i, pos in enumerate(self.positions):
            x, y = self.get_square_coords(pos)
            arcade.draw_circle_filled(x + i * 10, y, 10, PLAYER_COLORS[i])

    def draw_snakes_and_ladders(self):
        for start, end in self.ladders.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.BROWN, 4)

        for start, end in self.snakes.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.PURPLE, 4)

    def draw_sidebar(self):
        x = BOARD_SIZE + 20
        y = SCREEN_HEIGHT - 40
        arcade.draw_text(f"🎯 Turn: Player {self.turn + 1}", x, y, arcade.color.BLACK, 18)
        if self.dice_result:
            arcade.draw_text(f"🎲 Rolled: {self.dice_result}", x, y - 30, arcade.color.DARK_BLUE, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        dice = self.roll_dice()
        self.dice_result = dice
        self.move_player(dice)

        if self.positions[self.turn] == 100:
            arcade.draw_text(f"🏆 Player {self.turn + 1} wins!", BOARD_SIZE + 20, 200, arcade.color.GREEN, 20)
            arcade.finish_render()
            arcade.pause(3)
            arcade.close_window()

        self.turn = (self.turn + 1) % NUM_PLAYERS

    def roll_dice(self):
        return arcade.rand_in_circle((0, 0), 6)[0] % 6 + 1

    def move_player(self, dice):
        pos = self.positions[self.turn] + dice
        if pos > 100:
            return
        if pos in self.snakes:
            pos = self.snakes[pos]
        elif pos in self.ladders:
            pos = self.ladders[pos]
        self.positions[self.turn] = pos


if __name__ == "__main__":
    SnakeLadderGame()
    arcade.run()import arcade

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
BOARD_SIZE = 600
SQUARE_SIZE = BOARD_SIZE // 10
SIDEBAR_WIDTH = SCREEN_WIDTH - BOARD_SIZE

NUM_PLAYERS = 2
PLAYER_COLORS = [arcade.color.RED, arcade.color.BLUE]

class SnakeLadderGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "🎲 Snake & Ladders - Arcade Edition")
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        self.positions = [1 for _ in range(NUM_PLAYERS)]
        self.turn = 0
        self.dice_result = None

        self.snakes, self.ladders = self.generate_snakes_and_ladders()

    def generate_snakes_and_ladders(self):
        import random
        all_pos = list(range(2, 100))
        random.shuffle(all_pos)
        snakes = {}
        ladders = {}
        used = set()

        while len(ladders) < 8:
            start, end = random.sample(all_pos, 2)
            if start < end and start not in used and end not in used:
                ladders[start] = end
                used.update([start, end])

        while len(snakes) < 8:
            start, end = random.sample(all_pos, 2)
            if start > end and start not in used and end not in used:
                snakes[start] = end
                used.update([start, end])

        return snakes, ladders

    def get_square_coords(self, position):
        row = (position - 1) // 10
        col = (position - 1) % 10
        if row % 2 == 1:
            col = 9 - col
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = (9 - row) * SQUARE_SIZE + SQUARE_SIZE // 2
        return x, y

    def on_draw(self):
        arcade.start_render()
        self.draw_board()
        self.draw_snakes_and_ladders()
        self.draw_players()
        self.draw_sidebar()

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = arcade.color.WHITE if (row + col) % 2 == 0 else arcade.color.LIGHT_GRAY
                arcade.draw_rectangle_filled(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE, color)

                number = 100 - (row * 10 + (col if row % 2 == 0 else 9 - col))
                arcade.draw_text(str(number), x + 5, y + 5, arcade.color.BLACK, 12)

    def draw_players(self):
        for i, pos in enumerate(self.positions):
            x, y = self.get_square_coords(pos)
            arcade.draw_circle_filled(x + i * 10, y, 10, PLAYER_COLORS[i])

    def draw_snakes_and_ladders(self):
        for start, end in self.ladders.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.BROWN, 4)

        for start, end in self.snakes.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.PURPLE, 4)

    def draw_sidebar(self):
        x = BOARD_SIZE + 20
        y = SCREEN_HEIGHT - 40
        arcade.draw_text(f"🎯 Turn: Player {self.turn + 1}", x, y, arcade.color.BLACK, 18)
        if self.dice_result:
            arcade.draw_text(f"🎲 Rolled: {self.dice_result}", x, y - 30, arcade.color.DARK_BLUE, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        dice = self.roll_dice()
        self.dice_result = dice
        self.move_player(dice)

        if self.positions[self.turn] == 100:
            arcade.draw_text(f"🏆 Player {self.turn + 1} wins!", BOARD_SIZE + 20, 200, arcade.color.GREEN, 20)
            arcade.finish_render()
            arcade.pause(3)
            arcade.close_window()

        self.turn = (self.turn + 1) % NUM_PLAYERS

    def roll_dice(self):
        return arcade.rand_in_circle((0, 0), 6)[0] % 6 + 1

    def move_player(self, dice):
        pos = self.positions[self.turn] + dice
        if pos > 100:
            return
        if pos in self.snakes:
            pos = self.snakes[pos]
        elif pos in self.ladders:
            pos = self.ladders[pos]
        self.positions[self.turn] = pos


if __name__ == "__main__":
    SnakeLadderGame()
    arcade.run()lor.BLUE]

class SnakeLadderGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "🎲 Snake & Ladders - Arcade Edition")
        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        self.positions = [1 for _ in range(NUM_PLAYERS)]
        self.turn = 0
        self.dice_result = None

        self.snakes, self.ladders = self.generate_snakes_and_ladders()

    def generate_snakes_and_ladders(self):
        import random
        all_pos = list(range(2, 100))
        random.shuffle(all_pos)
        snakes = {}
        ladders = {}
        used = set()

        while len(ladders) < 8:
            start, end = random.sample(all_pos, 2)
            if start < end and start not in used and end not in used:
                ladders[start] = end
                used.update([start, end])

        while len(snakes) < 8:
            start, end = random.sample(all_pos, 2)
            if start > end and start not in used and end not in used:
                snakes[start] = end
                used.update([start, end])

        return snakes, ladders

    def get_square_coords(self, position):
        row = (position - 1) // 10
        col = (position - 1) % 10
        if row % 2 == 1:
            col = 9 - col
        x = col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = (9 - row) * SQUARE_SIZE + SQUARE_SIZE // 2
        return x, y

    def on_draw(self):
        arcade.start_render()
        self.draw_board()
        self.draw_snakes_and_ladders()
        self.draw_players()
        self.draw_sidebar()

    def draw_board(self):
        for row in range(10):
            for col in range(10):
                x = col * SQUARE_SIZE
                y = row * SQUARE_SIZE
                color = arcade.color.WHITE if (row + col) % 2 == 0 else arcade.color.LIGHT_GRAY
                arcade.draw_rectangle_filled(x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2, SQUARE_SIZE, SQUARE_SIZE, color)

                number = 100 - (row * 10 + (col if row % 2 == 0 else 9 - col))
                arcade.draw_text(str(number), x + 5, y + 5, arcade.color.BLACK, 12)

    def draw_players(self):
        for i, pos in enumerate(self.positions):
            x, y = self.get_square_coords(pos)
            arcade.draw_circle_filled(x + i * 10, y, 10, PLAYER_COLORS[i])

    def draw_snakes_and_ladders(self):
        for start, end in self.ladders.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.BROWN, 4)

        for start, end in self.snakes.items():
            x1, y1 = self.get_square_coords(start)
            x2, y2 = self.get_square_coords(end)
            arcade.draw_line(x1, y1, x2, y2, arcade.color.PURPLE, 4)

    def draw_sidebar(self):
        x = BOARD_SIZE + 20
        y = SCREEN_HEIGHT - 40
        arcade.draw_text(f"🎯 Turn: Player {self.turn + 1}", x, y, arcade.color.BLACK, 18)
        if self.dice_result:
            arcade.draw_text(f"🎲 Rolled: {self.dice_result}", x, y - 30, arcade.color.DARK_BLUE, 20)

    def on_mouse_press(self, x, y, button, modifiers):
        dice = self.roll_dice()
        self.dice_result = dice
        self.move_player(dice)

        if self.positions[self.turn] == 100:
            arcade.draw_text(f"🏆 Player {self.turn + 1} wins!", BOARD_SIZE + 20, 200, arcade.color.GREEN, 20)
            arcade.finish_render()
            arcade.pause(3)
            arcade.close_window()

        self.turn = (self.turn + 1) % NUM_PLAYERS

    def roll_dice(self):
        return arcade.rand_in_circle((0, 0), 6)[0] % 6 + 1

    def move_player(self, dice):
        pos = self.positions[self.turn] + dice
        if pos > 100:
            return
        if pos in self.snakes:
            pos = self.snakes[pos]
        elif pos in self.ladders:
            pos = self.ladders[pos]
        self.positions[self.turn] = pos


if __name__ == "__main__":
    SnakeLadderGame()
    arcade.run()