print('%d' % 3)
print('%5d' % 3)
print('%05d' % 3)
print("")

print('%05.2f' % 3.141592)
print('%5.3f' % 3.141592)
print('%06.3f' % 3.141592)

print("")
str1 = 'Today is {month} / {days}'.format(month='April', days=1)
str2 = 'Today is {month} / {days}'.format(days=1, month='April')
print(str1, end=', ')
print(str2)

str3 = 'Today is {0} / {1}'.format('April', 1)
print(str3)
