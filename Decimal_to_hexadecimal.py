"""This programme converts any real number from decimal to hexadecimal with the desired accuracy."""

def toHex(value, k):
    """Converts a real number from decimal to hexadecimal"""
    
    result = ""

    # If the number is negative, convert it to positive 
    # and add a '-' sign to the result string
    if value < 0: 
        value = -value;
        result += '-'

    ivalue = int(value) # Integer part
    fvalue = value - ivalue # Fractional part
    
    # Convert integer part
    while ivalue > 0:
        ost = ivalue%16
        ivalue = ivalue//16
        result += format(ost, 'X')

    result = result[:: -1]

    result += '.' # Add a comma

    # Convert fractional part
    for i in range(k):
        fvalue = fvalue * 16
        digit = int(fvalue)
        result += format(digit, 'X')

        fvalue -= digit

        if fvalue == 0:
          break

    # Return a string with a result
    return result;

number = float(input("\nEnter decimal number: "))
k = int(input("Enter the desired accuracy: "))
print('Hex number:', toHex(number, k))