import datetime


# TODO tests
def format_timestamp(timestamp: float, year: bool=True) -> str:
    """ Format  Unix timestamp to human readable date: 
        - if year is True: return date with year
        - if year is False: return date without year
    Returns:
        str: formatted date (e.g. 'May 09 2023' or 'May 09')
    """
    date = datetime.datetime.fromtimestamp(timestamp / 1000.0)
    FORMAT = '%B %d %Y' if year else '%B %d'

    return date.strftime(FORMAT)


def format_date(date_string: str, year: bool=True) -> float:
    """ Format date string to timestamp
    Returns:
        str: formatted date (e.g. 'May 09 2023' or 'May 09')
    """
    date_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    timestamp = date_obj.timestamp() * 1000
    return format_timestamp(timestamp, year=year)
