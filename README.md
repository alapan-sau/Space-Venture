# Space Venture 

# Introduction
Space venture is a multiplayer game developed in Python 3.6 using the Pygame 1.9.6
Library. The main objective of the game is to reach the other side of the game arena. The winner is declared based on the time taken to reach the other end and the obstacles crossed.

# Instruction Manual

The game is only key-based. One player appears after the other player dies automatically with a delay of one second. The keys to move the players are as follows:
<kbd>Up</kbd>,<kbd>Down</kbd>,<kbd>Left</kbd>,<kbd>Right</kbd> keys  are used to move the players in the arena.

# Scoring

Player1 and Player2 play in alternate turns.The points gained would depend on the obstacles crossed ( their speed if they are moving ) and time taken. The score for crossing a moving obstacle is five times its speed and that of each static obstacle is fixed at 5 per obstacle

The scoring algorithm is as follows:

`obstacle_score += speed_of_moving_obstacle * 10`
`obstacle_score += 20 (static)`

`total_score = obstacle_score + 10000/time`

It is taken care such that the time would never contribute to negative score

# Winning

The player wins depending on the total score of the player when he reaches the other end. The player having the highest score wins. Incase one of the player dies, the other player wins, provided he/she reaches the bank. If both the players die, the game is drawn.
It must also be noted that the speed of the moving obstacles increases for the player who wins the game. Consequently, the score he would get for crossing a moving obstacle would also be higher.

# Image References

- Player Icons from flaticons.com
- The space background image from shutterstoc.com

# Author

- Alapan Sau