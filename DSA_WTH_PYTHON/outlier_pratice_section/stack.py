class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None

        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def is_empty(self):
        return self.head is None


def is_balanced(s: str) -> bool:
    stack = Stack()

    for char in s:
        # 1. Manually push opening brackets
        if char == '(' or char == '{' or char == '[':
            stack.push(char)

        # 2. Handle closing brackets
        elif char == ')' or char == '}' or char == ']':
            # If stack is empty but we have a closing bracket, it's invalid
            if stack.is_empty():
                return False

            top_element = stack.pop()

            # 3. Manually check if the closing bracket matches the popped opening bracket
            if char == ')' and top_element != '(':
                return False
            if char == '}' and top_element != '{':
                return False
            if char == ']' and top_element != '[':
                return False

    # 4. If the stack is completely empty at the end, it's balanced!
    if stack.is_empty():
        return True
    else:
        return False


# --- Test Cases ---
if __name__ == "__main__":
    print(is_balanced("()[]{}"))  # True
    print(is_balanced("([{}])"))  # True
    print(is_balanced("(]"))      # False
    print(is_balanced("([)]"))    # False
    print(is_balanced("((("))     # False
    print(is_balanced(""))        # True
