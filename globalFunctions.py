def checkvalidDate(date:str) -> bool:
    dateParts = date.split('-')
    dateYear = dateParts[0]
    dateMonth = dateParts[1]
    dateDay = dateParts[2]
    
    if len(dateYear) == 4 and len(dateMonth) == 2 and len(dateDay) == 2:
        dateMonth = int(dateMonth)
        dateDay = int(dateDay)
        if 0<dateMonth<=12 and 0<dateDay<31:
            try:
                int(dateMonth/2)
                if dateMonth == 2:
                    if dateDay <= 28:
                        return True
                elif dateDay <= 31:
                    return True
                else: 
                    return False
            except:
                if dateDay <= 30:
                    return True
                else:
                    return False
        else:
            return False
    else: 
        return False