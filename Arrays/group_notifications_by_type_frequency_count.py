"""
Scenario: 
    Your Django app sends notifications.
    You receive a flat list of notification types from the last 24 hours.
    Count how many of each type 
    fired — to display a grouped notification badge in the frontend.
"""

notification = [
    'comment', 'like', 'follow', 'comment', 'like', 'comment', 'mention', 'like', 'follow', 'mention',
    'comment', 'like', 'follow', 'comment', 'mention', 'like', 'follow', 'comment', 'like', 'mention'
]

def count_notifications_by_type(notification_list):
    freq = {}
    for notif in notification_list:
        if notif in freq:
            freq[notif] += 1
        else:
            freq[notif] = 1
    sorted_freq = sorted(freq.items(), key= lambda x: x[1], reverse=True)
    return sorted_freq


print(count_notifications_by_type(notification))


