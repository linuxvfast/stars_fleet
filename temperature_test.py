# -*- coding:utf-8 -*-
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'temperatures.csv'
with open(filename) as file:
    reads = csv.reader(file)
    header_row = next(reads)

    tem,date,lows= [],[],[]
    for row_num in reads:
        current_date = datetime.strptime(row_num[0],'%Y-%m-%d')
        date.append(current_date)

        row = int(row_num[2])
        tem.append(row)

        low = int(row_num[3])
        lows.append(low)
    # print(tem)
    # print(date)
# fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(date,tem,c='blue')
plt.plot(date,lows,c='red')
#装饰
plt.title('temperatures hight',fontsize=24)
plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
plt.ylabel('temperatures (F)',fontsize=16)
# plt.tick_params(labelsize=16)

plt.show()