env_data = {
'at_links': '''
@BSC_TURKEY
@BSC_PhiliPPines
''',

'text': '''
AutoShill
If u want to auto shill every group regarding slow mode,
DM @AllCoinLab
''',

'API_ID': '123123123',
'API_HASH': 'abcabcabcabac',
'NUMBER': 123123123123,
}

import pickle
with open('./env.pkl', 'wb') as f:
  pickle.dump(env_data, f)

# download core
from core import run
run()
