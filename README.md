# macboxx
A python script to give Boxx mappings to MacOS users for Dolphin emulator

## Requirements
In theory this works on any system with Python installed, but for now it's targeted at Mac users.

## Installation
```bash
$ git clone https://github.com/prmaloney/macboxx.git
$ cd macboxx
$ pip install -r requirements.txt
$ mv macboxx.py path/to/Slippi\ Dolphin.app/
```
The macboxx.py script needs to be in the same directory as your `Slippi Dolphin.app`. The commands above install the project, the required packages, and moves it to the same directory as Dolphin. 

## Usage
Run the following command in your terminal
```
$ python macboxx.py
```
This should open Dolphin and you can start your game.

## Customization
Right now, the customization is not fully formed. For now, you'll have to edit the python script yourself to adjust the keymaps as you see fit. This will be improved in the future.
