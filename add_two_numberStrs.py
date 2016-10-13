# add two numbers in string format
def add(a, b):
    """
    :type a: string of numbers
    :type b: string of numbers
    """
    res, carry, val = "", 0, 0

    for i in range(max(len(a),len(b))):
        val = carry
        if (i < len(a)):
            val += int(a[-(i+1)])
        if (i < len(b)):
            val += int(b[-(i+1)])
        carry = val / 10 # digit to carry
        val   = val % 10 # value remain
        res += str(val)

    if (carry):
        res += str(carry)

    return res[::-1] # reverse number string


if __name__ == '__main__':
    print add("12345","12555")
    
