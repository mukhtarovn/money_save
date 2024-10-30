from calendar import monthrange
from datetime import datetime


print(round(1000/monthrange(2024, datetime.now().month)[1]))
print(monthrange(2024, datetime.now().month)[1]-datetime.now().day)
print(datetime.now().day)