t_1 = 1
t_2 = '1'

try:
    result = t_1 + t_2 /  t_1 + t_2
# except:
except TypeError as e:
    error_text = str(e)
    result = 'Error'
except ZeroDivisionError:
    result = 'Zero division error'
else:
    print('No exceptions')
finally:
    print('Work always')

print(result)
