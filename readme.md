# AutoGit
### Because there needed to be one more.

## Just.. why?
I have a habit, of.. not saving stuff. Until I started using Git, it really annoyed me. But then, I had to commit most of the time, just to put it on `origin`.  
But then I thought: what if the program committed itself when I changed it?

## And then, AutoGit was born.
It's a simple tool, that you download once, set it up, and then just forget about it. 

## But why should **I** use it?
Because you most likely don't like losing code. Or just don't like commiting every 10 minutes. Or just want to feel safe, that your code is saved and on the cloud, whatever the case might be. 

## But how does it work?
The first time you set it up, it creates a git repository in the folder, using `git init`. Throughout the setup, you'll be able to choose what you want to enable, such as: 
* what names and descriptions the commits should use
* setting up the `origin` of the repo
* how often it should `git commit`
* if and how often it should `git push`.
Scheduling commits and pushes is done with `cron` (which the setup will install if it's not already). Basically, it creates a cron task for commits and pushes seperately, but using the same script. That script will contain every aspect of the backup system, which you can change after the setup, if you desire.

## Alright, you convinced me. How should I get started?
Step 1: git clone this repo.  
Step 2: run the autogit.py script in the folder you want to mark for autogit. 
Step 3: go through the setup process.

And that's it! You know have enabled auto-commits and pushes to your choice of Git solution. 

## I don't like Autogit anymore. How do I remove it? 
Well, I'm sorry to hear that, but it's quite easy. Just run `./autogit.py -rm` and it will remove every cronjob, and any trace of itself. However, you should make a backup of `autogit.py` before deleting, because in the case you change your mind, you can just `./autogit.py -back` and automatic commits and pushes will go back how they used to be. 

# KePeterZ, 2020