def InvalidIp(s):
    if s.count('.') != 3:
        return "Invalid IP Address"

    l = s.split('.')

    for i in l:
        if int(i) > 255 or int(i) < 0:
            return "Invalid IP Address"
    else:
        return "Valid IP Address"

result = InvalidIp('0.168.34.89')
print(result)