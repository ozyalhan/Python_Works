import unittest

from fb_pyton_questions.main import problems


class TestCase(unittest.TestCase):

    def test1_1(self):

        test_data_list = ["apple", "banana", "cherry", "berry"]
        test_data_str = "b"
        predicted_result = ["banana","berry"]

        result_def = problems.problem1(test_data_list,test_data_str)
        self.assertEqual(result_def,predicted_result,' expected result: "banana","berry"')

    def test1_2(self):

        test_data_list = ["apple", "banana", "cherry", "berry"]
        test_data_str = "c"
        predicted_result = ["cherry"]

        result_def = problems.problem1(test_data_list,test_data_str)
        self.assertEqual(result_def,predicted_result,' expected result: "cherry"')

    def test1_3(self):

        test_data_list = ["apple", "banana", "cherry", "berry"]
        test_data_str = "a"
        predicted_result = ["apple"]

        result_def = problems.problem1(test_data_list,test_data_str)
        self.assertEqual(result_def,predicted_result,' expected result: "apple"')

    def test2_1(self):

        test_data_value = "AAAAaaBCCCDDe"
        predicted_result = "A4a2B1C3D2e1"

        result_def = problems.problem2(test_data_value)
        self.assertEqual(result_def,predicted_result,' expected result: "A4a2B1C3D2e1" ')

    def test2_2(self):

        test_data_value = "AAAAaaBCCCDD"
        predicted_result = "A4a2B1C3D2"

        result_def = problems.problem2(test_data_value)
        self.assertEqual(result_def,predicted_result,' expected result: "A4a2B1C3D2" ')

    def test2_3(self):

        test_data_value = "AAAAAaaBCCCDDeeee"
        predicted_result = "A5a2B1C3D2e4"

        result_def = problems.problem2(test_data_value)
        self.assertEqual(result_def,predicted_result,' expected result: "A5a2B1C3D2e4" ')


if __name__ == '__main__':
    unittest.main()


