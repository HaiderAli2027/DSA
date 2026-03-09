"""
Scenario: 
    You're building a rate limiter check in Flask. 
    Given an array of request timestamps (in seconds) for a user, 
    find the maximum number of requests made 
    in any 60-second window — to detect if they breached the limit.
"""

timestamps = [100, 109, 110, 111, 112, 113, 114, 115, 116, 119, 130, 150, 160, 170, 200, 210, 220, 230,
              240, 250, 290, 300, 310, 320, 330, 340, 350, 360]
window = 60
LIMIT = 10

def Max_Request_In_Window(timestamps, window):
    left = 0
    max_count = 0

    for right in range(len(timestamps)):
        while timestamps[right] - timestamps[left] >= window:
            left += 1
        
        count = right - left + 1
        max_count = max(max_count, count)
    return max_count

peak = Max_Request_In_Window(timestamps, window)
print(f'Max requests in any {window}-second window: {peak}')
print(f"Rate limit {'BREACHED' if peak > LIMIT else 'OK'}")

