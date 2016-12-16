# Conway's Game of Life
A presentation for 6CS008 (Computation and Complexity) at the University of Wolverhampton

<img src="https://raw.githubusercontent.com/marcuskainth/game_of_life/master/gol.gif" width="320px" height="320px" />

## Introduction
A Python implementation of Conway's Game of Life using matplotlib to demonstrate the rules.

## Usage
Fairly simple to implement in other projects, you can use this code with/without matplotlib, just remove the animation lines. However, if you'd like to see it in action, simply clone the repository and run from the Draw class. You can find the code below on how to initialise drawing.

```python
draw = Draw(Pattern.Random)
draw.run()
```

### Patterns
Various patterns are hard-coded into the project, these are listed below

```python
class Pattern(Enum):
    Random = 0
    Gun = 1
    StillLife = 2
    Oscillator = 3
    Glider = 4
    Spaceship = 5
```

## Authors
Created for University of Wolverhampton ([wlv.ac.uk](http://www.wlv.ac.uk)) by:

[Marcus Kainth](https://www.marcuskainth.co.uk), [@marcuskainth](https://github.com/marcuskainth)

Joaquin Delgado, [@JoaquinDF](https://github.com/JoaquinDF)

Adam Bolton, [@ADAMRNBOLTON](https://github.com/ADAMRNBOLTON)
