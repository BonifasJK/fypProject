from datetime import timedelta

def date_range(start, end):
    """Generate dates from start to end inclusive."""
    delta = end - start  # as timedelta
    days = [start + timedelta(days=i) for i in range(delta.days + 1)]
    return days
