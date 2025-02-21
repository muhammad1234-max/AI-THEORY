## statement 1: False
An agent with partial observability can still be perfectly rational if it makes optimal decisions based on the information available to it. For example, a Poker-playing AI does not have full information about the opponent's cards but can still make the best possible decision using probabilistic reasoning. Similarly, self-driving cars operate with limited sensor data but use predictive models to navigate safely.

## statement 2 : True
A pure reflex agent acts solely based on current sensor inputs without maintaining an internal state. In dynamic or partially observable environments, reflex agents fail to make rational decisions. For example, in chess, a reflex agent that chooses moves based only on the current board position (without considering the game’s history or future consequences) would perform poorly. More generally, in robot navigation with hidden obstacles, a pure reflex agent would repeatedly crash if it only reacted to immediate sensor readings without maintaining a memory of past movements.

## statement 3 : False
Not every agent in a given environment will behave rationally, as rationality depends on the performance measure and decision-making strategy. For instance, in tic-tac-toe, an agent that randomly places moves without considering the opponent's strategy is irrational, whereas a minimax-based agent plays optimally. In most environments, there exist both rational and irrational agents, so it is impossible for every agent to be rational.

## statement 4 : False
The agent function maps from percept histories to actions, while the agent program is an implementation of this function. The agent program processes sensor inputs and maintains an internal state before selecting an action. For example, in a robot vacuum cleaner, the agent program receives raw sensor data (like dust levels, obstacles) but also uses internal logic (like map memory). The agent function, on the other hand, represents the abstract mathematical mapping from all possible percept histories to actions.

## statement 5 : False
There are infinitely many possible agent functions, but not all can be implemented. Some agent functions require unlimited memory or computation, making them impractical. For example, an agent function that computes an optimal strategy for an arbitrarily large chessboard would require infinite computational power. Theoretical models such as Turing machines show that some functions are non-computable, proving that not all agent functions are implementable.

## statement 6 : True
If the performance measure in a given environment values randomness, then a random agent can be rational. For example, in a game of rock-paper-scissors against a human opponent, playing uniformly at random is a rational strategy since it prevents the opponent from predicting moves. Similarly, in some exploration tasks (e.g., a robot searching for a hidden object), random movement might be a viable strategy if no prior information exists

## statement 7 : True
If an agent follows an optimal decision-making strategy, it can be perfectly rational in multiple environments. For example, a chess-playing agent using minimax with perfect evaluation is rational in both a standard chess game and a variant with different board sizes, as long as the rules remain similar. Similarly, a sorting algorithm agent that optimally sorts data is rational in multiple environments where sorting is required, regardless of input size.







