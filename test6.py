import numpy as np
eth ={
  "ethereum": {
    "gbp": 971.53,
    "last_updated_at": 1611518969
  }
}

data = eth["ethereum"]
gpb = data['gbp']
# lastupdate = np.array(data['last_updated_at']).astype('datatime64(s)')

import datetime

timestamp = data['last_updated_at']
lastupdate = datetime.datetime.fromtimestamp(timestamp)


print(gpb)
print(lastupdate)