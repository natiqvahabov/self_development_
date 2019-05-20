# timestamp
import pandas as pd
import numpy as np
from datetime import datetime

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
		 datetime(2011, 1, 7), datetime(2011, 1, 8)
		 datetime(2011, 1, 10), datetime(2011, 1, 12)]

ts = pd.Series(np.random.randn(6), index=dates)

ts + ts[::2]

stamp = ts.index[0]
ts[stamp] # -> random number assigned to 0 index

ts['1/6/2011':'1/11/2011']
ts.truncate(after='1/9/2011')

# shifting 3 days
from pandas.tseries.offsets import Day, MonthEnd
now = datetime(2011, 11, 17)
now + 3 * Day()

ts.shift(3, freq='D')

# timezone 
import pytz # gets data from Olson db
pytz.common_timezones[-5:] # ['US/Eastern', 'US/Hawaii', 'US/Mountain', 'US/Pacific', 'UTC']

stamp = pd.Timestamp('2011-03-12 04:00')
stamp.tz_localize('utc')
stamp.tz_convert('America/New_York')

# periods also being used under pandas library