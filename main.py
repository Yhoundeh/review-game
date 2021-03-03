import arcade
import arcade.gui
from arcade.gui import UIManager


# Global Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'Historical Pursuit'
ROW_COUNT = 6
COLUMN_COUNT = 6
GRID_WIDTH = 100
GRID_HEIGHT = 100
MARGIN = 5
active_view = None

class MyFlatButton(arcade.gui.UIFlatButton):
    """
    To capture a button click, subclass the button and override on_click.
    """
    #def __init__(self, text, center_x, center_y, width, height, window):
    #    self.window = window


    def on_click(self):
        """ Called when user lets off button """
        question_view = QuestionView()
        self.window.show_view(question_view)
        active_view = 'question_view'

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
    def __init__(self):
        super().__init__()

        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        arcade.draw_text("Historical Pursuit", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ Use a mouse press to advance to the 'game' view. """
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
        active_view = 'game_view'


class GameView(arcade.View):
    """ Manage the 'game' view for our program. """

    def __init__(self):
        super().__init__()
        # Create variables here
        arcade.set_background_color(arcade.color.BABY_BLUE)
        self.grid_sprite_list = arcade.SpriteList()
        self.grid_sprites = []
        self.ui_manager = UIManager()

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        self.grid_sprite_list.draw()

    def on_hide_view(self):
        self.ui_manager.unregister_handlers()

    def setup(self):
        self.ui_manager.purge_ui_elements()

        y_slot = self.window.height // 4
        left_column_x = self.window.width // 4
        right_column_x = 3 * self.window.width // 4

        # right side elements
        button = MyFlatButton(
            'FlatButton',
            center_x=right_column_x,
            center_y=y_slot * 1,
            width=250,
            height=120,
            #window = self.window
        )
        self.ui_manager.add_ui_element(button)

        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (GRID_WIDTH + MARGIN) + (GRID_WIDTH*4 + MARGIN)
                y = row * (GRID_HEIGHT + MARGIN) + (GRID_HEIGHT / 1 + MARGIN)
                #need to either create sprite images or figure out how to put values on sprite
                sprite = arcade.SpriteSolidColor(GRID_WIDTH, GRID_HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

    def on_key_press(self, key, _modifiers):
        #if space key is pressed this shows the question view
        if key == arcade.key.SPACE:
            question_view = QuestionView()
            self.window.show_view(question_view)
            active_view = 'question_view'

class QuestionView(arcade.View):
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self):
        """ Draws the question view """
        arcade.start_render()
        arcade.draw_text("Questions Will Go Here", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the game view """
        if key == arcade.key.ESCAPE:
            game_view = GameView()
            self.window.show_view(game_view)
            active_view = 'game_view'

class button():

    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        question_view = QuestionView()


class player():

    def __init__(self):
        super().__init__()
        self.score = 0

    def answer_question(self, correct, question_value):
        if correct == True:
            self.score += question_value
        elif correct == False:
            self.score -= question_value
        else:
            pass

def main():
    """ Startup """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "Historical Pursuit")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()