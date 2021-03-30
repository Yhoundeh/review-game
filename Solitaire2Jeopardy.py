"""
Solitaire clone.
"""
import arcade

# Screen title and size
SCREEN_WIDTH = 1024
#SCREEN_HEIGHT = 768
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Drag and Drop Cards"

# Constants for sizing
#CARD_SCALE = 0.6
CARD_SCALE = 0.3

# How big are the cards?
CARD_WIDTH = 140 * CARD_SCALE
CARD_HEIGHT = 190 * CARD_SCALE

# How big is the mat we'll place the card on?
MAT_PERCENT_OVERSIZE = 1.25
MAT_HEIGHT = int(CARD_HEIGHT * MAT_PERCENT_OVERSIZE)
MAT_WIDTH = int(CARD_WIDTH * MAT_PERCENT_OVERSIZE)

# How much space do we leave as a gap between the mats?
# Done as a percent of the mat size.
VERTICAL_MARGIN_PERCENT = 0.10
HORIZONTAL_MARGIN_PERCENT = 0.10

# The Y of the bottom row (2 piles)
BOTTOM_Y = MAT_HEIGHT / 2 + MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The X of where to start putting things on the left side
START_X = MAT_WIDTH / 2 + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT

# The Y of the top row (4 piles)
TOP_Y = SCREEN_HEIGHT - MAT_HEIGHT / 2 - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# The Y of the middle row (7 piles)
MIDDLE_Y = TOP_Y - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# How far apart each pile goes
X_SPACING = MAT_WIDTH + MAT_WIDTH * HORIZONTAL_MARGIN_PERCENT
Y_SPACING = 0 - MAT_HEIGHT - MAT_HEIGHT * VERTICAL_MARGIN_PERCENT

# Card constants
CARD_VALUES = ["6", "5", "4", "3", "2"]
CARD_SUITS = ["Clubs", "Hearts", "Spades", "Diamonds"]

# If we fan out cards stacked on each other, how far apart to fan them?
CARD_VERTICAL_OFFSET = CARD_HEIGHT * CARD_SCALE * 0.3

# Face down image
FACE_DOWN_IMAGE = ":resources:images/cards/cardBack_red2.png"

# Constants that represent "what pile is what" for the game
PILE_COUNT = 33
BOTTOM_FACE_DOWN_PILE = 0
BOTTOM_FACE_UP_PILE = 1
BOTTOM_FACE_RIGHT_PILE = 32
PLAY_PILE_1 = 2
PLAY_PILE_2 = 3
PLAY_PILE_3 = 4
PLAY_PILE_4 = 5
PLAY_PILE_5 = 6
PLAY_PILE_6 = 7
PLAY_PILE_7 = 8
PLAY_PILE_8 = 9
PLAY_PILE_9 = 10
PLAY_PILE_10 = 11
PLAY_PILE_11 = 12
PLAY_PILE_12 = 13
PLAY_PILE_13 = 14
PLAY_PILE_14 = 15
PLAY_PILE_15 = 16
PLAY_PILE_16 = 17
PLAY_PILE_17 = 18
PLAY_PILE_18 = 19
PLAY_PILE_19 = 20
PLAY_PILE_20 = 21
PLAY_PILE_21 = 22
PLAY_PILE_22 = 23
PLAY_PILE_23 = 24
PLAY_PILE_24 = 25
PLAY_PILE_25 = 26
PLAY_PILE_26 = 27
PLAY_PILE_27 = 28
PLAY_PILE_28 = 29
PLAY_PILE_29 = 30
PLAY_PILE_30 = 31
#TOP_PILE_1 = 32
#TOP_PILE_2 = 33
#TOP_PILE_3 = 34
#TOP_PILE_4 = 35


class Card(arcade.Sprite):
    """ Card sprite """

    def __init__(self, suit, value, scale=1):
        """ Card constructor """

        # Attributes for suit and value
        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up
        self.image_file_name = f":resources:images/cards/card{self.suit}{self.value}.png"
        self.is_face_up = False
        super().__init__(FACE_DOWN_IMAGE, scale, hit_box_algorithm="None")

    def face_down(self):
        """ Turn card face-down """
        self.texture = arcade.load_texture(FACE_DOWN_IMAGE)
        self.is_face_up = False

    def face_up(self):
        """ Turn card face-up """
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        """ Is this card face down? """
        return not self.is_face_up


class BoardView(arcade.View):
    """ Main application class. """

    def __init__(self):
        super().__init__()
        self.King_Of_Clubs = 0
        self.Queen_Of_Diamonds = 0
        self.Jack_Of_Spades = 0
        # Sprite list with all the cards, no matter what pile they are in.
        # self.card_list = None

        arcade.set_background_color(arcade.color.AMAZON)

        # List of cards we are dragging with the mouse
        """ self.held_cards = None

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = None

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list = None

        # Create a list of lists, each holds a pile of cards.
        self.piles = None

    def setup(self): """
        """ Set up the game here. Call this function to restart the game. """

        # List of cards we are dragging with the mouse
        self.held_cards = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = []

        # ---  Create the mats the cards go on.

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        # Create the mats for the bottom face down and face up piles
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X, BOTTOM_Y
        self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)

        # Create the seven middle piles
        for i in range(6):
            for j in range(5):
                pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
                pile.position = START_X + i * X_SPACING, MIDDLE_Y + j * Y_SPACING
                self.pile_mat_list.append(pile)

        # Create the top "play" piles
        #for i in range(4):
            #pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            #pile.position = START_X + i * X_SPACING, TOP_Y
            #self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + X_SPACING + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)

        # --- Create, shuffle, and deal the cards

        # Sprite list with all the cards, no matter what pile they are in.
        self.card_list = arcade.SpriteList()

        card = Card("Clubs", "K", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        card = Card("Diamonds", "Q", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        card = Card("Spades", "J", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        # Create every card
        for i in range(6):
            for card_value in CARD_VALUES:
                card = Card("Hearts", card_value, CARD_SCALE)
                card.position = START_X, BOTTOM_Y
                self.card_list.append(card)

        # Create a list of lists, each holds a pile of cards.
        self.piles = [[] for _ in range(PILE_COUNT)]

        # Put all the cards in the bottom face-down pile
        for card in self.card_list:
            self.piles[BOTTOM_FACE_DOWN_PILE].append(card)

        # - Pull from that pile into the middle piles, all face-down
        # Loop for each pile
        for pile_no in range(PLAY_PILE_1, PLAY_PILE_30 + 1):
            # Pop the card off the deck we are dealing from
            card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
            # Put in the proper pile
            self.piles[pile_no].append(card)
            # Move card to same position as pile we just put it in
            card.position = self.pile_mat_list[pile_no].position
            # Put on top in draw order
            self.pull_to_top(card)

        card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
        self.piles[32].append(card)
        card.position = self.pile_mat_list[32].position
        self.pull_to_top(card)

        card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
        self.piles[1].append(card)
        card.position = self.pile_mat_list[1].position
        self.pull_to_top(card)

        # Flip up the top cards
        for i in range(PLAY_PILE_1, PLAY_PILE_30 + 1):
            self.piles[i][-1].face_up()

        self.piles[32][-1].face_up()
        self.piles[1][-1].face_up()
        self.piles[0][-1].face_up()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the mats the cards go on to
        self.pile_mat_list.draw()

        # Draw the cards
        self.card_list.draw()

        output = f"{self.King_Of_Clubs}"
        arcade.draw_text(output, 27, 80, arcade.color.WHITE, 14)

        output = f"{self.Queen_Of_Diamonds}"
        arcade.draw_text(output, 27 + X_SPACING, 80, arcade.color.WHITE, 14)

        output = f"{self.Jack_Of_Spades}"
        arcade.draw_text(output, 27 + X_SPACING + X_SPACING, 80, arcade.color.WHITE, 14)

    def pull_to_top(self, card):
        """ Pull card to top of rendering order (last to render, looks on-top) """
        # Find the index of the card
        index = self.card_list.index(card)
        # Loop and pull all the other cards down towards the zero end
        for i in range(index, len(self.card_list) - 1):
            self.card_list[i] = self.card_list[i + 1]
        # Put this card at the right-side/top/size of list
        self.card_list[len(self.card_list) - 1] = card

    #def on_key_press(self, symbol: int, modifiers: int):
        """ User presses key """
        #if symbol == arcade.key.R:
            # Restart
            #self.setup()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        # Have we clicked on a card?
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]
            if primary_card.suit == "Hearts":
                # Figure out what pile the card is in
                pile_index = self.get_pile_for_card(primary_card)
                
                if primary_card.value == "2":
                    self.points = 2

                elif primary_card.value == "3":
                    self.points = 3

                elif primary_card.value == "4":
                    self.points = 4

                elif primary_card.value == "5":
                    self.points = 5

                elif primary_card.value == "6":
                    self.points = 6

                self.card_list.remove(primary_card)

                question_view = QuestionView(self)
                question_view.setup()
                self.window.show_view(question_view)

            # Are we clicking on the bottom deck, to flip three cards?
            """ if pile_index == BOTTOM_FACE_DOWN_PILE:
                # Flip three cards
                for i in range(3):
                    # If we ran out of cards, stop
                    if len(self.piles[BOTTOM_FACE_DOWN_PILE]) == 0:
                        break
                    # Get top card
                    card = self.piles[BOTTOM_FACE_DOWN_PILE][-1]
                    # Flip face up
                    card.face_up()
                    # Move card position to bottom-right face up pile
                    card.position = self.pile_mat_list[BOTTOM_FACE_UP_PILE].position
                    # Remove card from face down pile
                    self.piles[BOTTOM_FACE_DOWN_PILE].remove(card)
                    # Move card to face up list
                    self.piles[BOTTOM_FACE_UP_PILE].append(card)
                    # Put on top draw-order wise
                    self.pull_to_top(card) 

            elif primary_card.is_face_down:
                # Is the card face down? In one of those middle 7 piles? Then flip up
                primary_card.face_up()
            else:
                # All other cases, grab the face-up card we are clicking on
                self.held_cards = [primary_card]
                # Save the position
                self.held_cards_original_position = [self.held_cards[0].position]
                # Put on top in drawing order
                self.pull_to_top(self.held_cards[0])

                # Is this a stack of cards? If so, grab the other cards too
                card_index = self.piles[pile_index].index(primary_card)
                for i in range(card_index + 1, len(self.piles[pile_index])):
                    card = self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_original_position.append(card.position)
                    self.pull_to_top(card) 

        else:

            # Click on a mat instead of a card?
            mats = arcade.get_sprites_at_point((x, y), self.pile_mat_list)

            if len(mats) > 0:
                mat = mats[0]
                mat_index = self.pile_mat_list.index(mat)

                # Is it our turned over flip mat? and no cards on it?
                if mat_index == BOTTOM_FACE_DOWN_PILE and len(self.piles[BOTTOM_FACE_DOWN_PILE]) == 0:
                    # Flip the deck back over so we can restart
                    temp_list = self.piles[BOTTOM_FACE_UP_PILE].copy()
                    for card in reversed(temp_list):
                        card.face_down()
                        self.piles[BOTTOM_FACE_UP_PILE].remove(card)
                        self.piles[BOTTOM_FACE_DOWN_PILE].append(card)
                        card.position = self.pile_mat_list[BOTTOM_FACE_DOWN_PILE].position """

    def remove_card_from_pile(self, card):
        """ Remove card from whatever pile it was in. """
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def get_pile_for_card(self, card):
        """ What pile is this card in? """
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def move_card_to_new_pile(self, card, pile_index):
        """ Move the card to a new pile """
        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        # Find the closest pile, in case we are in contact with more than one
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        # See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):

            # What pile is it?
            pile_index = self.pile_mat_list.index(pile)

            #  Is it the same pile we came from?
            if pile_index == self.get_pile_for_card(self.held_cards[0]):
                # If so, who cares. We'll just reset our position.
                pass

            # Is it on a middle play pile?
            elif PLAY_PILE_1 <= pile_index <= PLAY_PILE_7:
                # Are there already cards there?
                if len(self.piles[pile_index]) > 0:
                    # Move cards to proper position
                    top_card = self.piles[pile_index][-1]
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                                                top_card.center_y - CARD_VERTICAL_OFFSET * (i + 1)
                else:
                    # Are there no cards in the middle play pile?
                    for i, dropped_card in enumerate(self.held_cards):
                        # Move cards to proper position
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - CARD_VERTICAL_OFFSET * i

                for card in self.held_cards:
                    # Cards are in the right position, but we need to move them to the right list
                    self.move_card_to_new_pile(card, pile_index)

                # Success, don't reset position of cards
                reset_position = False

            # Release on top play pile? And only one card held?
            elif TOP_PILE_1 <= pile_index <= TOP_PILE_4 and len(self.held_cards) == 1:
                # Move position of card to pile
                self.held_cards[0].position = pile.position
                # Move card to card list
                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        # We are no longer holding cards
        self.held_cards = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

# class QuestionView(arcade.View):

 #   def __init__(self):
        """ This is run once when we switch to this view """
  #      super().__init__()
    
   # def on_show(self):
        """ This is run once when we switch to this view """
    #    arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

   # def on_draw(self):
        """ Draw this view """
    #    arcade.start_render()
     #   arcade.draw_text("Instructions Screen", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
      #                   arcade.color.WHITE, font_size=50, anchor_x="center")

   # def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, re-start the game. """
     #   game_view = AnswerView()
    #    game_view.setup()
      #  self.window.show_view(game_view) """

class QuestionView(arcade.View):
    """ Main application class. """

    def __init__(self, board_view):
        super().__init__()
        self.board_view = board_view
        self.answer = False
        King_Of_Clubs = self.board_view.King_Of_Clubs
        Queen_Of_Diamonds = self.board_view.Queen_Of_Diamonds
        Jack_Of_Spades = self.board_view.Jack_Of_Spades
        points = self.board_view.points

        # Sprite list with all the cards, no matter what pile they are in.
        self.card_list = None

        arcade.set_background_color(arcade.color.AMAZON)

        # List of cards we are dragging with the mouse
        self.held_cards = None

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = None

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list = None

        # Create a list of lists, each holds a pile of cards.
        self.piles = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of cards we are dragging with the mouse
        self.held_cards = []

        # Original location of cards we are dragging with the mouse in case
        # they have to go back.
        self.held_cards_original_position = []

        # ---  Create the mats the cards go on.

        # Sprite list with all the mats tha cards lay on.
        self.pile_mat_list: arcade.SpriteList = arcade.SpriteList()

        # Create the mats for the bottom face down and face up piles
        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X, BOTTOM_Y
        self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)

        # Create the seven middle piles
        #for i in range(6):
            #for j in range(5):
                #pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
                #pile.position = START_X + i * X_SPACING, MIDDLE_Y + j * Y_SPACING
                #self.pile_mat_list.append(pile)

        # Create the top "play" piles
        #for i in range(4):
            #pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
            #pile.position = START_X + i * X_SPACING, TOP_Y
            #self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + X_SPACING + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)

        pile = arcade.SpriteSolidColor(MAT_WIDTH, MAT_HEIGHT, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = START_X + X_SPACING + X_SPACING + X_SPACING, BOTTOM_Y
        self.pile_mat_list.append(pile)

        # --- Create, shuffle, and deal the cards

        # Sprite list with all the cards, no matter what pile they are in.
        self.card_list = arcade.SpriteList()

        card = Card("Clubs", "K", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        card = Card("Diamonds", "Q", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        card = Card("Spades", "J", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        card = Card("Hearts", "A", CARD_SCALE)
        card.position = START_X, BOTTOM_Y
        self.card_list.append(card)

        # Create every card
        #for i in range(6):
            #for card_value in CARD_VALUES:
                #card = Card("Hearts", card_value, CARD_SCALE)
                #card.position = START_X, BOTTOM_Y
                #self.card_list.append(card)

        # Create a list of lists, each holds a pile of cards.
        self.piles = [[] for _ in range(PILE_COUNT)]

        # Put all the cards in the bottom face-down pile
        for card in self.card_list:
            self.piles[BOTTOM_FACE_DOWN_PILE].append(card)

        # - Pull from that pile into the middle piles, all face-down
        # Loop for each pile
        #for pile_no in range(PLAY_PILE_1, PLAY_PILE_30 + 1):
            # Pop the card off the deck we are dealing from
            #card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
            # Put in the proper pile
            #self.piles[pile_no].append(card)
            # Move card to same position as pile we just put it in
            #card.position = self.pile_mat_list[pile_no].position
            # Put on top in draw order
            #self.pull_to_top(card)

        card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
        self.piles[3].append(card)
        card.position = self.pile_mat_list[3].position
        self.pull_to_top(card)
        
        card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
        self.piles[2].append(card)
        card.position = self.pile_mat_list[2].position
        self.pull_to_top(card)

        card = self.piles[BOTTOM_FACE_DOWN_PILE].pop()
        self.piles[1].append(card)
        card.position = self.pile_mat_list[1].position
        self.pull_to_top(card)

        # Flip up the top cards
        #for i in range(PLAY_PILE_1, PLAY_PILE_30 + 1):
            #self.piles[i][-1].face_up()

        self.piles[3][-1].face_up()
        self.piles[2][-1].face_up()
        self.piles[1][-1].face_up()
        self.piles[0][-1].face_up()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the mats the cards go on to
        self.pile_mat_list.draw()

        # Draw the cards
        self.card_list.draw()

        output = f"{self.board_view.King_Of_Clubs}"
        arcade.draw_text(output, 27, 80, arcade.color.WHITE, 14)

        output = f"{self.board_view.Queen_Of_Diamonds}"
        arcade.draw_text(output, 27 + X_SPACING, 80, arcade.color.WHITE, 14)

        output = f"{self.board_view.Jack_Of_Spades}"
        arcade.draw_text(output, 27 + X_SPACING + X_SPACING, 80, arcade.color.WHITE, 14)

        arcade.draw_text("Question", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        if self.answer == True:
            arcade.draw_text("Answer", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2-75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def pull_to_top(self, card):
        """ Pull card to top of rendering order (last to render, looks on-top) """
        # Find the index of the card
        index = self.card_list.index(card)
        # Loop and pull all the other cards down towards the zero end
        for i in range(index, len(self.card_list) - 1):
            self.card_list[i] = self.card_list[i + 1]
        # Put this card at the right-side/top/size of list
        self.card_list[len(self.card_list) - 1] = card

    def on_key_press(self, symbol: int, modifiers: int):
        """ User presses key """
        if symbol == arcade.key.SPACE:
            # Restart
            
            self.answer = True

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get list of cards we've clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        # Have we clicked on a card?
        if len(cards) > 0:

            # Might be a stack of cards, get the top one
            primary_card = cards[-1]
            
            # Figure out what pile the card is in
            pile_index = self.get_pile_for_card(primary_card)
            #game_view = BoardView()
            #game_view.setup()
            if primary_card.suit == "Clubs":
                self.board_view.King_Of_Clubs += self.board_view.points
            
            elif primary_card.suit == "Diamonds":
                self.board_view.Queen_Of_Diamonds += self.board_view.points
            
            elif primary_card.suit == "Spades":
                self.board_view.Jack_Of_Spades += self.board_view.points    

            self.window.show_view(self.board_view)

            # Are we clicking on the bottom deck, to flip three cards?
            """ if pile_index == BOTTOM_FACE_DOWN_PILE:
                # Flip three cards
                for i in range(3):
                    # If we ran out of cards, stop
                    if len(self.piles[BOTTOM_FACE_DOWN_PILE]) == 0:
                        break
                    # Get top card
                    card = self.piles[BOTTOM_FACE_DOWN_PILE][-1]
                    # Flip face up
                    card.face_up()
                    # Move card position to bottom-right face up pile
                    card.position = self.pile_mat_list[BOTTOM_FACE_UP_PILE].position
                    # Remove card from face down pile
                    self.piles[BOTTOM_FACE_DOWN_PILE].remove(card)
                    # Move card to face up list
                    self.piles[BOTTOM_FACE_UP_PILE].append(card)
                    # Put on top draw-order wise
                    self.pull_to_top(card)

            elif primary_card.is_face_down:
                # Is the card face down? In one of those middle 7 piles? Then flip up
                primary_card.face_up()
            else:
                # All other cases, grab the face-up card we are clicking on
                self.held_cards = [primary_card]
                # Save the position
                self.held_cards_original_position = [self.held_cards[0].position]
                # Put on top in drawing order
                self.pull_to_top(self.held_cards[0])

                # Is this a stack of cards? If so, grab the other cards too
                card_index = self.piles[pile_index].index(primary_card)
                for i in range(card_index + 1, len(self.piles[pile_index])):
                    card = self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_original_position.append(card.position)
                    self.pull_to_top(card)

        else:

            # Click on a mat instead of a card?
            mats = arcade.get_sprites_at_point((x, y), self.pile_mat_list)

            if len(mats) > 0:
                mat = mats[0]
                mat_index = self.pile_mat_list.index(mat)

                # Is it our turned over flip mat? and no cards on it?
                if mat_index == BOTTOM_FACE_DOWN_PILE and len(self.piles[BOTTOM_FACE_DOWN_PILE]) == 0:
                    # Flip the deck back over so we can restart
                    temp_list = self.piles[BOTTOM_FACE_UP_PILE].copy()
                    for card in reversed(temp_list):
                        card.face_down()
                        self.piles[BOTTOM_FACE_UP_PILE].remove(card)
                        self.piles[BOTTOM_FACE_DOWN_PILE].append(card)
                        card.position = self.pile_mat_list[BOTTOM_FACE_DOWN_PILE].position """

    def remove_card_from_pile(self, card):
        """ Remove card from whatever pile it was in. """
        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def get_pile_for_card(self, card):
        """ What pile is this card in? """
        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def move_card_to_new_pile(self, card, pile_index):
        """ Move the card to a new pile """
        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

    def on_mouse_release(self, x: float, y: float, button: int,
                         modifiers: int):
        """ Called when the user presses a mouse button. """

        # If we don't have any cards, who cares
        if len(self.held_cards) == 0:
            return

        # Find the closest pile, in case we are in contact with more than one
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_mat_list)
        reset_position = True

        # See if we are in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):

            # What pile is it?
            pile_index = self.pile_mat_list.index(pile)

            #  Is it the same pile we came from?
            if pile_index == self.get_pile_for_card(self.held_cards[0]):
                # If so, who cares. We'll just reset our position.
                pass

            # Is it on a middle play pile?
            elif PLAY_PILE_1 <= pile_index <= PLAY_PILE_7:
                # Are there already cards there?
                if len(self.piles[pile_index]) > 0:
                    # Move cards to proper position
                    top_card = self.piles[pile_index][-1]
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                                                top_card.center_y - CARD_VERTICAL_OFFSET * (i + 1)
                else:
                    # Are there no cards in the middle play pile?
                    for i, dropped_card in enumerate(self.held_cards):
                        # Move cards to proper position
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - CARD_VERTICAL_OFFSET * i

                for card in self.held_cards:
                    # Cards are in the right position, but we need to move them to the right list
                    self.move_card_to_new_pile(card, pile_index)

                # Success, don't reset position of cards
                reset_position = False

            # Release on top play pile? And only one card held?
            elif TOP_PILE_1 <= pile_index <= TOP_PILE_4 and len(self.held_cards) == 1:
                # Move position of card to pile
                self.held_cards[0].position = pile.position
                # Move card to card list
                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

        if reset_position:
            # Where-ever we were dropped, it wasn't valid. Reset the each card's position
            # to its original spot.
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_original_position[pile_index]

        # We are no longer holding cards
        self.held_cards = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If we are holding cards, move them with the mouse
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    start_view = BoardView()
    window.show_view(start_view)
    #start_view.setup()
    arcade.run()


if __name__ == "__main__":
    main()