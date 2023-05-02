//Q: Study the code snippet below:
  if (isDown(game, KEYS.A)) {
        this.sprite.body.angularVelocity = -5 * (this.speed / 1000)
      } else if (isDown(game, KEYS.D)) {
        this.sprite.body.angularVelocity = 5 * (this.speed / 1000)
      } else {
        this.sprite.body.angularVelocity = 0
      }

/*
Q: In your own words explain what the code is intended to achieve and how the code will achieve the intention.

A: Controls the sprites movements
*/

/*
Q: Create a short presentation to explain to your peers your answer.

A: Will be presented during the sprint.
*/