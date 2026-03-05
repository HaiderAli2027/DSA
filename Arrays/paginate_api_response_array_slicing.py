# Scenario: 
# You're building a Flask REST endpoint. 
# The client sends page and page_size params. 
# Slice the in-memory result list accordingly.

products = [f"Products_{i}" for i in range(1,50)]

def paginate(data, page, page_size):
    total = len(data)
    start = (page - 1) * page_size
    end  = start + page_size

    if start >= total:
        return {"data": [], "total": total, "page": page, "pages": -(-total // page_size)}
    
    return {
        "data": data[start:end],
        "total": total,
        "page": page,
        "pages": -(-total // page_size)
    }
print(paginate(products,page=2,page_size=10))
print(paginate(products,page=6,page_size=10))


"""
The Ceiling Division Trick in Data Structures and Algorithms (DSA) is 
a small mathematical trick used to divide two integers 
and round the result up to the nearest integer.
"""