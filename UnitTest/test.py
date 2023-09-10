import unittest
import Code
from classForTest import ClassForUnitTest

class TestingMyCode(unittest.TestCase):
    def testCodeForUnitTest(self):
        self.assertTrue(Code.CodeForUnitTest(1,3),4)
    def testSum(self):
        self.assertEqual(Code.Sum(1,3),4)
    def testSubtraction(self):
        self.assertEqual(Code.Subtraction(1,3),-2)
    def testMultiply(self):
        self.assertEqual(Code.Multiply(1,3),3)
    def testDivide(self):
        self.assertEqual(Code.Divide(6,3),2)

class TestingClasCode(unittest.TestCase):
    def testSum(self):
        objA = ClassForUnitTest()
        self.assertEqual(objA.Sum('string','AmendString'),'stringAmendString')
    def testMultiply(self):
        objA = ClassForUnitTest()
        self.assertEqual(objA.Multiply('string',3),'stringstringstring')


