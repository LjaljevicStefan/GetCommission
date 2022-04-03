import re

def check_input(date_str):
    '''
    Function for checking date input format
    
    Parameters
    ---------
    date_str : str
        String containing date in the format YYYY-MM-DD

    Returns
    -------
    1 or -1 value where 1 is for valid input format and -1 for invalid
    '''
    leap = False
    
    pattern = re.search(r'\d\d\d\d-\d\d-\d\d',date_str)

    if pattern != None:

        year = int(date_str[0]+date_str[1]+date_str[2]+date_str[3])
        month = int(date_str[5]+date_str[6])
        day = int(date_str[8]+date_str[9])
        
        if year % 4 == 0:
            leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False

        if month < 1 or month > 12 or day < 1 or day > 31:
            return -1
        elif (month in (2,4,6,9,11) and day >30) or (month == 2 and leap == True and day > 29) or (month == 2 and leap == False and day > 28):
            return -1
        else:
            return 1
    else:
        return -1

def get_commission(date_str = ''):
    '''Function for evaluating commission based on month in year
    
    Parameters
    ---------
    date_str : str
        String containing date in the format YYYY-MM-DD. Default is "".
        
    Returns
    -------
    Float, 0.1 is for 10% and 0.15 is for 15%.'''
    check = check_input(date_str)

    if check == 1:
        if int(date_str[6]) > 5:
            return 0.15
        else:
            return 0.1
    else:
        return check

if __name__ == '__main__':

    date_str = input("Please enter a date in the format 'YYYY-MM-DD': ")

    get_commission(date_str)