# rock-paperscissors

A game of wits for gents and scholars. 

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+

## Setup

Optionally fork this [remote repository](https://github.com/kneelanda/rock-paperscissors), to create a copy under your own control. Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop. Then navigate to wherever you downloaded the repo:

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/rock-paperscissors
```

Create and activate your virtual environment:

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

## Player Types

When you play games, there will be a human and computer player. Descriptions below.

player type(s) | description
--- | ---
`HUMAN` | A human player who will input their selections.
`COMPUTER` | A computer player which makes random selections.

## Usage

### Game Play

Play a game:

```sh
python game.py
```

## Demo

Here are some demonstrations of what gameplay looks like:

Example 1: 
--->> python game.py
Welcome to 'Rock, Paper, Scissors, Shoot!'
Please make a choice('rock','paper','scissors'): rock
You chose: rock
The computer chose: rock
It's a tie!


Example 2:
--->> python game.py
Welcome to 'Rock, Paper, Scissors, Shoot!'
Please make a choice('rock','paper','scissors'): rock
You chose: rock
The computer chose: paper
Paper covers rock. You lose. It's ok, try again!

Example 3:
--->> python game.py 
Welcome to 'Rock, Paper, Scissors, Shoot!'
Please make a choice('rock','paper','scissors'): rock
You chose: rock
The computer chose: scissors
Rock crushes scissors. You win! Thanks for playing. Feel free to play again!


## **Note - much of this README file was adapted from the tic-tac-toe example provided from professor rossetti