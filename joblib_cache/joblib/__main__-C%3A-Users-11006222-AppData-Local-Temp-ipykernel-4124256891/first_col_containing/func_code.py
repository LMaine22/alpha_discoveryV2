# first line: 1
@memory.cache
def first_col_containing(ticker_full_name, substr=''):
    """
    Finds the first column name in raw that matches the pattern 'ticker_full_name_substr'.
    Uses joblib.Memory for caching results across processes.
    """
    # This function relies on the global `raw` DataFrame.
    # Joblib's Memory decorator handles serialization of `raw` correctly for caching.
    
    if substr == 'PX_LAST':
        potential_col_name_long_price = f"{ticker_full_name}_Last_Price_PX_LAST"
        if potential_col_name_long_price in raw.columns:
            return potential_col_name_long_price

        potential_col_name_short_px = f"{ticker_full_name}_PX_LAST"
        if potential_col_name_short_px in raw.columns:
            return potential_col_name_short_px

    for c in raw.columns:
        if c.startswith(ticker_full_name) and substr in c:
            return c
    return None
