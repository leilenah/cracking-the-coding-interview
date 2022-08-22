# Run Command: Ctrl + Option + N
# pg. 46


def example1(array = []):
    """
    Runtime: O(n)
    """
    sum = 0
    product = 1

    # O(n) - linear
    for num in array:
        sum += num

    # O(n) - linear
    for num in array:
        product *= num


def example2(array = []):
    """
    Runtime: O(n^2)
    """
    # O(n)
    for num in array:
        # O(n)
        for num_again in array:
            print()


def example3(array = []):
    """
    Runtime: O(n^2)
    """
    # O(n)
    for i in range(0, len(array)):

        # O(1)
        j = i + 1

        # O(n)
        for j in range(len(array)):
            print()


def example4(arrayA = [], arrayB = []):
    """
    Runtime: O(ab)
    a = len(arrayA)
    b = len(arrayB)
    """

    # O(a)
    for i in range(0, len(arrayA)):

        # O(b)
        for j in range(0, len(arrayB)):

            # O(1)
            if (arrayA[i] < arrayB[j]):
                print()


def example5(arrayA = [], arrayB = []):
    """
    Runtime: O(ab)
    a = len(arrayA)
    b = len(arrayB)
    """

    # O(a)
    for i in range(0, len(arrayA)):

        # O(b)
        for j in range(0, len(arrayB)):

            # O(1)
            for k in range(0, 100000):
                print()


def example6(array = []):
    """
    Runtime: O(n)
    """
    # O(n)
    for i in range(0, (len(array) / 2)):
        # do O(1) stuff


def example7():
    """
    Which of the following are equivalent to O(n)?

    1. O(n + p) where p < n / 2
        - since p is less than n, we know that n is the dominant term
        - we can drop the non-dominant term in this case, which is p
        - O(n + p) == O(n)

    2. O(2n)
        - we can drop constants
        - O(2n) == O(n)

    3. O(n + log n)
        - we can drop the non-dominant term, log n
        - O(n + log n) == O(m)

    4. O(n + m)
        - this is not equvalent to O(n) since we don't know the relationship
    """


def example8(array = []):
    """
    Algorithm:
        1. take in array of strings
        2. sort each string
        3. sort the full array

    let s = the length of the longest string
    let a = the length of the array

    Runtime: O(a*s(log a + log s))
    """

    # O(a)
    for string in array:

        # O(s log s)
        # sort each string

    # O(a*s log a)
    # sort the array


def example9(node = None):
    """
    Runtime: O(n)
    """
    # O(1)
    if (node == None):
        return 0

    # O(n)
    return example9(node.left) + node.value + example9(node.right)

