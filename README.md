# Chess Ai
In this project we will be building a AI chess bot that learns how to play chess better as it plays more chess games.

We've bulit on top of a basic 2-player chess program built by Jernej Henigman. Find out more about it here: https://github.com/JernejHenigman/Chess

## Added features
...

To run game, you must have Pygame installed. If you need to install, navigate to folder containing ChessBoard.py and run:  
python3 -m pip install -U pygame --user  
python ChessBoard.py


The Game:

Simplified so that the ai is always black

aggressivness logic:
    if the bot loses and it has alot of valuable pieces it should prioritize protecting its king more

    if the bot loses and the enemy has lots of valuable pieces it should prioritise capturing valuable pieces more 

    if the bot loses and the enemy has no valuabkle pieces it should prioritise capturing the king more 

    if the bot loses and it doesnt have alot of valuable pieces it prioritizes protecting its pieces more 

    do this for specific pieces for instance if loosing queen leads to losses value queen more 

    every time it looses, it checks the pieces it lost and values them more 

    over time the increment by which you change how you value the pieces is related to the amount of games in it's experience (or victories), 
    we should have a variable that represents this and decays logorithmicsally (or something)
    
    the reason why we might want this to change with victories, instead of experience is that we want radicall changes in strategy when the bot cant win.
    100 loses doesnt imply we are arriving at the ideal strategy so why would we pretend we are getting closer to the goal in that case


    the bot needs to be able to choose random moves

    needs to evaluate how much the kings can move

    if the king is in check protecting the king is the absolute priority  

    it needs to evaluate which pieces of its own are in danger

    it needs to evaluat  which pieces of the enemies can be attacked 

    it needs to be able to change the value of the move based on its how much closer the move leads to capturing a valuable piece, constraining the king, protecting our king, protecting valuable pieces

    if ever moves are equal, choose randomly 

    it needs to be able to look atleast 2 moves ahead

    upon loss it needs to evaluate its appraoach, change theweights of the values and the size of the incrementor (by the comparing the # of losses to victories)

    If we had more time an interesting case to pursue would be having the chess bot play itself with varying values for its pieces besides the predefined values we gave. We could compare which values resulted in winning most often.