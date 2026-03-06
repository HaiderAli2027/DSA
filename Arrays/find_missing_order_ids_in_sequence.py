"""
Scenario: 
    Your Flask order service expects sequential order IDs.
    After a bulk insert, you get back the created IDs. 
    Find which ones are missing — they failed to insert.

"""
expected_ids = list(range(1001, 1021))
created_ids = [1001, 1002, 1003, 1007, 1008, 1010, 1011, 
               1012, 1013, 1014, 1016, 1017, 1018, 1020]

def find_missing_ids(expected, created):
    missing = []
    created_set = set(created)

    for order_id in expected:

        if order_id not in created_set:

            missing.append(order_id)
    
    return missing
print(find_missing_ids(expected_ids, created_ids))










"""
What is a set in Python?

    A set is a collection that:

        removes duplicate values

        does not keep order

        allows fast lookup
"""