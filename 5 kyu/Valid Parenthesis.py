def valid_parentheses(string):
    currentLeftParen = 0
    for char in string:
        if char == '(':
            currentLeftParen += 1
        elif char == ')':
            if currentLeftParen == 0:
                return False
            else:
                currentLeftParen -= 1
    if not currentLeftParen == 0:
        return False
    return True
        