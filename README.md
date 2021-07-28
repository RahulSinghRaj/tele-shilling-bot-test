# AutoShill

Automatic Shilling Program for Telegram

# Links

Telegram: https://t.me/AutoShillTG  
Github: https://github.com/AllCoinLab  

# Introduction

### 🔥🔥🔥 ATTENTION ALL SHILLERS!! 🔥🔥🔥 
  
With this program,  
you can **SHILL MORE** efficiently to more groups with **FREE** hands.  
Do other things! rest, play, or find more opportunities.  

For the launch event,
it will be **FREE** to use for all of you.  
Follow the instructions in github

When the time is right,  
Fee will be charged for future use.  
And you will know that it is still much better to use :)  

# Features
1. Can shill with your user **ACCOUNT**, not with **BOT**
(Can also do with bot but you prefer account)  
2. Can shill in multiple TG group  
(tested for 50+ groups, careful yourself for the TG spam system)  
3. Can shill with the **GROUP LINK**. No need for **GROUP ID**, etc.  
4. Can shill based on time limitation of **SLOW MODE**.  
(tested for no slow mode to 1h slow mode)  
5. **NO INSTALLATION NEEDED**
6. **NOT** using your computer power  
(You can also run this in your mobile too + turn on/off)
8. And many more, just focusing on spreading this tool now.  

# Also
1. Automatically joins the group if listed group is not joined  
(Only few group can be joined per day due to TG system)

# Instruction
Working on progress.  
It will be announced in Telegram if the tool is ready.  

1. Follow instructions on section 'Obtaining api_id' in this link to get 'api_id' and 'api_hash':  
https://core.telegram.org/api/obtaining_api_id

2. Open Google Colab Intro Page  
https://colab.research.google.com/notebooks/intro.ipynb

2-1. Login with your google account  
This is one of Official Google Page, check yourself :)

2-2. If you have already logged in, popup will appear. Simply click 'ESC' to erase it.

3. Click on the cell and type:
```
!git clone https://github.com/AllCoinLab/AutoShill.git
```

4. Click left panel and click each files and follow each instructions below

4-1. Open cfg/app.cfg  
Write down api_id, api_hash and phone number

4-2. Open cfg/ctrl.cfg  
Set values to control this program

4-2. Open cfg/group.cfg  
Write down all group links you want to shill like examples given
##### You can write down based on @ link or full link
##### MAKE SURE each groups are separated by at least ONE SPACE or NEWLINE
##### Other than that, you don't need to care for some orders or something
##### No need to care for space, newline count between groups.
##### Just make sure at least ONE SPACE or NEWLINE
##### Also no need to care for uppercase

4-3. Open cfg/shill.txt  
Write down shill text

4. Change data and save

5. Click on the cell and type:
```
!ipython3 run.py
```

6. Check shilling is being processed

7. Enjoy 24/7 Shilling :)



# Some Tips
Before the mute, TG system usually sends warning message.  
This tool will display those warnings.  
So some warning happens primarily based on spam / flood / etc,  
it is recommended to stop for a few moment and restart.


# FAQ
1. Spam / Flood warning message happens  

It is sign for the mute / ban,  
erase some shill group or increase 'SLEEP' value

Sometimes TG system applies the mute / ban without warning message.  
This can be caused by user report.  
As it cannot be avoided as there is no prior notice,  
I recommend you to erase more shill group and increase 'SLEEP' value


# DISCLAIMER
This is made for the shillers to shill more effectively and efficiently.  
Using too much in too much TG groups may lead unexpected results by the TG system. (ex. mute / ban)  
This tool is tested with many situations.  
(Up to 50+ groups for 24+ hours)  
But it may differ because of the various slow mode cooldown for each group.

This tool has some safety methods to avoid it,  
but this is not responsible for those unexpected results.  
It is up to **YOU** to adjust using time and target group counts to avoid it.

