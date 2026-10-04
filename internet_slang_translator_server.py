import socket
translation ={
    "tbh":"to be honest",
    "ig":"i guess",
    "atm":"at the momment",
    "irl":"in real life",
    "lol":"laughing out loud",
    "omg":"oh my god",
    "nvm":"never mind",
    "ttyl":"talk to you later",
    "brb":"be right back",
    "idc":"i dont care",
    "idk":"i dont know",
}
HOST ="127.0.0.1"
PORT =5000
server =socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((HOST,PORT))
print(f"server is running on {HOST}:{PORT}")
while True:
    data, client_addr = server.recvfrom(2048)
    sentence = data.decode()
    words = sentence.split()
    translated = []
    for word in words:
        prefix = ""
        suffix = ""
        while len(word) > 0 and not word[0].isalnum():
            prefix += word[0]
            word = word[1:]
        while len(word) > 0 and not word[-1].isalnum():
            suffix = word[-1] + suffix
            word = word[:-1]
        lower_word = word.lower()
        if lower_word in translation:
            translated.append(prefix + translation[lower_word] + suffix)
        else:
            translated.append(prefix + word + suffix)
    result = " ".join(translated)
    server.sendto(result.encode(), client_addr)
    print("\nreceived:", sentence)
    print("translated:", result)

