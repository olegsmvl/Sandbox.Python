
list_test = ['aad', 'dfrr']

try:
    msg = list_test.split()
except Exception as e:
    text = f'exception: {e}'
    print(text)
