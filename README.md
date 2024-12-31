# Minesweeper Solver using logic programming (swi-prolog)
## Descripton
this project solves a minesweeper board on [MinesweeperOnline website](https://minesweeperonline.com/#) using logic programming with the help of selenium.

![](https://github.com/Reynardd/MineSweeperSolver/blob/main/sample.gif)

this project was written as the final project for AI Course in IUT.
## How to run
clone the repository

install python dependencies

```pip install selenium chromedriver_autoinstaller janus_swi```

install [swi-prolog](https://www.swi-prolog.org/)

execute main.py

```python3 main.py```

enjoy :)

## Known problems
sometimes importing janus_swi in windows encounters ```FATAL ERROR: Could not find system resources```

to solve the issue try these:

[DLL file missing](https://www.swi-prolog.org/FAQ/FindResources.md)

in cmd: ```setx SWI_HOME_DIR "C:\Program Files\swipl"``` 
