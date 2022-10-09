import random, string


def isbn_unique_code_generator(sender, instance, *args, **kwargs):
    if not instance.isbn:
        data = instance.title
        # x = [i for i in range(4,15+1) if i%2!=0]
        # instance.unique_code='product'+x
        instance.isbn = code_generator(data)


"""

>>> string.ascii_uppercase
'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> string.digits
'0123456789'
>>> string.ascii_uppercase + string.digits
'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

"""


def code_generator(data, size=5, chars=string.ascii_uppercase + string.digits):
    # code=''.join(random.choice(chars) for _  in range(size))
    code = ''.join(random.choice(chars) for _ in range(size))
    print(code)
    return data + code
# brand12345, brand78458
