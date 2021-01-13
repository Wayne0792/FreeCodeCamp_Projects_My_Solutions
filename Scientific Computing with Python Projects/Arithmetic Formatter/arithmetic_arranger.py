def arithmetic_arranger(problems, sol=False):
    if len(problems) > 5:
      return "Error: Too many problems."
    problemss = [p.split() for p in problems]

    for p in problemss:
        if p[1] != '+' and p[1] != '-':
            return "Error: Operator must be '+' or '-'."
        if not(p[0].isnumeric() and p[2].isnumeric()):
            return "Error: Numbers must only contain digits."
        if len(p[0]) > 4 or len(p[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    n = len(problemss)
    #primeira linha da saida
    arranged_problems = ""
    for i in range(n):
        p = problemss[i]
        arranged_problems += "  "+(len(p[2]) - len(p[0]))*" " + p[0]
        if i < n-1: #após o último número não devemos imprimir quatro espaços
            arranged_problems += "    "
    arranged_problems += "\n"
    #segunda linha da saida
    for i in range(n):
        p = problemss[i]
        arranged_problems += p[1]+" "+(len(p[0]) - len(p[2]))*" "+p[2]
        if i < n-1: #após o último número não devemos imprimir quatro espaços
            arranged_problems += "    "
    arranged_problems += "\n"
    #terceira linha da saida
    for i in range(n):
        p = problemss[i]
        nt = (2 + max(len(p[0]), len(p[2])))
        arranged_problems += nt*"-"
        if i < n-1:
            arranged_problems += "    "
    #quarta linha (opcional)
    if sol:
        arranged_problems += "\n"
        for i in range(n):
            p = problemss[i]
            r = str(eval(''.join(p)))
            nt = (2 + max(len(p[0]), len(p[2])))
            arranged_problems += (nt-len(r))*" "+r
            if i < n-1:
                arranged_problems += "    "

    return arranged_problems
