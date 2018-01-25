# -*- coding:utf-8 -*-
import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'temperatures.csv'
with open(filename) as file:
    reads = csv.reader(file)  #全部读取
    header_row = next(reads)  #获取下一行的内容

    #最高温度，日期，最低温度
    tem,date,lows= [],[],[]
    for row_num in reads:
        current_date = datetime.strptime(row_num[0],'%Y-%m-%d')  #转换日期
        date.append(current_date)

        row = int(row_num[2])
        tem.append(row)

        low = int(row_num[3])
        lows.append(low)
    # print(tem)
    # print(date)
# fig = plt.figure(dpi=128,figsize=(10,6))
#alpha 表示颜色的透明度
plt.plot(date,tem,c='blue',alpha=0.5)
plt.plot(date,lows,c='red',alpha=0.5)
plt.fill_between(date,tem,lows,facecolor='blue',alpha=0.1)  #facecolor 表示填充的颜色

#装饰
plt.title('temperatures hight',fontsize=24)
plt.xlabel('',fontsize=16)
# fig.autofmt_xdate()
plt.ylabel('temperatures (F)',fontsize=16)
# plt.tick_params(labelsize=16)

plt.show()