import unittest

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def pages(self):
        "Create the actual sub lists that represent the pages and the maximum number of items per page"
        result = []
        current_group = []

        for item in self.collection:
            current_group.append(item)

            if len(current_group) == self.items_per_page:
                result.append(current_group)
                current_group = []

        if current_group:
            result.append(current_group)

        return result   
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        return len(self.pages())
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index > len(self.pages())-1:
            return -1
        return len(self.pages()[page_index])
        
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if not self.collection or item_index < 0:
            return -1
        
        if item_index > len(self.collection) - 1:
            return -1
        
        for index, page in enumerate(self.pages()):
            if self.collection[item_index] in page:
                return index
        return -1
        

collection = ['a','b','c','d','e','f']
helper = PaginationHelper(collection, 4)

class PaginationHelperTest(unittest.TestCase):

    def setUp(self):
        self.collection = ['a','b','c','d','e','f']
        self.helper = PaginationHelper(self.collection, 4)  
    
    def test_item_count(self):
        self.assertEqual(self.helper.item_count(), 6, 'page_count is returning incorrect value.')

    def test_page_count(self):
        self.assertEqual(self.helper.page_count(), 2, 'item_count returned incorrect value')

    def test_page_item_count(self):
        self.assertEqual(self.helper.page_item_count(0), 4, 'page_item_count returned incorrect value for page 0.')
        self.assertEqual(self.helper.page_item_count(1), 2, 'page_item_count returned incorrect value for page 1.')
        self.assertEqual(self.helper.page_item_count(2), -1, 'page_item_count should return -1 for page_index values that are out of range.')

    def test_page_index(self):
        self.assertEqual(self.helper.page_index(5), 1, 'page_index returned incorrect value for item_index 5.')
        self.assertEqual(self.helper.page_index(2), 0, 'page_index returned incorrect value for item_index 2.')
        self.assertEqual(self.helper.page_index(20), -1, 'page_index should return -1 for item_index values that are out of range.')
        self.assertEqual(self.helper.page_index(-10), -1, 'page_index should return -1 for item_index values that are out of range.')

if __name__ == '__main__':
    unittest.main()

    