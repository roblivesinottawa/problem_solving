def calc(seconds, week):
    return seconds * week

result = calc(86400, 7)
print(result)

# 

def how_many_passwords(letter=6, possibility=26):
    return possibility ** letter


total = how_many_passwords()
print(total)

# 

def sectors(disk_size=None, sector_size=None):
    disk_size = 16
    sector_size = 512
    return disk_size / sector_size

print(sectors())

