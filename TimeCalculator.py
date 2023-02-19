def add_time(start, duration , Day = None):
    x = start.split()
    oldAP = x[1]
 
    now = x[0].split(':')
    skip = duration.split(':')
    for i in range(1,-1,-1):
        if i == 1:
            sumMin = int(now[i]) + int(skip[i])
            newMin = int(sumMin % 60)
            if newMin < 10:
                newMin = '0' + str(newMin)
            hourPass = (sumMin/60)//1

        elif i == 0:
            sumHour = int(now[i]) + int(skip[i]) + hourPass
            newHour = int(sumHour % 12)
            if newHour == 0:
                newHour = '12'

    x[0] = str(newHour) + ':' + str(newMin)

    APcount = ((sumHour/12)//1)%2
    if APcount == 1:
        if oldAP == 'PM':
                x[1] = 'AM'
        else:
            x[1] = 'PM'

    nday = ((sumHour/12)//1)/2
    if oldAP == 'AM':
        nday = int(nday//1)

    elif oldAP == 'PM':
        up = nday - (nday//1) 
        if up >= 0.5:
            nday = int((nday+1)//1)
    nameDay = ''
    if Day:
        dayInWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for i in dayInWeek:
            if i.lower() == Day.lower():
                nameDay = (dayInWeek.index(i) + nday) % 7
                nameDay = ', ' + dayInWeek[int(nameDay)]  
      
    if nday > 1 :
        nday = ' (' + str(nday) + ' days later)'
    elif nday == 1:
        nday = ' (next day)'
    elif nday < 1:
        nday = ''

    new_time = x[0] + ' ' +  x[1] + nameDay  + str(nday)
    return new_time
