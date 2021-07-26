env_data = {
# write down target group links one by one using newline like example below
'at_links': '''
@BSC_TURKEY
@BSC_PhiliPPines
''',

# write down text which you want to shill
# it will be displayed same including newline.
'shill_text': '''
AutoShill
If u want to auto shill every group regarding slow mode,
DM @AllCoinLab
''',

# Your api_id (if 123123123)
'API_ID': '123123123',
# Your api_hash (if abcabcabcabac)
'API_HASH': 'abcabcabcabac',
# Your phone number with country code (if +1 012 400 9999)
'NUMBER': '10124009999',
}

import pickle
with open('./env.pkl', 'wb') as f:
  pickle.dump(env_data, f)

# download core
from core import run
run()
