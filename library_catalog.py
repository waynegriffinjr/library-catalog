'''Class hierarchy for managing a collection of books.'''

class Book:
    '''Initializes Book class with details and sets books as available by default.'''
    def __init__(self, title, author, year):
         # ensures that year must be a positive integer and handles any errors in input
        if not isinstance(year, int) or year <= 0:
            raise ValueError ("Year must be a positive integer.")
        if not isinstance (author, str) or author == "":
            raise ValueError ("Please enter valid    author.")
        if not isinstance (title, str) or title == "":
            raise ValueError ("Please enter valid title.")
    
        # attributes only set when input has been validatedd
        self.title = title
        self.author = author
        self.year = year
        self.checked_out = False
   
        
    def check_out(self):
        '''Book status checked, and if available, it is labeled as checked out.'''
       
        if self.checked_out:  #error handling
            return False
        else:
            self.checked_out = True
            return True
    
    def return_book(self):
        '''Book status checked, validated, and labled as returned and available.'''
        
        if self.checked_out:
            self.checked_out = False 
            return True
        else:
            return False 
        
    def is_available(self):
        if self.checked_out is False:
            return True
        else: return False
            
        
    def __repr__(self):
        '''Provides human-readable status check for individual titles.'''
        status = "❌ - Checked out" if self.checked_out else "✅ - Available" 
        return f"['{self.title}' - {self.year} - {self.author} ({status})]" 


class EBook(Book):
    
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
    
        # File Size validation.
        if not isinstance(file_size_mb, (int, float)) or file_size_mb <= 0:
            raise ValueError ("File Size must be a positive integer.")

        # EBook added attributes
        self.file_size_mb = file_size_mb
        self.checkout_count = 0

    def check_out(self):
            self.checkout_count += 1
            print(f"Checked out {self.checkout_count} times.")
            return True
        
    def return_book(self):
        if self.checkout_count > 0:   
            self.checkout_count -= 1
            return True
        else:
            return False
        
    def is_available(self):
        return True
        
    def __repr__(self):
        '''Provides human-readable status check for individual ebook titles.''' 
        return f"['eBook: {self.title}' - {self.year} - {self.author} ({self.file_size_mb} MB.)]" 
        
    
class Catalog:
    def __init__(self):
        self.book_list = []
        
    def add_book(self, item):
        self.book_list.append(item)
     
    def search_by_author(self, author):
        match_list = []
        for item in self.book_list:
            if author.lower() == item.author.lower():
                match_list.append(item)
        return match_list
        
    def search_by_title(self, keyword):
        match_list = []
        for item in self.book_list:
            if keyword.lower() in item.title.lower():
                match_list.append(item)
        return match_list

    def get_available(self):
        available_books = []
        for item in self.book_list:
            if item.is_available():
                available_books.append(item)
        return available_books
    
    def summary(self):
        return f"There are {len(self.book_list)} book resources in the catalog."


# Create a book
b = Book("Test Title", "Test Author", 2020)

# 1. Test initial state
print("Initial availability:", b.is_available())   # Expect True
print("Initial checked_out:", b.checked_out)       # Expect False

# 2. Test first checkout
result = b.check_out()
print("First checkout result:", result)            # Expect success message or True
print("Availability after checkout:", b.is_available())  # Expect False
print("checked_out after checkout:", b.checked_out)      # Expect True

# 3. Test second checkout (should not change state)
result = b.check_out()
print("Second checkout result:", result)           # Expect None or False
print("Availability still:", b.is_available())     # Expect False

# 4. Test returning the book
result = b.return_book()
print("Return result:", result)                    # Expect success message or True
print("Availability after return:", b.is_available())  # Expect True
print("checked_out after return:", b.checked_out)      # Expect False

# 5. Test returning again (should not change state)
result = b.return_book()
print("Second return result:", result)             # Expect None or False
print("Availability still:", b.is_available())     # Expect True

# 6. Test __repr__
print("Repr output:", repr(b))                     # Should show title, author, year, status

# 7. Test invalid year
try:
    Book("Bad", "Author", -5)
    print("ERROR: Negative year did NOT raise ValueError")
except ValueError:
    print("PASS: Negative year raised ValueError")

# 8. Test empty title
try:
    Book("", "Author", 2000)
    print("ERROR: Empty title did NOT raise ValueError")
except ValueError:
    print("PASS: Empty title raised ValueError")

# 9. Test empty author
try:
    Book("Title", "", 2000)
    print("ERROR: Empty author did NOT raise ValueError")
except ValueError:
    print("PASS: Empty author raised ValueError")

