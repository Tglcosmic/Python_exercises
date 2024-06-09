import numpy as np
from datetime import datetime, timedelta
#
# arr_a = np.random.randint(1, 4, (3, 3))
# print(arr_a)
start_date = datetime.now().replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
end_date = datetime.now().replace(month=12, day=31, hour=23, minute=59, second=59, microsecond=999999)
timedelta(days=np.random.randint((end_date - start_date).days))
print(timedelta())