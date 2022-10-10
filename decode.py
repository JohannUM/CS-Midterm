# String of the alphabet, used in calculations
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# function to calculate the frequencies of the characters in a string. 
# The output is a dictionary where the keys are the characters and the associated value is the frequency
def get_frequencies(msg):
    freq = {}
    for l in msg: # Loop through each char in the string
        freq[l] = freq.get(l, 0) + 1 # Increase value at that key by one
    return freq

# Function that calculates by how much the alphabet is shifted using the fact that "E" is the most frequent char in the english language
# In the alphabet string "E" is at index 4
def calculate_shift(freq):
    counter = 0
    highest_freq = None
    # Get the highest frequency char
    for key in freq:
        if freq[key] > counter:
            highest_freq = key
            counter = freq[key]
    index = alphabet.find(highest_freq) # Find the index of the highest frequency char in the normal alphabet
    # Calculate the shift.
    if(index > 4):
        return (index - 4)*-1
    else:
        return 4 - index

# Function to decode the message using the shift which was previously calculated
def decode_msg(shift, msg):
    decoded_msg = ''
    for l in msg: # Loop through the encoded message
        pos = alphabet.find(l) # Find the index of the current char in the alphabet
        curr_shift = pos + shift # Calculate the shift for that character
        if (curr_shift >= len(alphabet)): # If the new index is bigger than the length of the alphabet
            curr_shift = len(alphabet)-curr_shift-1 # Then the new index is the length of the alphabet - the shift
        decoded_msg = decoded_msg + alphabet[curr_shift] # Append the decoded character to the decoded message
    return decoded_msg

# Function calls
secret_message = str(input())
s = calculate_shift(get_frequencies(secret_message))
d = decode_msg(s, secret_message)
print("The decoded message is: " + d)

