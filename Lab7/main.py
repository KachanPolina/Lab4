from datetime import datetime


def calculate_response_time(time_list):
    """
    >>> data = [
    ... {"create_time": "10:15", "response_time": "10:20"},
    ... {"create_time": "13:00", "response_time": "13:02"},
    ... {"create_time": "09:12", "response_time": "09:55"},
    ... ]
    >>> calculate_response_time(data)
    16.67
    """
    """
    >>> data = [
    ... {"create_time": "10:15", "response_time": "10:20"},
    ... ]
    >>> calculate_response_time(data)
    5.00
    """
    """
    >>> data = [
    ... {"create_time": "10:20", "response_time": "10:21"},
    ... {"create_time": "13:00", "response_time": "13:40"},
    ... ]
    >>> calculate_response_time(data)
    20.50
    """
    difference_arr = []
    for time in time_list:
        create_time = datetime.strptime(time['create_time'], "%H:%M")
        response_time = datetime.strptime(time['response_time'], "%H:%M")
        difference = response_time - create_time
        difference_arr.append(difference.total_seconds())

    return round(float((sum(difference_arr) / len(difference_arr)) / 60), 2)


data = [
    {"create_time": "10:15", "response_time": "10:20"},
    {"create_time": "13:00", "response_time": "13:02"},
    {"create_time": "09:12", "response_time": "09:55"},
]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(calculate_response_time(data))
