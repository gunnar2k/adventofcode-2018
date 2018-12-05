import pandas as pd
import numpy as np

input = open("input.txt")

dates = []
events = []

for line in [x.strip() for x in input]:
    date = line[1:17].replace("1518", "2018")
    event = line[19:]
    dates.append(date)
    events.append(event)

df = pd.DataFrame({
    'Date': dates,
    'Event': events,
})
df['Date'] = pd.to_datetime(df.Date)
df = df.sort_values(by='Date')

guards = {
    # format:
    #
    # { GUARD_ID: {
    #   'total_minutes': <int>,
    #   'ranges': [<range>,...],
    # }}
    #
    #
    # example:
    #
    # 100: {
    #   'total_minutes': 120,
    #   'ranges': [],
    # }
}
current_guard = None
fell_asleep_at = None

for index, row in df.iterrows():
    event = row['Event']
    date = row['Date']

    if "begins shift" in event:
        guard_id = int(event.replace("Guard #", "").replace(" begins shift", ""))
        if guard_id not in guards:
            guards[guard_id] = {
                'total_minutes': 0,
                'minutes': {}
            }
        current_guard = guard_id
    elif "falls asleep" in event:
        fell_asleep_at = date
    elif "wakes up" in event:
        wakes_up = date - fell_asleep_at
        minutes = int(str(np.timedelta64(wakes_up,'m')).replace(" minutes", ""))
        print(current_guard, " fell asleep at ", fell_asleep_at)
        print(current_guard, " woke up at ", date)
        guards[current_guard]['total_minutes'] += minutes
        for min in range(fell_asleep_at.minute, date.minute):
            try:
                guards[current_guard]['minutes'][min] += 1
            except KeyError:
                guards[current_guard]['minutes'][min] = 1
        fell_asleep_at = None

    # print(date, event)

print(guards)
max_guard = guards[list(guards.keys())[0]]
max_guard_id = None
for guard_id in guards:
    guard = guards[guard_id]
    if guard['total_minutes'] > max_guard['total_minutes']:
        max_guard = guard
        max_guard_id = guard_id

print("---------")
print(max_guard)

print("---------")
minutes = max_guard['minutes']

max_minute = max(minutes, key=lambda x: minutes[x])

print(max_guard_id)
print(max_minute * max_guard_id)

print("-------------")
minutes = {}
for minute in range(0, 60):
    minutes[minute] = {
        'id': 0,
        'minutes': -1,
    }
    for guard_id in guards:
        guard = guards[guard_id]
        try:
            if guard['minutes'][minute] > minutes[minute]['minutes']:
                minutes[minute]['id'] = guard_id
                minutes[minute]['minutes'] = guard['minutes'][minute]
        except KeyError:
            pass

print(minutes)
print(max(minutes, key=lambda x: minutes[x]['minutes']))
