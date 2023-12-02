# Grab-Latest-ProtonGE-Script
Just a simple script for downloading and extracting the latest ProtonGE release for Steam
 
## Prerequisites

-  ProtonGE installed (see: [GloriousEggroll/proton-ge-custom#installation](https://github.com/GloriousEggroll/proton-ge-custom#installation))


## Install Steps
1.

      
      pip install tqdm requests
      mkdir ~/scripts
      wget https://raw.githubusercontent.com/thefinaldegree/Grab-Latest-ProtonGE-Script/main/GrabNewProtonGE.py
      chmod +x GrabNewProtonGE.py
      crontab -e
      

2. Now that we're in crontab, scroll to the bottom of the file and after any existing entries, include the following line:

      `0 0 * * 1 python3 /home/<USER>/scripts/GrabNewProtonGE.py`
   
      Note: To get your username, run the following in the terminal: `echo "$USER"`

3. To save, press `ctrl` + `X`


> [!NOTE]
> You will be prompted to type `Y` and then press `enter` to confirm.

4. After successfully adding the entry to crontab, you'll see `crontab: installing new crontab` leftover in the terminal.
   Now we run the script initially so we're not waiting around to get the freshest eggroll:
   `python3 "/home/$USER/scripts/GrabNewProtonGE.py"`
```
user@computer:~$ python3 "/home/$USER/scripts/GrabNewProtonGE.py"
New version available:  8.25
Downloading New Release:
[ https://github.com/GloriousEggroll/proton-ge-custom/releases/download/GE-Proton8-25/GE-Proton8-25.tar.gz ]
GE-Proton8-25.tar.gz: 100%|██████████████████████████████████████████████| 429M/429M [00:03<00:00, 114MiB/s]
Download Complete!

Extracting Release
[ /home/tristan/.steam/compatibilitytools.d/GE-Proton8-25 ]
GE-Proton8-25.tar.gz: 100%|███████████████████████████████████████████| 7.95k/7.95k [00:05<00:00, 1.38kiB/s]
Extraction Complete!

Please restart Steam to see new version
```
