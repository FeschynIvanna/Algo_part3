import unittest


def find_unsorted_array(nums):
    if sorted(nums) == nums:
        return (-1, -1)

    left, right = 0, len(nums) - 1

    while nums[left] == min(nums[left:right+1]):
        left += 1

    while nums[right] == max(nums[left:right+1]):
        right -= 1

    return (left, right)


#def bubble_sorted(a):
    #is_sorted = True
    #for i in range(len(a)-1, 0, -1):
        #for j in range(0, i):
            #if a[j] > a[j+1]:
                #is_sorted = False
                #a[j], a[j+1] = a[j+1], a[j]

    #return is_sorted

#a = [2, 5, 3, 4, 1]
#bubble_sorted(a)
#print(a)


#print(find_unsorted_array([1, 2, 3, 4, 5]))

#print(find_unsorted_array([2, 5, 3, 4, 1]), [0, 5])

#print(find_unsorted_array([1, 2, 3, 4, 6, 5]), [4, 5])


class TestFindUnsortedArray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_array([1, 2, 3, 4, 5]), (-1, -1))

    def test_unsort_array(self):
        self.assertEqual(find_unsorted_array([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))

    def test_single_element_array(self):
        self.assertEqual(find_unsorted_array([1]), (-1, -1))


if __name__ == '__main__':

    unittest.main()