logs = [
    ["01-01-2023", "15:00", "ERROR", "failed"],
    ["01-01-2023", "14:00", "SUCCESS", "established"],
    ["01-01-2022", "18:00", "CRITICAL", "failed"],
]


def check_error(log):
    if log[2] == "ERROR" or log[2] == "CRITICAL":
        return True
    else:
        return False


def get_date(err):
    return err[0]


def extractErrorLogs(logs):  # 4/15
    errors = list(filter(check_error, logs))
    return sorted(errors, key=get_date)

#SUCCESS

def get_time(err):
    split_up = err[0].split("-")
    return split_up[2], split_up[1], split_up[0], err[1]


def erl(logs):  # 15/15
    errors = list(filter(check_error, logs))
    return sorted(errors, key=get_time)


a = ["12-01-2023", "10-01-2022"]

logs2 = [
    ["01-01-2166", "00:28", "ERROR", "failed"],
    ["01-04-2087", "15:45", "CRITICAL", "failed"],
    ["01-06-2342", "11:10", "CRITICAL", "failed"],
    ["01-08-2963", "15:15", "ERROR", "failed"],
    ["01-12-2944", "04:03", "CRITICAL", "failed"],
    ["02-03-2779", "13:25", "ERROR", "failed"],
    ["02-07-2518", "05:36", "ERROR", "failed"],
    ["02-08-2179", "00:28", "CRITICAL", "failed"],
    ["02-10-2349", "19:50", "ERROR", "failed"],
    ["02-10-2645", "10:49", "CRITICAL", "failed"],
    ["03-02-2159", "17:37", "CRITICAL", "failed"],
    ["03-04-2452", "06:22", "ERROR", "failed"],
    ["03-08-2489", "13:47", "ERROR", "failed"],
    ["04-01-2343", "02:09", "ERROR", "failed"],
    ["04-06-2706", "00:39", "ERROR", "failed"],
    ["04-07-2933", "15:48", "ERROR", "failed"],
    ["04-09-2183", "18:33", "CRITICAL", "failed"],
    ["04-09-2468", "16:27", "ERROR", "failed"],
    ["04-12-2298", "16:26", "ERROR", "failed"],
    ["05-03-2899", "08:28", "ERROR", "failed"],
    ["05-12-2653", "01:09", "CRITICAL", "failed"],
    ["05-12-2852", "17:00", "CRITICAL", "failed"],
    ["06-02-2195", "02:48", "ERROR", "failed"],
    ["06-04-2871", "15:41", "ERROR", "failed"],
    ["06-06-2892", "17:18", "ERROR", "failed"],
    ["06-10-2373", "07:16", "CRITICAL", "failed"],
    ["07-02-2351", "21:50", "ERROR", "failed"],
    ["07-05-2081", "17:10", "ERROR", "failed"],
    ["07-06-2421", "15:35", "ERROR", "failed"],
    ["07-06-2977", "00:43", "CRITICAL", "failed"],
    ["08-01-2007", "12:29", "CRITICAL", "failed"],
    ["08-02-2514", "05:55", "ERROR", "failed"],
]

# print(extractErrorLogs(logs2))
# print(sorted(logs2, key=get_date))
print(erl(logs2))
