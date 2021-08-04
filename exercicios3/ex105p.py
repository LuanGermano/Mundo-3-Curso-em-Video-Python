def notas(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['média'] = sum(n) / len(n)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = "boa"
        elif r['média'] >= 5:
            r["Situação"] = 'Razoavel'
        else:
            r["Situação"] = "Ruim"
    return r


resp= notas(5,8,7,4, sit=True)
print(resp)