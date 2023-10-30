from fastapi import FastAPI

app = FastAPI()

@app.get("/calculator/{number1}/{number2}/{sign}")
def calculator(number1: float, number2: float, sign: str):
    if sign == '+':
        return {number1 + number2}
    elif sign == '-':
        return {number1 - number2}
    elif sign == '*':
        return {number1 * number2}
    elif sign == ':':
        if number2 == 0:
            return {"No devision by zero allowed!"}
        else:
            return {number1 / number2}
    else:
        return {"Please, enter a sign from [+, -, *, :]"}