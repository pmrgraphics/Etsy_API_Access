from secrets import choice
import string



print(''.join([choice(string.ascii_uppercase + string.digits) for _ in range(60)]))