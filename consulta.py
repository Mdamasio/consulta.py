import whois

def consultar_whois(dominio):
    try:
        info = whois.whois(dominio)
        return info
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    dominio = input("Digite o domínio que deseja consultar: ")
    resultado = consultar_whois(dominio)
    
    if isinstance(resultado, dict):
        for chave, valor in resultado.items():
            print(f"{chave}: {valor}")
    else:
        print("Erro ao consultar o WHOIS:", resultado)
