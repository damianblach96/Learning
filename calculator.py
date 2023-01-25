# write your code here
import sys

memory = 0

msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def is_one_digit(v):
    v = float(v)
    if v.is_integer() and -10 < v < 10:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    v1 = float(v1)
    v2 = float(v2)
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    else:
        pass
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    else:
        pass
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_8
    else:
        pass
    if msg != "":
        msg = msg_9 + msg
    else:
        pass
    if msg == "":
        pass
    else:
        print(msg)

while True:
    operands = ["+", "-", "*", "/"]
    calc = input(msg_0)
    x, oper, y = calc.split()
    if x == "M":
        x = memory
        if y == "M":
            y = memory
        else:
            pass
    elif y == "M":
        y = memory
    else:
        pass

    try:
        float(x) and float(y)
    except Exception:
        print(msg_1)
        continue
    else:
        if oper in operands:
            pass
        else:
            print(msg_2)
            continue

    check(x, y, oper)
    x = float(x)
    y = float(y)

    if oper == "+":
        result = x + y
        print(result)
    elif oper == "-":
        result = x - y
        print(result)
    elif oper == "*":
        result = x * y
        print(result)
    elif oper == "/" and y != 0:
        result = x / y
        print(result)
    else:
        print(msg_3)
        continue

    while True:
        print(msg_4)
        ans = input()
        if ans == "y":
            if is_one_digit(result) == True:
                msg_index = 10
                while True:
                    msg = "msg_"
                    msgx = str(msg_index)
                    msg_ = globals()[msg + msgx]
                    print(msg_)
                    ans2 = input()
                    if ans2 == "y":
                        if msg_index < 12:
                            msg_index = msg_index + 1
                            pass
                        else:
                            memory = result
                            break
                    elif ans2 == "n":
                        break
                    else:
                        continue
            else:
                memory = result
                break
        elif ans == "n":
            break
        else:
            continue
        break
    while True:
        print(msg_5)
        con = input()
        if con == "y":
            break
        elif con == "n":
            sys.exit()
