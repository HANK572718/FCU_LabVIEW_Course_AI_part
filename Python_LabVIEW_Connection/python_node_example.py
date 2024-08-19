import json  # Required for the dict conversion

# Global variable TestList
TestList = [True, True, False]

# Function to return TestList
def return_list():
    x = TestList
    return x

# Global variable TestTuple
TestTuple = (2, 5, TestList)

# Function to return a list containing TestTuple twice
def return_tuple_list():
    x = [TestTuple, TestTuple]
    return x

# Function to return a list containing TestTuple twice
def return_tuple():
    # x = (3,4,[True,True, False])
    x = TestTuple

    return x

# Global variable TestDict
TestDict = {
    "String": "Test",
    "Number": 2,
    "Other number": 3
}

# Function to return TestDict as a JSON string
def return_dict():
    x = json.dumps(TestDict)
    return x

# Main execution block
if __name__ == "__main__":
    # Show results of the functions
    res_list = return_list()
    res_tuple = return_tuple()
    res_dict = return_dict()
    print("List returned:", res_list, type(res_list))
    print("Tuple returned:", res_tuple, type(res_tuple))
    print("Dict returned (JSON format):", res_dict, type(res_dict))
