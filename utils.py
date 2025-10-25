"""
utils.py

Contains small, reusable helper functions.
"""

def safe_convert_to_float(data_dict: dict, key: str):
    """
    Safely gets a value from a dictionary, converts it to float.
    Returns None if the key doesn't exist or if conversion fails.
    """
    value = data_dict.get(key)
    try:
        return float(value)
    except (ValueError, TypeError):
        return None