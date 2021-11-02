intercepted_msg = 'cbyvprzbiruvzznevangryerlobngenvagnapre'
fragment = 've'
d1 = (ord(fragment[1]) - ord(fragment[0]) ) % 26
found = 1
for x in range(len(intercepted_msg) -2):
    if (ord(intercepted_msg[x + 1]) - ord(intercepted_msg[x])) % 26 == d1:
        offset = (ord(fragment[0]) - ord(intercepted_msg[x])) % 26
        decode = [chr(97 + (ord(c) - 97 + offset) % 26) for c in intercepted_msg]
        print("B:", "".join(decode))
if not found:
    print("Offset unknown")
