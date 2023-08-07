class FlatIterator:

    def __init__(self, list_of_list: list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.parent_counter = -1
        self.child_counter = 0
        self.child_list = list()

        return self

    def __next__(self):
        
        if self.child_counter == len(self.child_list):
            self.parent_counter += 1
            if self.parent_counter == len(self.list_of_list):
                raise StopIteration
            
            self.child_counter = 0
            self.child_list = self.list_of_list[self.parent_counter]

        item = self.child_list[self.child_counter]
        self.child_counter += 1

        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()
