def generate_code(row,column):
    code_number=(row*(row-1)//2+1)
    for i in range(1,column):
        code_number+=i+row
    code=20151125
    for i in range(code_number-1):
        code=code*252533%33554393
    return code
