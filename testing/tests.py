import unittest

from data.courses_mentors_durations import courses, mentors, durations
from main_for_collections import max_min_len_of_course, ordered_sequence, correlation
from main_for_api import delete_folder, make_folder


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


class TestUnitMainAPI(unittest.TestCase):
    def test_make_folder_status_code(self):
        status_code = make_folder("test")
        delete_folder("test")

        self.assertEqual(201, status_code, "A folder has not been created")

    @unittest.expectedFailure
    def test_double_make_folder_status_code(self):
        make_folder("test")
        status_code = make_folder("test")
        delete_folder("test")
        
        self.assertEqual(201, status_code)

    @unittest.expectedFailure
    def test_delete_folder_invalid_token(self):
        status_code = delete_folder("test", TOKEN="FAKE_TOKEN")

        self.assertEqual(204, status_code)

    @unittest.expectedFailure
    def test_delete_status_code(self):
        status_code = delete_folder("fake_test")

        self.assertEqual(204, status_code)

    def test_delete_error_status_code(self):
        status_code = delete_folder("test")

        self.assertEqual(404, status_code)


if __name__ == "__main__":
    unittest.main()
