# Project-Search
A personal first foray into GUI apps in python with an app that searches for project folders within a set parent folder. 

The goal is to develop a simple application that can be run with keyboard shortcuts to quickly open folders that are saved in a single location and are saved with a common naming convention. This is my first exploration of the tkinter library and my first "application" with python.

The current build is designed for windows systems. The executable and settings file are located in the `dist` folder. To run place both items within the same folder. Use the `settings.json` file to direct to your root file path and select the hotkey combination you would like to use. Run `Project_Search_ex.exe` to run the applicaiton in the background. It will be pulled up when using the hotkey combination selected which defaults to `ctrl` + `alt` + `p`. 

If you would like the app to run on startup, create a shortcut and place this in your `Startup` programs folder.
