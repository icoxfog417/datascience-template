import numpy as np

from scripts import simple_matmul as sm


class TestSimpleMatmul:
    def test_simple_matmul(self) -> None:
        A = np.array([1, 2, 3])
        B = np.array([2, 4, 5])

        np.testing.assert_array_equal(sm.f(A, B), A @ B)
