from typing import Any


class FlatIterator:
    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.parent_counter = 0
        self.previous_item = None

        return self
    
    def general_iterator(self):
        item = self.list_of_list[self.parent_counter]

        if item == []:
            self.parent_counter += 1
            item = self.list_of_list[self.parent_counter]
        
        return item
    
    def __next__(self):
        item = self.general_iterator()

        try:
            while type(item) is list:
                if item[0] == []:
                    item.pop(0)

                if item == []:
                    item = self.general_iterator()
                    continue
                
                self.previous_item = item
                item = item[0]

            self.previous_item.pop(0)

            return item

        except IndexError:
            raise StopIteration


def test_3(): 
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

if __name__ == '__main__':
    test_3()