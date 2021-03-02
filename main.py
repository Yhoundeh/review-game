import arcade

'''
TO-DO:
-Calibrate buttons to do different things on different screens (button on game menu should pull up the question, button on the question menu should do something different)
-Change the grid on the game menu so that it shows buttons in the grid with the value of the questions displayed and the top row shows the categories
-Need to change the values of the questions to better fit the grid (we only need 5 of each value and it appears we have 10 100 value questions)
-Figure out how to have each question button call back to a specific question in our database (probably will need a question class)
-Could use a python version of an ERD (I cannot for the life of me remember what they're called lol)
-We either need to find a way to write text on top of a sprite or make a image for each of our questions so I can call those in (however making the images will make our database redundant so probaby having text on our sprites will be ideal)
-Might need another view so we can show the winner at the end
*I will add more here as I think of things our program is currently lacking.
'''

# Global Variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = 'Historical Pursuit'
ROW_COUNT = 5
COLUMN_COUNT = 5
GRID_WIDTH = 100
GRID_HEIGHT = 100
MARGIN = 5
active_view = None

class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""
        arcade.set_background_color(arcade.color.BABY_BLUE)

        #I might need to include a setup function here
        #active_view = 'menu_view'

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()

        ## need to implement as buttons later to add question input functionality
        arcade.draw_text("Historical Pursuit", SCREEN_WIDTH/2, SCREEN_HEIGHT/2,
                         arcade.color.BLACK, font_size=30, anchor_x="center")


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

    def setup(self):
        for row in range(ROW_COUNT):
            self.grid_sprites.append([])
            for column in range(COLUMN_COUNT):
                x = column * (GRID_WIDTH + MARGIN) + (GRID_WIDTH*4.75 + MARGIN)
                y = row * (GRID_HEIGHT + MARGIN) + (GRID_HEIGHT / 1 + MARGIN)
                #need to either create sprite images or figure out how to put values on sprite
                sprite = arcade.SpriteSolidColor(GRID_WIDTH, GRID_HEIGHT, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
                self.grid_sprites[row].append(sprite)

    def on_draw(self):
        """ Draw everything for the game. """
        arcade.start_render()
        self.grid_sprite_list.draw()

    def on_button_press(self, _x, _y, _button, _modifiers))

    def on_key_press(self, key, _modifiers):
        #if space key is his shows the question view
        #need to switch this over to mouse interactive button
        if key == arcade.key.SPACE:
            question_view = QuestionView()
            self.window.show_view(question_view)
            active_view = 'question_view'

class QuestionView(arcade.View):
    #somehow need to specify to get different question view for each question
    #maybe use setup function to pull which question 
    def __init__(self):
        super().__init__()
        arcade.set_background_color(arcade.color.BABY_BLUE)

    def on_draw(self):
        """ Draws the question view """
        arcade.start_render()
        arcade.draw_text("Question Will Go Here", SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.BLACK, 30, anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ If user hits escape, go back to the game view """
        if key == arcade.key.ESCAPE:
            game_view = GameView()
            self.window.show_view(game_view)
            active_view = 'game_view'

class button():
    #needs more work
    def __init__(self, x, y, width, height):
        super().__init__()
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        #if I use the view variable I set I can change what happens when the button is pressed depending on what screen is active
        question_view = QuestionView()
        #self.window.show_view(question_view)

class player():
    #could potentially need more work 
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
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, "History Trivia")
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()