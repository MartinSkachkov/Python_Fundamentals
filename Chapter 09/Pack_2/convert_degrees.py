c_temps = input().split(' ')

for temp in c_temps:
    print(f'{int(temp) * 1.8 + 32:.0f}')
