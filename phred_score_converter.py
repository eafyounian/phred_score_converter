from browser import document, html

def calculate(event):
    phred = document['phred'].value
    try:
        phred = int(phred)

        if phred < 0:
            document['probability'].textContent = "Phred score should be positive!"
        else:
            result = 10 ** ((-phred) / 10)
            document['probability'].textContent = '%.9f (Base 33 corresponding ASCII:  %s  )' %(result, chr(phred + 33))
            # document['probability'].textContent = str(result)
    except ValueError:
        document['probability'].textContent = "Incorrect entry! Try again!"

def calculate_ascii(event):
    ascii_char = document['ascii'].value
    if len(ascii_char) != 1:
        document['probability_ascii'].textContent = "Enter a character of length 1!"
    else:
        phred = ord(ascii_char) - 33
        result = 10 ** ((-phred) / 10)
        document['probability_ascii'].textContent = '%.9f (Phred score:  %s  )' %(result, phred)

document['calculate_button'].bind("click", calculate)
document['calculate_button_ascii'].bind("click", calculate_ascii)