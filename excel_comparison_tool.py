import sys
import pandas as pd
from pathlib import Path


def main():
    if(len(sys.argv) < 2):
        print("Usage: Input a new and old xlsx sheet for comparison on the command line.")
        sys.exit()


    new = pd.read_excel(sys.argv[1]).fillna(0)
    old = pd.read_excel(sys.argv[2]).fillna(0)
    # Perform Diff
    diff = old.copy()
    for row in range(diff.shape[0]):
        for col in range(diff.shape[1]):
            value_OLD = old.iloc[row,col]
            try:
                value_NEW = new.iloc[row,col]
                if value_OLD==value_NEW:
                    diff.iloc[row,col] = new.iloc[row,col]
                else:
                    diff.iloc[row,col] = ('{}-->{}').format(value_OLD,value_NEW)
            except:
                diff.iloc[row,col] = ('{}-->{}').format(value_OLD, 'NaN')

    # Save output and format
    fname = 'old_vs_new.xlsx'
    writer = pd.ExcelWriter(fname, engine='xlsxwriter')

    diff.to_excel(writer, sheet_name='DIFF', index=False)
    new.to_excel(writer, sheet_name='old.stem', index=False)
    old.to_excel(writer, sheet_name='new.stem', index=False)

    # get xlsxwriter objects
    workbook  = writer.book
    worksheet = writer.sheets['DIFF']
    worksheet.hide_gridlines(2)

    # define formats
    date_fmt = workbook.add_format({'align': 'center', 'num_format': 'yyyy-mm-dd'})
    center_fmt = workbook.add_format({'align': 'center'})
    number_fmt = workbook.add_format({'align': 'center', 'num_format': '#,##0.00'})
    cur_fmt = workbook.add_format({'align': 'center', 'num_format': '$#,##0.00'})
    perc_fmt = workbook.add_format({'align': 'center', 'num_format': '0%'})
    grey_fmt = workbook.add_format({'font_color': '#E0E0E0'})
    highlight_fmt = workbook.add_format({'font_color': '#FF0000', 'bg_color':'#B1B3B3'})

    # set column width and format over columns
    # worksheet.set_column('J:AX', 5, number_fmt)

    # set format over range
    ## highlight changed cells
    worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                            'criteria': 'containing',
                                            'value':'-->',
                                            'format': highlight_fmt})
    ## highlight unchanged cells
    worksheet.conditional_format('A1:ZZ1000', {'type': 'text',
                                            'criteria': 'not containing',
                                            'value':'→',
                                            'format': grey_fmt})

    # save
    writer.save()


if __name__ == '__main__':
    main()
