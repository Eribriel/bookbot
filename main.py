import sys
if len(sys.argv) == 2:
    import stats
    book_path = sys.argv[1]
    stats.sorted_list(book_path)
    
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    