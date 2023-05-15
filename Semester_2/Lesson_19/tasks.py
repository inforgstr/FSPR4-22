def readeable_time(seconds):
    hours = seconds//3600
    minutes = (seconds-hours*3600)//60
    sec = seconds - (hours*3600+minutes*60)

    lst = [f"0{x}" if len(str(x))==1 else str(x) for x in (hours, minutes, sec)]
    return ":".join(lst)

print(readeable_time(620))
