# VIVI

<img src="/assets/vivi.png" alt="image of vivi" width=200>

Vivi is a voicebot based virtual assistant inspired by JARVIS

My initial thought of this project is to model or improve a NLU process that will be able to utilize database as a form of "memory" similar to a human brain, and to provide a more 'humanized' reply (instead of hard coding replies). Conversations and parameters that are conversed will be remembered and replaced in the 'Least Used' rule after a period of time. In addition, I also thought of providing a personality to the bot (the way it speaks and also a very crucial aspect -- VOICE + TONE!). 

These ideas were great, but it is not very feasible with my short amount of time (given by myself). Therefore, I decided to utilize the current resources that are available and make a 'quick' and 'dirty' vivi bot.

Stages of vivi:
- [x] Create a base program for vivi
- [x] Connecting to a database
- [x] Connecting to Dialogflow
- [ ] Provide task specific functions



### Create a base program for Vivi
Main purpose of this first part was to create a base program that will be able to listen (microphone), and convert it into text (SpeechRecognition library).

Code used: `main.py`

### Connecting to a database
Since I'm using mac, I decided to use PostgreSQL (I'm using that for another project as well). No need much justification on this! Just google it and you'll know why :)

Code used: `databaseQuery.py` and `config.py` (P/S: I did not write this from scratch)

### Connecting to Dialogflow
I started knowing dialogflow when I was working on a Minnesota State Project (helping to develop chatbot for the MN state system universities), and thus, I know how easy and powerful it is! Instead of creating my own model of NLU, I decided that perhaps this might be a quicker way (quicker by alot too). Their model is pretty developed and honestly, I have no confidence that I will be able to train a model much 'intelligent' than that in a short time (given limited processing power and data). Plus, having to clean data and get it ready for the model takes time too.

The role of dialogflow here would be detecting the 'meaning' of my sentence/query, and returning a reply that consist of returning text, action, and parameter. Action and parameter will help to perform the different tasks (as a virtual assistant). Dialogflow will take care of the 'voicebot/chatbot' aspect of Vivi.

Code used: `dialogflow.py`

### Provide task specific function
The ultimate goal here is to create a more 'intelligent' virtual assistant that work similarly to a voicebot. Based on the actions and parameters returned from dialogflow, vivi can ultimately select the specific task to carry out (for example, open google / search president of united states / open gmail etc). This part is simple, consisting of the usual if, else-if statement. Simply google "virtual assistant with python" and you will be able to find a lot of examples. 

The alternative way of making it more 'intelligent' would be supervised learning? by providing tons of statements(input) and actions taken (output). But since the action that I am looking for is limited, the if-else statement would be sufficient. 
###### _Maybe I'll get bored one day and start writing the model?_

Code used: `tasks.py`



## Obstacles and Challenges 
#### Mac x VSCode x Python

&ensp; I don't want to run it in python IDLE and couldn't find a better text editor at that time, so I resolve into VSCode. Editing in it was okay until I am trying to run the program. *I CAN'T ACTIVATE MY MICROPHONE.* Well, I thought it was a problem with VSCode and tried using my friend's Windows laptop but it was working perfectly fine. I tried looking into System Preference and there was no option to "allow microphone usage in VSCode".

&ensp; Eventually I found a trick -- running VSCode as an admin and bypass permission `sudo /Applications/Visual\ Studio\ Code.app/Contents/MacOS/Electron`. I was able to run it! Hoola. But there always possessed a type of 'risk' associated when you bypass permission (I guess?), so it was not a good idea anyway. 

&ensp; I stopped using VSCode for this project now. I started utilizing `vim` and it is working great so far! (of course, with some `.vimrc` configurations) We'll see how it goes!

#### Conda x Python Packages

&ensp; Probably a lot of people have the same issue as me -- by having multiple versions of Python in my local that is getting out of control. Much worst, I also have conda within my local! pip3 install and pip install is either with 1 of the python version (2 or 3), or within one of the conda environment.

&ensp; I started getting into conda when one of the project was using it. I installed based on instructions (without understanding it), and it kinda messed up my local...? (at least that's what I'm feeling). At some point, I decided to understand conda and create an environment for vivi. Everything worked well until..... I have to install dialogflow. Apparently, dialogflow isn't an official python package(?) and thus, I can't install it within the conda environment. I tried looking for alternative and everything is getting back to step 0.

&ensp; I have to say, I gave up on conda.. haha! Now I'm developing through vim, and managing python packages + versions through `pyenv` and `direnv`.
