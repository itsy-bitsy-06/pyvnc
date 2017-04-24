# Caesg

Provides an interactive shell for vnc connection automation.

```
  # To run an interactive shell
  cd Src
  python shell.py
  help
  connect --host=10.10.10.10 --display=1 --password=xyz
  typekeys --string=ls
  screeshot
  exit
```

The commands can also be loaded into a script file and run in batch mode.

```
  cd Src
  python shell.py script.caesg.txt
  
```
