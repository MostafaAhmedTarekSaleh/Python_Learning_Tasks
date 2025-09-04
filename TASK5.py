#Caesar Cipher Encoder/Decoder
"""
thought process:
dict that has lowercase letters of alphabet as keys and their corresponding
numerical values as the values.
When we shift we look at letter, take corresponding value, and add/ subtract from it the shift , then search that
new value and retrieve its key.

it is understood that dict is not "intended" to be used this way , searching is meant to be done
with keys not values, but here values are unique in the cipher so it is not an issue. also speed is
not of concern here.
"""
import string

aDict = dict(zip(string.ascii_lowercase, range(1, 27)))

msg = input("Please enter the string to be encoded: ").lower()
shift= int(input("Enter the desired shift encoding value: "))
def encode(msg,shift):
    result = []
    for letter in msg:
        new_value = (aDict[letter] + shift) % 26
        for letter, number in aDict.items():
            if number == new_value:
                result.append(letter)
    res = ""
    for char in result:
        res = res + char
    return res


def decode(encoded_msg,shift):
    result = []
    for letter in encoded_msg:
        old_value = aDict[letter] - shift
        for letter, number in aDict.items():
           if number == old_value:
               result.append(letter)
    res = ""
    for char in result:
        res = res + char
    print("Here is the message decoded again: ")
    return res

encoded_msg = encode(msg,shift)
print(encoded_msg)
decoded_msg = decode(encoded_msg,shift)
print(decoded_msg)
