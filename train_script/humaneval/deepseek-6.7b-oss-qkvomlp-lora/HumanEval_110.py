def exchange(lst1, lst2):
    # Check if all elements of lst1 are even
    if all(num % 2 == 0 for num in lst1):
        return "YES"
    
    # Check if it is possible to exchange elements between lst1 and lst2 to make all elements of lst1 even
    for num1 in lst1:
        if num1 % 2 != 0:
            for num2 in lst2:
                if num2 % 2 == 0:
                    # Exchange elements
                    lst1[lst1.index(num1)] = num2
                    lst2[lst2.index(num2)] = num1
                    # Check if all elements of lst1 are even after exchange
                    if all(num % 2 == 0 for num in lst1):
                        return "YES"
                    else:
                        # Revert the exchange
                        lst1[lst1.index(num2)] = num1
                        lst2[lst2.index(num1)] = num2
    return "NO"