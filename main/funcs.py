import string
import random

def gen_ukey(length: int, table: object, prefix: str) -> str:
    ukey = 0
    while ukey == 0:
        charset = string.ascii_letters + string.digits
        rand_ukey = prefix + ''.join(random.choices(charset, k=length))
        ls_query = table.objects.filter(ukey__exact=rand_ukey)
        if not ls_query:
            ukey = rand_ukey
        else:
            ukey = 0
    
    return ukey