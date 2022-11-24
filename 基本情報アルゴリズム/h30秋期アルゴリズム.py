def compute(expression,explen):
    opcnt = 0
    value = [0,0,0,0,0]
    operator = ["","","",""]
    priority = [0,0,0,0]
    nest = 0
    for i in range(0,explen,1):
        chr1 = expression[i]
        if "0" <= chr1 and chr1 <= "9":
            value[opcnt] = 10 * value[opcnt] + int(chr1)
        if chr1 == "+" or chr1 == "-" or chr1 == "*" or chr1 == "/":
            operator[opcnt] = chr1
            if chr1 == "+" or chr1 == "-":
                priority[opcnt] = nest + 2
            else:
                priority[opcnt] = nest + 3
            opcnt += 1
            value[opcnt] = 0
        if chr1 == "(":
            nest += 2
        if chr1 == ")":
            nest -= 2
    while opcnt > 0:
        ip = 0
        for i in range(1,opcnt,1):
            if priority[ip] < priority[i]:
                ip = i
        chr1 = operator[ip]
        if chr1 == "+":
            value[ip] = value[ip] + value[ip + 1]
        if chr1 == "-":
            value[ip] = value[ip] - value[ip + 1]
        if chr1 == "*":
            value[ip] = value[ip] * value[ip + 1]
        if chr1 == "/":
            value[ip] = value[ip] / value[ip + 1]
        for i in range(ip + 1,opcnt,1):
            if value[i + 1] == False:
                value.append(0)
            value[i] = value[i + 1]
            operator[i - 1] = operator[i]
            priority[i - 1] = priority[i]
        opcnt -= 1
    return print(value[0])

expression = list("(12-3-1)/4/2")
explen = len(expression)
compute(expression,explen)
