import arrow
from ics import Calendar, Event, alarm
import datetime
from datetime import timedelta

winter_classtimes = ["8:00", "9:40", "10:10", "11:50", "14:00", "15:40", "16:10", "17:50", "19:00", "21:35"]
summer_classtimes = ["8:00", "9:40", "10:10", "11:50", "14:30", "16:10", "16:40", "18:20", "19:30", "22:05"]

def createEvent(year, month, day, kind, class_name, class_teacher, class_location):
    """
    创建事件
    """
    # 冬夏季作息表更换
    if (month >= 5 & month < 10):
        classtimes = summer_classtimes
    else:
        classtimes = winter_classtimes

    e = Event()
    e.name = class_name
    table_time = classtimes[kind*2].split(':')
    hours = int(table_time[0])
    minutes = int(table_time[1])
    seconds = 0
    start_time = arrow.Arrow(year, month, day, hours, minutes, seconds, tzinfo='local')
    table_time = classtimes[kind*2+1].split(':')
    hours = int(table_time[0])
    minutes = int(table_time[1])
    seconds = 0
    end_time = arrow.Arrow(year, month, day, hours, minutes, seconds, tzinfo='local')
    e.begin = start_time.format()
    e.end = end_time.format()
    e.description = class_teacher
    e.location = class_location
    return e

# 根据周数计算年月日
def deltaDay(init_year, init_month, init_day, delta_day):
    '''
    根据校历第一天日期和天数计算对应的日期
    '''
    first_day=datetime.datetime(init_year,init_month,init_day)
    add_day=datetime.timedelta(days=delta_day)
    return datetime.datetime.strftime(first_day+add_day,"%Y-%m-%d")
