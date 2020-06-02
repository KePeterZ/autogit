import os, sys # Only library needed

def setup():
  # First time, setup autoGit.
  print("Initiating setup.")
  # Ask if user wants to install cron
  if input("Would you like to install cron now? [no]: ")=="y":
    os.system("sudo apt install cron")
  print("How often would you like to commit?")
  commitTimes = input("[in minutes, default is 10]: ")
  commitTimes = 10 if commitTimes=="" else int(commitTimes)
  # print(commitTimes)
  print("Would you like to enable auto-push?")
  pushTimes = input("[enter in minutes, press ENTER if you don't want to enable it]: ")
  if pushTimes!="":
    pushTimes = int(pushTimes)
  else:
    pushTimes = False
  print("That's all I needed. Now I'll create the cron-jobs.")
  # Create cronjobs here

args = sys.argv
if "push" in args:
  commitName = "autopush from AutoGit"
  os.system("git commit -am '%s'" % commitName)
  os.system("git push origin master")
elif "commit" in args:
  commitName = "autopush from AutoGit"
  os.system("git commit -am '%s'" % commitName)
elif "rm" in args:
  # Remove cronjobs here
  pass
else:
  setup()