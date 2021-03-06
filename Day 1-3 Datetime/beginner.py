from datetime import date, timedelta

start_100days = date(2018, 7, 24)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    hundred_days = timedelta(days=100)
    return str(start_100days + hundred_days)


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return pycon_date - pybites_founded


print(get_hundred_days_end_date())
print(str(get_days_between_pb_start_first_joint_pycon()))