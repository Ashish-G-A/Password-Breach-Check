import hashlib
import requests

og_password = input('enter password to check: ')


h = hashlib.sha1()
byte_password = og_password.encode()
h.update(byte_password)
hashed_password = h.hexdigest()
hash_head = str(hashed_password[:5])
hash_body = str(hashed_password[5:]).upper()

# print(hash_head)
# print(hash_body.upper())

url = 'https://api.pwnedpasswords.com/range/{}'.format(hash_head)

r = requests.get(url)
print('status: {}'.format(r.status_code))

# for case in r.text.splitlines():
#     print(case[:35])

times = 0
for case in r.text.splitlines():
    if case[:35] == hash_body:
        times = case[36:]
        break

print('the password has been leaked {} times'.format(times))