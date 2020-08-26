input.onButtonPressed(Button.A, function () {
    if (sprite.get(LedSpriteProperty.X) == 2) {
        game.addScore(1)
    } else {
        game.gameOver()
    }
    basic.showString("Score" + ("" + game.score()))
})
input.onButtonPressed(Button.AB, function () {
    control.reset()
})
let sprite: game.LedSprite = null
sprite = game.createSprite(2, 2)
game.setScore(0)
basic.forever(function () {
    sprite.move(1)
    sprite.ifOnEdgeBounce()
    basic.pause(200)
})
