
def add_time(start, duration,weekday=False):
    start = start.split()
    time = start[0]
    ampm = start[1]
    starttimes = time.split(':')
    starthours = int(starttimes[0])
    startminutes = int(starttimes[1])
    week=''
    ind=0

    duration = duration.split(':')
    addhours = int(duration[0])
    addminutes = int(duration[1])
    hours = starthours + addhours
    minutes = startminutes + addminutes
    if minutes > 60:
        hours = hours + 1
        minutes = minutes - 60
    if minutes < 10:
        minutes = '0' + str(minutes)
    if ampm=='PM':
      hours=hours+12

    if hours<24:
      if hours>12:
        hours=hours-12
        ampm='PM'
    if hours==12:
      ampm='PM'
  
        
    day=''
    if hours>23:

            days=hours//24
            print(days)
            hours=hours-(days*24)
            if days==1:
                day=' (next day)'
            if days==2:
              day=' (2 days later)'

            if days>2:
              day=' ('+str(days)+' days later)'
            if hours > 11:

           #   hours = hours - 12
              if ampm == 'AM':
                ampm = 'AM'
              else:
                ampm = 'AM'
            else:
              ampm='AM'

    if hours==0:
      hours=12
    L = ['Monday', 'tuesday', 'Wednesday', 'Thursday', 'Friday', 'saturDay', 'Sunday']
    if weekday:
      if day=='':
        week=', '+str(weekday)
      else:
        if weekday=='Monday':
         ind=0
        if weekday=='tuesday':
          ind=1
        if weekday=='Wednesday':
          ind=2
        if weekday=='Thursday':
          ind=3  
        if weekday=='Friday':
          ind=4 
        if weekday=='saturDay':
          ind=5
        if weekday=='Sunday':
          ind=6
        ind=ind+days
        ind=ind%7
        which=L[ind]
        week = ', ' + str(which)

    answer = str(hours) + ':' + str(minutes) + ' ' + ampm+week+day
    return answer