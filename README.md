# DayZLockPick

### Small tool to emulate a keyboard to crack the password of the combination locks in DayZ.

<div align="center">
<img src="https://static.wikia.nocookie.net/dayz_gamepedia/images/5/5b/CombinationLock.png/revision/latest/scale-to-width-down/300?cb=20181213204531" />
</div>

## Project Stack

<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a>

## Supported Platforms

<a href="https://www.microsoft.com/en-us" target="_blank" rel="noreferrer">
        <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/windows8/windows8-original.svg" alt="windows" width="35" height="35"/>
</a>

## Setup & Run Project

#### Make sure to have [Python](https://www.python.org/downloads/) installed on your computer.

### Config
#### In a text editor you can edit `AwesomeKey` and `TimeBeforeStart` vars in `lockpick.py`.

`AwesomeKey` must be the [hex value](https://web.archive.org/web/20190801085838/http://www.gamespp.com/directx/directInputKeyboardScanCodes.html) of your interact key in Dayz. 
- By Default key is `F`

`TimeBeforeStart` is the time in seconds before starting emulate your keyboard.
- By Default the value is `4` seconds.

### Then in DayZ after finding a hidden combination lock :

- Put your cursor on the last slot.
- Reset this last slot to 0.

<img src="https://github.com/Chep0x61/DayZLockPick/blob/main/.github/assets/combinationlock.jpg?raw=true" /> 

### Finally you can run the project :

```bash
python lockpick.py
```

## Contributors

| [<img src="https://github.com/Chep0x61.png?size=85" width=85><br><sub>Chep0x61</sub>](https://github.com/Chep0x61) | 
:---: 

#### I hope this ReadMe was useful ! :heart:
