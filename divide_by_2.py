from pythonds3.basic import Stack


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

        bin_string = ""
        while not rem_stack.is_empty():
            bin_string = bin_string + digits[rem_stack.pop()]

        return bin_string
