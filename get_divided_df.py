def get_divided_df(c_id1,c_id2):
    # select columns other than 'Opportunity Number','Opportunity Result'
    cols = [col for col in df.columns if col not in [c_id1,c_id2]]
    # dropping the 'Opportunity Number'and 'Opportunity Result' columns
    global data, target
    data = df[cols]
    #assigning the Oppurtunity Result column as target
    target = df[c_id1]
    return data.head(2)
get_divided_df('Opportunity Number','Opportunity Result')