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

    handler = {
        '{': 0,
        '[': 0,
        '(': 0,
        ')': 0,
        ']': 0,
        '}': 0
    }

    for _ in range(stack.size()):
        item = stack.pop()

        handler[item] += 1

    if handler['('] != handler[')'] or handler['['] != handler[']'] or handler['{'] != handler['}']:
        print("Несбалансированно")
    else:
        print("Сбалансированно")

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
    
    for balanced_item, disbalanced_item in zip(balanced_args, disbalanced_args):
        check_balance(balanced_item)
        check_balance(disbalanced_item)
