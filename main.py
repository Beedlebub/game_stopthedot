def on_button_pressed_a():
    if sprite.get(LedSpriteProperty.X) == 2:
        game.add_score(1)
    else:
        game.game_over()
    basic.show_string("Score" + str(game.score()))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

sprite: game.LedSprite = None
sprite = game.create_sprite(2, 2)
game.set_score(0)

def on_forever():
    sprite.move(1)
    sprite.if_on_edge_bounce()
    basic.pause(200)
basic.forever(on_forever)
