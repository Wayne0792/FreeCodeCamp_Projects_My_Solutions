def add_time(start, duration, starting_day=None):
    starts = start.split(':')
    start_hours = int(starts[0])
    start_minutes, period = starts[1].split()
    start_minutes = int(start_minutes)
    duration_hours, duration_minutes = [int(v) for v in duration.split(':')]

    output_minutes = (start_minutes+duration_minutes)%60 
    duration_hours += (start_minutes+duration_minutes)//60
    output_hours = (start_hours+duration_hours)%12
    period_turns = (start_hours+duration_hours)//12
    days = period_turns//2

    if period_turns%2 == 0:
        output_period = period
    else:
        if period == "AM":
            output_period = "PM"
        else:
            output_period = "AM"
            days += 1
    
    if output_hours == 0:
        output_hours = 12
    
    output_string = str(output_hours)+':'+str(output_minutes).rjust(2, '0')+' '+output_period

    days_of_the_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    if starting_day:
        starting_day = starting_day.capitalize()
        new_index = (days_of_the_week.index(starting_day)+days)%7
        output_string += ", "+days_of_the_week[new_index]
    
    if days == 1:
        output_string += " (next day)"
    if days > 1:
        output_string += " ({} days later)".format(days)

    return output_string

