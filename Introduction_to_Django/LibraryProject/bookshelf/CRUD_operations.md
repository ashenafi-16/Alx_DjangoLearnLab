# CRUD Operations

**Create**
```python
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()
```
**Retrieve**
```
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
```
**Update**
```
book.title = "Nineteen Eighty-Four"
book.save()
```
**Delete**
```
book.delete()
```
