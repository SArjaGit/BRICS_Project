class Helper:  
  # Function to standardize column names
  @staticmethod
  def year_col_name(cols):
    new_cols = []
    for col in cols:
        if '[YR' in col: # if it's a year col, append only the number
            new_cols.append(col.split(' ')[0])
        elif ' ' in col: # this must be the second check due to ambiguity
            new_cols.append(col.replace(' ', '_'))
        else: # if the column doesn't meet any criteria, append it as it is
            new_cols.append(col)
    return new_cols
