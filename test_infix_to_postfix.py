from infix_to_postfix import infix_to_postfix, postfix_eval


def test_infix_to_postfix():
    assert infix_to_postfix("( A + B ) * ( C + D )") == "A B + C D + *"
    assert infix_to_postfix("( A + B ) * C") == "A B + C *"
    assert infix_to_postfix("A + B * C") == "A B C * +"


def test_postfix_eval():
    assert postfix_eval("4 5 6 * +") == 34
    assert postfix_eval("7 8 + 3 2 + /") == 3
