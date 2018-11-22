# working with everything we have learned so far in the chapter

# storing the titles of a serie of books by Dan Brown
book_one = "Angels and Demons"
book_two = "Davincci Code"
book_three = "The Lost Symbole"
book_four = "Inferno"
# another book that is not with the serie
book_out = "Deception Point"
# making the list that will contain the books
serie = []

# adding the books to the serie by different methods
serie.append(book_one)
serie.insert(1,book_two)
serie.insert(2,book_three)
serie.append(book_four)
serie.insert(4,book_out)

# remove the book that is not included in the serie
removed = serie.pop()
print("We have removed this book from the serie,",removed.title())

# show the list
print(serie)
# show the sorted list
print(sorted(serie))

# sort the list now
serie.sort()
print(sorted_serie)

# reverse the list
serie.reverse()
print(serie)

# reverse back to original
serie.reverse()
print(serie)
