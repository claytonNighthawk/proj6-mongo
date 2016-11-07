import arrow

def human(date):
    try:
        then = arrow.get(date).replace(tzinfo='local')
        now = arrow.now().floor('day')

        if then.date() == now.date():
            human = "Today"
        elif now.replace(days=+1).date() == then.date():
            human = "Tomorrow"
        elif now.replace(days=-1).date() == then.date():
            human = "Yesterday"    
        else: 
            human = then.humanize(now)

    except: 
        human = date

    return human