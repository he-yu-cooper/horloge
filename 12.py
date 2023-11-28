def set_time_format(is_12h):
    return is_12h

def display_time(h, m, s, is_12h):
    if is_12h:
        if h > 12:
            h -= 12
            return "{:02d}:{:02d}:{:02d} PM".format(h, m, s)
        else:
            return "{:02d}:{:02d}:{:02d} AM".format(h, m, s)
    else:
        return "{:02d}:{:02d}:{:02d}".format(h, m, s)

is_12h = set_time_format(True)
print(display_time(16, 30, 0, is_12h)) 
