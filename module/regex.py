import re

# Regular Expression (正規表現：Regex)
# ↓参考サイト↓
# https://docs.python.org/3/py-modindex.html

email = "myemail@gmail.com"
bad_mail = "myemail@gmailcom"
print("@" in email)

matched = re.search('@\w+\.', email)
if matched:
    print(matched)
    print("Matched")
else:
    print("Not found")