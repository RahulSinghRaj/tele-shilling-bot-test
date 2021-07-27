################################################
# Write down each parameter carefully
# so as to shill perfectly
################################################

env_data = {
############################################# info params
# Your api_id (if 123123123)
'API_ID': 123123123,
# Your api_hash (if abcabcabcabac)
'API_HASH': 'abcabcabcabac',
# Your phone number with country code (if +1 012 400 9999)
'NUMBER': 10124009999,

############################################# control params
# Sleep duration between group message
# Try to increase number to avoid mute / ban
'SLEEP': 0,
# Set 1 if you stop and run again
# Set 0 in normal case
'RECONNECT': 0,
# Set 1 to display log for Slow Mode
# It may print too many logs
'SLOW_LOG': 0,

# write down group @ links one by one using newline like example below
# No need to care for Uppercase
'AT_LINKS': '''
@BSC_TURKEY
@BSC_PhiliPPines
''',

# write down group full links one by one using newline like example below
# No need to care for Uppercase
'FULL_LINKS': '''
https://t.me/uniswap_talk
https://t.me/BSCApe
'''
  
# write down text which you want to shill
# it will be displayed exactly same (including newline)
'SHILL_TEXT': '''
🔥🔥🔥 ATTENTION ALL SHILLERS 🔥🔥🔥

Here is the FREE Automatic Shilling Tool
Just for you!
Join @AutoShillTG
''',
}

import pickle
with open('./env.pkl', 'wb') as f:
  pickle.dump(env_data, f)

# download core
from core import run
run()
