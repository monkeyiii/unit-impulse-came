import getdate
import datetime
# i = 'a'
i = datetime.datetime.now()
k = getdate.birthgap(8,22)
l = getdate.birthgap(8,24)
l2 = getdate.birthgap(8,25)
l3 = getdate.birthgap(8,27)
l4 = getdate.birthgap(7,24)
from unittest import TestCase
class Test(TestCase):
    def test_birthgap(self):
        self.assertEqual(getdate.birthgap(8, 22),k)
    def test_birthgap2(self):
        self.assertEqual(getdate.birthgap(8, 24),l)
    def test_birthgap3(self):
        self.assertEqual(getdate.birthgap(8, 25),l2)
    def test_birthgap4(self):
        self.assertEqual(getdate.birthgap(8, 27),l3)
    def test_birthgap5(self):
        self.assertEqual(getdate.birthgap(7, 24),l4)
    if __name__ == "__main__":
            getdate.main()

