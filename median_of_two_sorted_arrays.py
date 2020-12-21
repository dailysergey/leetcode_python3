class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        l = len(nums1)
        m = 0.0
        if l%2 == 0:
            m = (nums1[l//2] + nums1[(l//2) - 1]) / 2
        else:
            m = nums1[l//2]
        return m
        '''
        '''
        1. Найти такую точку, которая больше левой части и меньше правой - точка опоры
        x x [x] | [x] x x  lLong, rLong
          y [y] | [y]  y   lShort, rShort
          
          x x y [y] [x] | [y] y x x
        2. Точка опоры в меньшем массиве имеет себе подобную в большем массиве(списке)
        3. После определения точки опоры, можно узнать куда нужно свигаться, т.е. направление
        4. Что делаем:
            a. Бинарный поиск в меньшнем списке
            b. Получаем индексы соответствующих опорных точек 
            с. Получаем направление куда сдвигать один массив
            d. Получаем результат
            
        Time: O(log(n))
        Space: O(1)
        n - число элементов в меньшем списке
        '''
        def getVal(arr, i):
            '''Get value at index i of array arr'''
            if i == -1:
                return float('-inf')
            if i == len(arr):
                return float('inf')
            return arr[i]

        def getIndices(rShort, aShort, aLong):
            '''Get indices'''
            midIndex = int((len(aShort) + len(aLong)) / 2)
            rLong = midIndex - rShort
            return (rShort - 1, rShort, rLong - 1, rLong)

        def getResult(lShort, rShort, lLong, rLong, aShort, aLong):
            odd = (len(aShort) + len(aLong)) % 2
            if odd:
                return min(getVal(aLong, rLong), getVal(aShort, rShort))
            else:
                return (max(getVal(aShort, lShort), getVal(aLong, lLong))
                        + min(getVal(aShort, rShort), getVal(aLong, rLong))) / 2

        def getDirection(lShort, rShort, lLong, rLong, aShort, aLong):
            '''Determine direction'''
            if getVal(aShort, lShort) > getVal(aLong, rLong):
                return -1
            elif getVal(aLong, lLong) > getVal(aShort, rShort):
                return 1
            else:
                return 0

        # determine long and short arrays
        aShort = nums1
        aLong = nums2
        if len(nums1) > len(nums2):
            aShort = nums2
            aLong = nums1

        # temp vars
        lShort = rShort = lLong = rLong = d = 1

        # binary search

        l = 0
        r = len(aShort)
        while d != 0:
            m = int((l+r) / 2)
            # get indices from m
            lShort, rShort, lLong, rLong = getIndices(m, aShort, aLong)

            # get direction
            d = getDirection(lShort, rShort, lLong, rLong, aShort, aLong)

            if d < 0:
                r = m - 1
            elif d > 0:
                l = m + 1

        # calculate median
        return getResult(lShort, rShort, lLong, rLong, aShort, aLong)
