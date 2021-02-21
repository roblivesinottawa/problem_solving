def print_seconds(hours, minutes, seconds):
    return (hours*3600) + (minutes*60) + seconds


a = print_seconds(2, 30, 0)
b = print_seconds(0,45,15)
result = a + b


print(result)


def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

print(convert_seconds(5000))