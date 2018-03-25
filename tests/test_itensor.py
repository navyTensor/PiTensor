import unittest
import pitensor


class PiTensorTest_ITensor(unittest.TestCase):
    def test(self):
        self.testIndex()
        self.testITensor()

    def testIndex(self):
        i = pitensor.Index("I", 3)

    def testITensor(self):
        i = pitensor.Index("I", 3)
        j = pitensor.Index("J", 4)
        T = pitensor.ITensor(i,j)
        T.fill(1.0)
        U = pitensor.ITensor(i)
        S = pitensor.ITensor()
        V = pitensor.ITensor()
        foo = pitensor.svd(T, U, S, V)
        print(foo)
