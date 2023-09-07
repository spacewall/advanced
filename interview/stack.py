from collections import deque


class Stack(deque):
    def is_empty(self) -> bool:
        if self.__len__() == 0:
            return True
        else:
            return False

    # Здесь ожидаем строку в контексте второго задания
    def push(self, element: str) -> None:
        self.append(element)

    # Данный метод доступен при наследовании
    # def pop(self):
    #     return super().pop()

    def peek(self):
        return self.__getitem__(-1)
    
    def size(self):
        return self.__len__()
