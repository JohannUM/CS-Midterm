secret_message = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def get_frequencies(msg : str):
    freq = {}
    for l in msg:
        freq[l] = freq.get(l, 0) + 1
    return freq

def calculate_shift(freq: dict, msg : str):
    counter = 0
    highest_freq = None
    for key in freq:
        if freq[key] > counter:
            highest_freq = key
            counter = freq[key]
    pos = alphabet.find(highest_freq)
    if(pos > 4):
        return (pos - 4)*-1
    else:
        return 4 - pos

def decode_msg(shift : int, msg : str):
    decoded_msg = ''
    for l in msg:
        pos = alphabet.find(l)
        curr_shift = pos + shift
        if (curr_shift >= len(alphabet)):
            curr_shift = len(alphabet)-curr_shift-1
        decoded_msg = decoded_msg + alphabet[curr_shift]
    return decoded_msg
    print("The decoded message is: " + decoded_msg)


s = calculate_shift(get_frequencies(secret_message), secret_message)
d = decode_msg(s, secret_message)
print("The decoded message is: " + d)

