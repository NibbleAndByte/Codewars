import math

class PaginationHelper:

  # The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
  def __init__(self, collection, items_per_page):
      self.itemsPerPage = items_per_page
      self.collection = collection
  
  # returns the number of items within the entire collection
  def item_count(self):
      return len(self.collection)
      
  
  # returns the number of pages
  def page_count(self):
      return math.ceil(float(len(self.collection)) / self.itemsPerPage)
      
	
  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
  def page_item_count(self,page_index):
      totalValue = (page_index + 1) * self.itemsPerPage
      overlap = totalValue - len(self.collection)
      
      if  overlap > self.itemsPerPage:
          return -1
      elif  overlap > 0 and overlap <= self.itemsPerPage:
          return self.itemsPerPage - overlap
      else:
          return self.itemsPerPage

  # determines what page an item is on. Zero based indexes.
  # this method should return -1 for item_index values that are out of range
  def page_index(self,item_index):
      if item_index >= len(self.collection) or len(self.collection) == 0 or item_index < 0:
          return -1
      return item_index / self.itemsPerPage
      
      
  