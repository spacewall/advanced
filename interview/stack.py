from collections import deque


class Stack(deque):
    def is_empty(self) -> bool:
        if self.__len__() == 0:
            return True
        else:
            return False

    def push(self, element) -> None:
        self.append(element)

    # Данный метод доступен при наследовании
    # def pop(self):
    #     return super().pop()

    def peek(self):
        return self.__getitem__(-1)
    
    def size(self):
        return self.__len__()
    

def check_balance(string: str) -> None:
    stack = Stack()

    for sub_str in string.strip(''):
        stack.append(sub_str)

    l_stack = Stack()
    r_stack = Stack()
    handler = None

    for _ in range(stack.size()):
        item = stack.pop()

        if item in ('[', '{', '('):
            l_stack.push(item)
        else:
            r_stack.push(item)

        if l_stack.size() == r_stack.size():
            r_stack.reverse()

    row_delimiter = 50 * "-"
    print(row_delimiter)

    
if __name__ == '__main__':
    balanced_args = [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}"
    ]

    disbalanced_args = [
        "}{}",
        "{{[(])]}}",
        "[[{())}]"
    ]
    n = 1
    for balanced_item, disbalanced_item in zip(balanced_args, disbalanced_args):
        print(n)
        n += 1
        check_balance(balanced_item)
        check_balance(disbalanced_item)
