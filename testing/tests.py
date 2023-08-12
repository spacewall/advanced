import unittest

from data.courses_mentors_durations import courses, mentors, durations
from main import max_min_len_of_course, ordered_sequence, correlation


class TestUnitMain(unittest.TestCase):
    def test_first_task_max_len(self):
        result = max_min_len_of_course(courses, mentors, durations)
        
        self.assertIn('Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)', ' '.join(result))

    def test_first_task_not_in(self):
        result = max_min_len_of_course(courses, mentors, durations)

        self.assertNotIn("Java-разработчик с нуля", ' '.join(result), 'The Java course has a medium duration')

    def test_second_task(self):
        result = ordered_sequence(courses, mentors, durations)

        expected = [
            'Python-разработчик с нуля - 12 месяцев',
            'Java-разработчик с нуля - 14 месяцев',
            'Fullstack-разработчик на Python - 20 месяцев',
            'Frontend-разработчик с нуля - 20 месяцев'
            ]

        self.assertListEqual(result, expected)

    def test_third_task(self):
        result = correlation(courses, mentors, durations)

        self.assertIsNotNone(result)


# if __name__ == "__main__":
#     unittest.main()
