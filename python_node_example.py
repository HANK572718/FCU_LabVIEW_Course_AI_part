import json  # Required for the dict conversion

TestList = [True, True, False]


def return_list():
    x = TestList
    return x


##
TestTuple = (3, 5, "TestList")


def return_tuple():
    x = [TestTuple, TestTuple]
    return x


##
TestDict = {
    "String": "Test",
    "Number": 2,
    "Other number": 3
}


def return_dict():
    x = json.dumps(TestDict)
    return x
