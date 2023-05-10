from datetime import datetime, date


# TODO tests
def format_date_from_timestamp(timestamp: float) -> date:
    """ Format Unix timestamp to date object."""
    return datetime.fromtimestamp(timestamp / 1000.0).date()


def format_date_from_string(date_string: str) -> date:
    """ Format date string to date object."""
    return datetime.strptime(date_string, '%Y-%m-%d').date()
