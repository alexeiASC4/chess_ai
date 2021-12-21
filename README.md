# Chess Bot
In this project, we will build a chess bot that chooses the best move possible based on varying depths in its game tree search. We've set the bot to always play black. We've bulit on top of a basic 2 human-input chess program built by Jernej Henigman. Find out more about it here: https://github.com/JernejHenigman/Chess

### To run game:
Clone this repository. Then, navigate to folder containing ChessBoard.py and run:

    python3 -m pip install -U pygame --user  
    python ChessBoard.py

## Our Changes to Base Game
* Changed colors of chess board to classic chess colors
* Notified user who won
* Added bot that chooses moves for black pieces
* Added game tree search logic:
    * Bot looks at all possible moves it can make, then analyzes how its opponent can best respond to each move. It will then pick the move that results in the best outcome. The best outcome is decided by how many of its opponents pieces it takes, while preserving its pieces, and getting close to checkmate. It can do this for varying levels of depth in the search tree. 

## Ideas for Further Development
* If we had more time an interesting case to pursue would be having the chess bot play itself with varying values for its pieces besides the predefined values we gave. We could compare which values resulted in winning most often.  

* Additonally, if we gave the bot memory, the bot could change its own behavior, like varying its level of aggression. For example:
    *  if the bot loses and it has alot of valuable pieces it should prioritize protecting its king more
    *  if the bot loses and the enemy has lots of valuable pieces it should prioritise capturing valuable pieces more 
    *  if the bot loses and it doesnt have a lot of valuable pieces it prioritizes protecting its pieces more (can do this for specific pieces, for instance, if losing queen leads to losses, value queen more)
* Make bot more user-friendly
    * Have different modes of difficulty for the game. (Easy mode could be random moves by the bot, medium could be the bot using a single level of the game tree, and so on)
  
*Authors: 
Alexei Tulloch, Ayende Chand
