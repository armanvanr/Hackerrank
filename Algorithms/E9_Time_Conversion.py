def timeConversion(s):
    if s[8:] == "PM": # kondisi PM (ambil char ke 9 dan 10)
        if s[:2] == "12": # jam adalah char ke 1 dan 2
            h = "12"
        else:
            h = str(int(s[:2]) + 12) # ubah jam ke number, update jam += 12
    else: # kondisi AM
        if s[:2] == "12":
            h = "00"
        else:
            h = s[:2]
    r = s[2:8] # ambil bagian menit dan detiknya
    return h+r

def time_conversion(s):
    pm_am = s[-2:]
    hh = s[:2]
    if pm_am == "PM":
        hour= str(int(hh)+12)
        if hh == "12": hour="12"
    else:
        hour= hh
        if hh == "12": hour = "00"
    minute_second = s[2:8]
    return hour+minute_second



# print(timeConversion("11:00:00PM"))
# print(timeConversion("12:00:00AM"))
# print(timeConversion("05:00:00PM"))
# print(timeConversion("09:00:00AM"))

time_conversion("11:00:00PM")
