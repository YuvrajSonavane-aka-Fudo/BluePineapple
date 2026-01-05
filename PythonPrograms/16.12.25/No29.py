def countOddOccurance(list1):
    listOfOddOccuringElements = list(filter(lambda x : list1.count(x)%2!=0 , list1))
    print(listOfOddOccuringElements)

countOddOccurance([1,2,3,5,5])