## Introduction
**Auto Mouse Scroller** is a python created program aimed for automating your mouse scroll without touching your mouse. It is created with the combination of other libraries with *pyautogui* as the main module. 
Auto Mouse Scroller is a open sourced reasearch concept that is created from simple python code lines making it easy for the newcomers to understand. 
Used Libraries are the following - 

    pyautogui 
    keyboard 
    time
Before you dive in to the program, it is recommended to [read the docs](https://pyautogui.readthedocs.io/en/latest/#fail-safes) of pyautogui so that you can get a good idea on how does it work.

Pyautogui documentation by [Al Sweigart](https://twitter.com/AlSweigart).
 Concept program is created by [@Black_2_white](https://twitter.com/Black_2_white).

## Inspiration
When I was reading a book in my laptop, I always had to scroll up and down the page. Just a few days after my test ended, I was reading a book called "The Pragmatic Programmer" while also having a sack of burrito on my other hand. <br> 
Turns out that having a burrito on a hand is uncomfortable while having to scroll the pages of the pdf. That lead me to the idea of Auto Mouse Scroller Project. I wanted to create a automated program that allowed me to read a book while also not ***even touching the mouse***. The outcome was beyond my expectation. That's what lead the project program to be here.

## How does it work?
The program at first requires an index from 1 to 4 to select the scrolling speed. After that, a alert window will come up notifying that the program will begin in 3 seconds after the 'OK' is clicked. The user needs to align the mouse position on the tab for the scrolling to work. 
Once the scrolling starts to work, it can be stopped using three ways. 
1. Using the Shift key on anywhere on the machine.
2. Using the Crtl+C on the terminal to trigger a keyboardInterrupt eliminating the program manually. 
3. Activating the failsafe by moving the mouse to one corner of the screen. [Check the docs](https://pyautogui.readthedocs.io/en/latest/#fail-safes).

## ⚠ Limitations ⚠
Auto Mouse Scroller is just a research concept demo. It is not an app or either a fully debugged program. These are the limitations of the program so far.

1. If the user gives an input of any other value except of 1 to 4 then the program starts to work without begin aborted. 
2. The code violates the D.R.Y concept. 
