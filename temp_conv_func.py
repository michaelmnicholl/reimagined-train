def fahrenheit(celsius):
    """convert degrees celsius to fahrenheit"""
    return ((9 * celsius)/5) + 32

def fahrenheit_list(celsius_list):
    """convert a list of temperatures in degrees celsius to fahrenheit"""
    fahrenheit_lst = []
    for celsius_temp in celsius_list:
        fahrenheit_temp = fahrenheit(celsius_temp)
        fahrenheit_lst = fahrenheit_lst + [fahrenheit_temp]
    return fahrenheit_lst



        
    
