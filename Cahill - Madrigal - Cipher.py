text = "Can you keep a secret?"
location = "Meet me at 48.6061 degreees N, 129.3328 degrees W at 5pm."
password = "%Kh@n! Ac&d#my92"

passage = """
Ciphers transform messages into an unrecognizable form to secure information
from unauthorized access. Typically, they rearrange, substitute, or manipulate
the characters in the original message based on a key. Modern ciphers, such as
AES (Advanced Encryption Standard), rely on complex mathematical algorithms
that make them infeasible even for computers to break through brute force.
With current computing systems, it would take millions of years to test every
possible key! As a result, AES is widely used to secure digital communications,
from text messages to bank transfers. However, AES is still only as strong as
the secrecy of its key, so make sure to keep your key private!
"""


def encrypt(message, key):
    """Returns the given message encrypted using your custom cipher."""
    return madrigal(message, key)


def decrypt(message, rekey):
    """Returns the given message encrypted using your custom cipher."""
    return ekati(message, rekey)


def madrigal(message, shift):
    mad = ""
    for i in message:
        mad = mad + cahill(i, shift)
    return mad


def cahill(i, shift):
    number = "123456789"
    alphabet1 = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
    alphabet2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    if i in number:
        if shift == 5 or shift == 6 or shift == 7 or shift == 8:
            num = int(i)
            if num + shift < 10:
                i1 = num + shift
                return str(i1)
            elif num - shift > 0:
                i1 = num - shift
                return str(i1)
            else:
                return i
        elif shift == 4:
            num = int(i)
            if num == 2 or num == 3 or num == 4 or num == 6 or num == 7 or num == 8:
                if num + shift < 10:
                    i1 = num + shift
                    return str(i1)
                elif num - shift > 0:
                    i1 = num - shift
                    return str(i1)
            else:
                return i
        elif shift == 3:
            num = int(i)
            if num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
                if num + shift < 10:
                    i1 = num + shift
                    return str(i1)
                elif num - shift > 0:
                    i1 = num - shift
                    return str(i1)
            else:
                return i
        else:
            return i


    elif i in alphabet1:
        i_position = alphabet1.index(i) + shift
        i2 = alphabet2[i_position]
        return i2

    else:
        return i


def ekati(message, shift):
    remad = ""
    for i in message:
        remad = remad + ekat(i, shift)
    return remad


def ekat(i, shift):
    number = "123456789"
    alphabet1 = "qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm"
    alphabet2 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

    if i in number:
        if shift == 5 or shift == 6 or shift == 7 or shift == 8:
            num = int(i)
            if num + shift < 10:
                i1 = num + shift
                return str(i1)
            elif num - shift > 0:
                i1 = num - shift
                return str(i1)
            else:
                return i
        elif shift == 4:
            num = int(i)
            if num == 2 or num == 3 or num == 4 or num == 6 or num == 7 or num == 8:
                if num + shift < 10:
                    i1 = num + shift
                    return str(i1)
                elif num - shift > 0:
                    i1 = num - shift
                    return str(i1)
            else:
                return i
        elif shift == 3:
            num = int(i)
            if num == 4 or num == 5 or num == 6 or num == 7 or num == 8 or num == 9:
                if num + shift < 10:
                    i1 = num + shift
                    return str(i1)
                elif num - shift > 0:
                    i1 = num - shift
                    return str(i1)
            else:
                return i
        else:
            return i



    elif i in alphabet2:
        a2_position = alphabet2.index(i)
        a1_position = a2_position - shift
        x2 = alphabet1[a1_position]
        return x2

    else:
        return i


custom_key = 7


messages = [
    text, location, password, passage
]

for message in messages:


    encrypted = encrypt(message, custom_key)
    print(f"Custom encrypted message: {encrypted}")

    decrypted = decrypt(encrypted, custom_key)
    print(f"Custom decrypted message: {decrypted}\n")
