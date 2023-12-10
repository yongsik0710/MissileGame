import os


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Options:
    class Video:
        display_resolution = [1920, 1080]

    class Audio:
        volume = 1.0


class Resources:
    class Fonts:
        font = resource_path("Fonts/LINESeedKR-Bd.ttf")

    class Sounds:
        class Music:
            lobby = resource_path("Sounds/Background/lobby.wav")
            stage_1 = resource_path("Sounds/Background/stage_1.wav")
            stage_2 = resource_path("Sounds/Background/stage_2.wav")
            stage_3 = resource_path("Sounds/Background/stage_3.wav")
            stage_4 = resource_path("Sounds/Background/stage_4.wav")

        class Cannon:
            class Basic:
                shoot = resource_path("Sounds/Cannon/Basic/shoot.wav")
                damage = resource_path("Sounds/Cannon/Basic/damage.wav")
                barrel_move = resource_path("Sounds/Cannon/Basic/barrel_move.wav")
                move = resource_path("Sounds/Cannon/Basic/move.wav")
                burning = resource_path("Sounds/Cannon/Basic/burning.wav")

            class Ballista:
                shoot = resource_path("Sounds/Cannon/Ballista/shoot.wav")
                damage = resource_path("Sounds/Cannon/Ballista/damage.wav")
                barrel_move = resource_path("Sounds/Cannon/Ballista/barrel_move.wav")
                move = resource_path("Sounds/Cannon/Ballista/move.wav")
                burning = resource_path("Sounds/Cannon/Ballista/burning.wav")

            class FlameCannon:
                shoot = resource_path("Sounds/Cannon/FlameCannon/shoot.wav")
                damage = resource_path("Sounds/Cannon/FlameCannon/damage.wav")
                barrel_move = resource_path("Sounds/Cannon/FlameCannon/barrel_move.wav")
                move = resource_path("Sounds/Cannon/FlameCannon/move.wav")
                burning = resource_path("Sounds/Cannon/FlameCannon/burning.wav")

            class Catapult:
                shoot = resource_path("Sounds/Cannon/Catapult/shoot.wav")
                damage = resource_path("Sounds/Cannon/Catapult/damage.wav")
                barrel_move = resource_path("Sounds/Cannon/Catapult/barrel_move.wav")
                move = resource_path("Sounds/Cannon/Catapult/move.wav")
                burning = resource_path("Sounds/Cannon/Catapult/burning.wav")

            class Tank:
                shoot = resource_path("Sounds/Cannon/Tank/shoot.wav")
                damage = resource_path("Sounds/Cannon/Tank/damage.wav")
                barrel_move = resource_path("Sounds/Cannon/Tank/barrel_move.wav")
                move = resource_path("Sounds/Cannon/Tank/move.wav")
                burning = resource_path("Sounds/Cannon/Tank/burning.wav")

        class Shell:
            class Basic:
                explode = resource_path("Sounds/Shell/Basic/explode.wav")

            class Arrow:
                explode = resource_path("Sounds/Shell/Arrow/explode.wav")

            class Fireball:
                explode = resource_path("Sounds/Shell/Fireball/explode.wav")

            class Stone:
                explode = resource_path("Sounds/Shell/Stone/explode.wav")

            class Missile:
                explode = resource_path("Sounds/Shell/Missile/explode.wav")

        class Util:
            class Button:
                mouse_on = resource_path("Sounds/Util/mouse_on.wav")
                click = resource_path("Sounds/Util/click.wav")

    class Texture:
        class Effects:
            explosion_1 = resource_path("Images/Effects/explosion_1.png")
            explosion_2 = resource_path("Images/Effects/explosion_2.png")

            fire = resource_path("Images/Effects/fire.png")

        class Util:
            current_player = resource_path("Images/Utilities/current_player.png")

        class Levels:
            class Level1:
                level_image = resource_path("Images/Levels/level_1.png")
                background_image = resource_path("Images/Backgrounds/level_1.png")

            class Level2:
                level_image = resource_path("Images/Levels/level_2.png")
                background_image = resource_path("Images/Backgrounds/level_2.png")

            class Level3:
                level_image = resource_path("Images/Levels/level_3.png")
                background_image = resource_path("Images/Backgrounds/level_3.png")

            class Level4:
                level_image = resource_path("Images/Levels/level_4.png")
                background_image = resource_path("Images/Backgrounds/level_4.png")

        class Cannons:
            class Barrel:
                basic_barrel = resource_path("Images/Cannons/Basic/barrel.png")
                ballista_barrel = resource_path("Images/Cannons/Ballista/barrel.png")
                flame_cannon_barrel = resource_path("Images/Cannons/FlameCannon/barrel.png")
                catapult_barrel = resource_path("Images/Cannons/Catapult/barrel.png")
                tank_barrel = resource_path("Images/Cannons/Tank/barrel.png")

            class Body:
                catapult_body = resource_path("Images/Cannons/Catapult/body.png")
                tank_body = resource_path("Images/Cannons/Tank/body.png")

            class Wheel:
                basic_wheel = resource_path("Images/Cannons/Basic/wheel.png")
                ballista_wheel = resource_path("Images/Cannons/Ballista/wheel.png")
                flame_cannon_wheel = resource_path("Images/Cannons/FlameCannon/wheel.png")
                catapult_wheel = resource_path("Images/Cannons/Catapult/wheel.png")
                tank_wheel = resource_path("Images/Cannons/Tank/wheel.png")

        class Shells:
            basic = resource_path("Images/Shells/basic.png")
            arrow = resource_path("Images/Shells/arrow.png")
            fireball = resource_path("Images/Shells/fireball.png")
            stone = resource_path("Images/Shells/stone.png")
            missile = resource_path("Images/Shells/missile.png")
