import pandas as pd
import numpy as np

def effective_date_order(df, by=['emplid', 'adm_appl_nbr', 'appl_prog_nbr'],
                         dates=['effdt', 'effseq']):
    return df.sort_values(by=by+dates,
                          ascending=[True]*len(by)+
                          [False]*len(dates)).groupby(by=by).cumcount()
    
def most_recent_rows(df, by=['emplid', 'adm_appl_nbr', 'appl_prog_nbr'],
                         dates=['effdt', 'effseq']):
    df['order'] = effective_date_order(df, by, dates)
    return df[df['order']==0].drop('order', axis=1)
    

def check_for_action(df1, df2, action):
    """
        Determine if the applicant had ever had their PROG_ACTION field have
        the value specified in the action parameter.

        This function takes two dataframes and an action string.
        The first dataframe is the filtered data - and it will NOT be altered!
        The second data frame is ALL rows from the PS_ADM_APPL_PROG table.

        We are generally checking for 'APPL' (applied), 'ADMT' (admit),
        'COND' (conditional admit) or 'MATR' (matriculation).

        This function compares the action string to what is in the database, so
        submit an uppercase string. It will create a new column in the dataframe
        passed as df1

        It works by grouping the unfiltered data - seeing if the particular
        action happens in that table... then creating a boolean variable.

        The function returns df1 with the additional column added.
    """
    return pd.merge(df1,
                    df2.groupby(by=['emplid',
                                    'adm_appl_nbr',
                                    'appl_prog_nbr']
                               ).prog_action
                                .transform(lambda x : '{}'.format(action)
                                           in x.values
                                          ).to_frame(name='has_{}'.format(
                                              action.lower())),
                    how='left',
                    left_index=True,
                    right_index=True)

def check_appl_admt_order(df2):
    return df2[((df2.prog_action==
                 'APPL') |
                (df2.prog_action==
                 'COND') |
                (df2.prog_action==
                 'ADMT'))].sort_values(by=['emplid',
                                           'adm_appl_nbr',
                                           'appl_prog_nbr',
                                           'effdt',
                                           'effseq'],
                                       ascending=[True,
                                                  True,
                                                  True,
                                                  False,
                                                  False]).groupby(by=['emplid',
                                                                      'adm_appl_nbr',
                                                                      'appl_prog_nbr']
                                                                 )['prog_action'].head(1).rename("last_appl_admt")