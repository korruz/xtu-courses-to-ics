# 全部格子信息的读取

# from demo4 import createEvent
from myfun import createEvent,deltaDay
import xlrd
import re
from ics import Calendar

wb = xlrd.open_workbook("./example.xls")
sh = wb.sheet_by_name('Sheet1')

init_year = 2021
init_month = 3
init_day = 1
# 第一天一般是星期一，这里未作特殊处理

c = Calendar()

for class_kind in range(3,8):
    for day_kind in range(1,8):
        if (sh.cell_value(class_kind,day_kind).strip()==''):
            continue
        class_str = sh.cell_value(class_kind,day_kind).split('\n')
        pattern = re.compile(r'\d+')
        weeks = re.findall(pattern, class_str[3])
        for week in range(eval(weeks[0]),eval(weeks[1])+1):
            day_str = deltaDay(init_year,init_month,init_day+day_kind-1,7*(week-1)).split('-')
            event = createEvent(int(day_str[0]),int(day_str[1]),int(day_str[2]),class_kind-3,class_str[1],class_str[2],class_str[4])
            c.events.add(event)
        if len(class_str) == 5:
            continue
        elif class_str[1] != class_str[5]:
            continue
        pattern = re.compile(r'\d+')
        weeks = re.findall(pattern, class_str[7])
        for week in range(eval(weeks[0]),eval(weeks[1])+1):
            day_str = deltaDay(init_year,init_month,init_day+day_kind-1,7*(week-1)).split('-')
            event = createEvent(int(day_str[0]),int(day_str[1]),int(day_str[2]),class_kind-3,class_str[5],class_str[6],class_str[8])
            c.events.add(event)
            
with open('iCalendar.ics', 'w', encoding='utf-8') as my_file:
    my_file.writelines(c)
