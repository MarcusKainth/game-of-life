# Conway's Game of Life
A presentation for 6CS008 (Computation and Complexity) at the University of Wolverhampton.

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
Various patterns are hard-coded into the project, these are listed below.

```python
class Pattern(Enum):
    Random = 0
    Gun = 1
    StillLife = 2
    Oscillator = 3
    Glider = 4
    Spaceship = 5
```

## Requirements
- Python 3.4+
- Numpy
- Matplotlib

The project has been tested on Python 3.5.2 but in theory should work from version 3.4 and later as enumeration is used.

It's possible to get the project to work on Python 2.7+ by not using enumeration.

## Authors
Created for [University of Wolverhampton](https://www.wlv.ac.uk) [Computer Science](https://www.wlv.ac.uk/about-us/our-schools-and-institutes/faculty-of-science-and-engineering/school-of-mathematics-and-computer-science/) module 6CS008 by:

[Marcus Kainth](https://www.marcuskainth.co.uk), [@marcuskainth](https://github.com/marcuskainth)

Joaquin Delgado, [@JoaquinDF](https://github.com/JoaquinDF)

Adam Bolton, [@ADAMRNBOLTON](https://github.com/ADAMRNBOLTON)
