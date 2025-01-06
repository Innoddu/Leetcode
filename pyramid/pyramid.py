
import unittest

def find_target_pyramid(pyramid, target):

    res = None
    def dfs(row, col, path, prod_val):
        nonlocal res
        if res is not None:
            return
        if row == len(pyramid):

            if prod_val == target:
                res = path[:-1]
            return

        if col < 0 or col >= len(pyramid[row]):
            return
  
        new_product = prod_val * pyramid[row][col]
        dfs(row + 1, col, path + "L", new_product)
        dfs(row + 1, col + 1, path + "R", new_product)
        
    
    dfs(0, 0, "", 1)
    return res


class TestFindTargetPyramid(unittest.TestCase):
    def test_small_pyramid(self):
        """
        Simple 3-row pyramid (target=2)
        
            1
           2 3
          4 1 1
        
        Path 'LR' => 1 * 2 * 1 = 2
        """
        pyramid = [
            [1],
            [2, 3],
            [4, 1, 1]
        ]
        target = 2
        result = find_target_pyramid(pyramid, target)
        self.assertEqual(result, "LR", f"Expected 'LR', got {result}")

    def test_larger_pyramid(self):
        """
        5-row pyramid (target=720)
        
                2
              4   3
            3   2   6
           2   9   5   2
         10   5   2  15   5
        
        'LRLL' => 2 * 4 * 2 * 9 * 5 = 720
        """
        pyramid = [
            [2],
            [4, 3],
            [3, 2, 6],
            [2, 9, 5, 2],
            [10, 5, 2, 15, 5]
        ]
        target = 720
        result = find_target_pyramid(pyramid, target)
        self.assertEqual(result, "LRLL", f"Expected 'LRLL', got {result}")

    def test_no_path(self):
        """
        Pyramid with no valid product path (target=10)
        
            1
           2 2
          3 3 3
        
        No path should produce 10, expecting None
        """
        pyramid = [
            [1],
            [2, 2],
            [3, 3, 3]
        ]
        target = 10
        result = find_target_pyramid(pyramid, target)
        self.assertIsNone(result, f"Expected None, got {result}")

    def test_single_row(self):
        """
        Single-row pyramid (target=5)
        
            5
        
        Path string is '', product is 5
        """
        pyramid = [[5]]
        target = 5
        result = find_target_pyramid(pyramid, target)
        self.assertEqual(result, "", f"Expected '', got {result}")

    def test_negative_case(self):
        """
        Extended example with a negative value
            2
          -1  -2
        
        L => 2 * -1 = -2
        """
        pyramid = [
            [2],
            [-1, -2]
        ]
        target = -2
        result = find_target_pyramid(pyramid, target)
        self.assertEqual(result, "L", f"Expected 'L', got {result}")


if __name__ == '__main__':
    unittest.main()