# Scenario: 
# You have a list of users returned from a Django ORM query. 
# Filter only the active admins without hitting the database again.

users = [
    {"id": 1, "name": "Alice", "role": "admin", "is_active": True},
    {"id": 2, "name": "Bob", "role": "editor", "is_active": True},
    {"id": 3, "name": "Charlie", "role": "admin", "is_active": False},
    {"id": 4, "name": "Diana", "role": "admin", "is_active": True},
]

def filter_active_admin(users):
    result = []

    for user in users:
        if user["role"] == "admin" and user["is_active"]:
            result.append(user)
    return result

ActiveUsers = filter_active_admin(users)
print("Active users are: ",ActiveUsers)