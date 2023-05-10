from pygame import mixer

class settings:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        #self.ship_speed = 1.5
        self.ship_limit = 2

        #self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #self.alien_speed = 1.0

        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, -1 влево
        #self.fleet_direction = 1
        self.speedup_scale = 1.1

        self.score_scale = 1.5
        self.name_file = "record.txt"

        self.initialize_dynamic_settings()
        self.sound_fire = mixer.Sound("content_sndLaser.wav")
        self.sound_fire.set_volume(0.05)
        self.sound_explode = mixer.Sound("odinochnyiy-vzryiv.wav")
        self.sound_explode.set_volume(0.1)
        self.sound_start = mixer.Sound("content_sndBtnDown.wav")
        self.sound_start.set_volume(0.3)

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)