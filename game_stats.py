class GameStats():
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = open(self.settings.name_file, "r").read()
        self.high_score = 0 if self.high_score == "" else int(self.high_score)
        #if self.high_score == "":
         #   self.high_score = 0

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1