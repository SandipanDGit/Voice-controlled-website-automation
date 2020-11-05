# Voice-controlled-website-automation
This is a voice controlled automation of a chess website https://lichess.org/

How it works: 
1. The program upon running, opens a new window of mozilla firefox and opens lichess.org
2. system asks for login permission with preset values (currently set to one of my personal dummy account credentials)
  where user need to type 'y' in the terminal (this is going to be voice controlled, but not wired up as of now)
3. The script uses selenium webdriver to control the browser activity automatically
4. the user is now supposed to speak the time format of the game that it wants to start
   This is recorded and sent to google voice recogniton API for recognition in text
5. The text is parsed, formatted and fed into selenium to make the game start in the browser by simulating a click at required position
6. The game starts
7. Now the user is supposed to speak the next chess move in common english with that corresponds to a chess notation
8. The speech is recorded, decoded by Google API
9. It is parsed and reformatted into a chess notation
10. It is validated as a chess notation using regex
11. The final chess notation is fed into selenium to be typed in the chess move slot in the website

**The user always has the liberty to use normal mouse move when things doesn't work out

platform requirements : 
1. Python should be installed
  1.1. Third party module : SpeechRecognition
  1.2. Third party module : selenium
    
3. geckodriver.log v0.26.0 should be installed 
4. Mozilla firefox browser should be installed

Entry point : master.py

There are few changes to be done for this script to run in your machine. I'll be making the changes ASAP. Stay tuned.
