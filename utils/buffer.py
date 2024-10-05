BUFFER = 'Buffer'

def writeBuffer(recipient, theme, letter):
    with open(f'{BUFFER}/{recipient}', 'a') as fileR:
        write = fileR.write(f'{recipient}\n\n{theme}\n\n{letter}')


