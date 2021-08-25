# Insta Connection AI Bot
### ABOUT
Instagram is among one of the most used social networking  sites. It offers many features which makes it so popular among people. But one thing I wanted to do is to find my Connection to a particular person so by using that I can connect with that specific person with the help of my connections and my connection’s connection and so on. To find connection, Instagram offers only mutual connection i.e one person common between us.This problem can be seen as the informed search where we can take user as start, person to whom we are finding connection can be taken as goal and relations or connections can be taken as environment so to do this task I used Depth limit search on the list of people user follows then people followed by user’s following and so on. This problem can be solved completely and will always find the connection. The problem is, the number of  nodes or connections are in huge numbers which takes time and Instagram doesn't offer any API which has this tree structure.  
### REQUIRED DOWNLOADING AND INSTALLATION
- Python 3.9.0 installation
- Selenium install
- time install
- Webchrome driver install
### INPUTS NEEDED
- Your instagram username 
- Your instagram password
- Username of a person to whom you want to connect
- Max depth limit
- Max width limit(work best if width limit is less than 10)
- Path of chrome webdriver
### HOW TO RUN
Run with Python IDLE or 
To Run on Command prompt use py -i Insta Connection finder.py on folder's directory
