SELECT* FROM loans
JOIN books ON loans.book_id = books.id
JOIN members ON loans.member_id = members.id
WHERE loans.return_date IS NULL