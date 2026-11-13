
eventos = {
    "sao paulo": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa São Paulo de Futebol Amador", "nivel": "Intermediário", "vagas": 25},
            {"nome": "Torneio Metropolitano de Futebol", "nivel": "Avançado", "vagas": 20}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel": "Iniciante", "vagas": 25},
            {"nome": "Copa Paulista de Basquete", "nivel": "Intermediário", "vagas": 20},
            {"nome": "Torneio Metropolitano de Basquete", "nivel": "Avançado", "vagas": 15}
        ],
        "tenis": [
            {"nome": "Torneio Municipal de Tênis", "nivel": "Iniciante", "vagas": 20},
            {"nome": "Copa Paulista de Tênis", "nivel": "Intermediário", "vagas": 15},
            {"nome": "Circuito Metropolitano de Tênis", "nivel": "Avançado", "vagas": 10}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa Paulista de Vôlei", "nivel": "Intermediário", "vagas": 25},
            {"nome": "Torneio Metropolitano de Vôlei", "nivel": "Avançado", "vagas": 20}
        ]
    },

    "osasco": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa Osasco de Futebol", "nivel": "Intermediário", "vagas": 20}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel": "Iniciante", "vagas": 25},
            {"nome": "Copa Osasco de Basquete", "nivel": "Intermediário", "vagas": 20}
        ]
    },

    "guarulhos": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa Guarulhos de Futebol", "nivel": "Intermediário", "vagas": 20}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa Guarulhos de Vôlei", "nivel": "Intermediário", "vagas": 20}
        ]
    },

    "campinas": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa Campinas de Futebol", "nivel": "Intermediário", "vagas": 25}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel": "Iniciante", "vagas": 25},
            {"nome": "Copa Campinas de Basquete", "nivel": "Intermediário", "vagas": 20}
        ]
    },

    "são bernardo do campo": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel": "Iniciante", "vagas": 30},
            {"nome": "Copa São Bernardo de Futebol", "nivel": "Intermediário", "vagas": 20}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei", "nivel": "Iniciante", "vagas": 25},
            {"nome": "Copa São Bernardo de Vôlei", "nivel": "Intermediário", "vagas": 20}
        ]
    }
}


modalidades = [
    "futebol",
    "basquete",
    "volei",
    "tenis"
]

niveis = [
    "Iniciante",
    "Intermediário",
    "Avançado"
]

inscricoes = []

classificacao = {
    "Iniciante": 1,
    "Intermediário": 2,
    "Avançado": 3
}

usuario_atual = None

def meus_eventos():
    print("\n--- PARTICIPAÇÃO DE EVENTOS ---\n")

    if usuario_atual is None:
        print("Você não possui usuário cadastrado")
        return

    if not usuario_atual["eventos"]:
        print("Você não está participando de nenhum evento.")
        return

    for evento in usuario_atual["eventos"]:
        print(f"Evento: {evento['nome']}")
        print(f"Nível: {evento['nivel']}")
        print(f"Vagas restantes: {evento['vagas']}")
        print("-------------------")

def inscricao_evento(regiao, mod, usuario_atual):
    lista_eventos = eventos[regiao][mod]

    for i, ev in enumerate(lista_eventos, start=1):
        print(f"{i}. {ev['nome']}")

    escolha = input("Digite o número do evento: ").strip()

    if not escolha.isdigit() or not 1 <= int(escolha) <= len(lista_eventos):
        print("Evento inválido")
        return

    evento = lista_eventos[int(escolha) - 1]

    if classificacao[usuario_atual["nivel"]] < classificacao[evento["nivel"]]:
        print("Seu nível é insuficiente para participar desse evento.")
        return

    if evento["vagas"] <= 0:
        print("Não há vagas disponíveis.")
        return

    if evento["nome"] in [ev["nome"] for ev in usuario_atual["eventos"]]:
        print("Você já está participando desse evento.")
        return

    usuario_atual["eventos"].append(evento)
    evento["vagas"] -= 1

    print(f"Inscrição realizada em {evento['nome']}!")

def consultar_inscricoes(inscricoes):
    print("\n-- INSCRIÇÕES --\n")

    if not inscricoes:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in inscricoes:
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print(f"Telefone: {usuario['telefone']}")
        print(f"Modalidade: {usuario['modalidade']}")
        print(f"Nível: {usuario['nivel']}")
        print("-------------------")

def verificar_email(email):
    for usuario in inscricoes:
        if usuario["email"].lower() == email.strip().lower():
            return False

    return True

def cadastro():
    global usuario_atual
    print("Esse é o menu de inscrição para jogar nas equipes da PonteEsportes\n")
    print("Digite seus dados cadastrais: ")
    nome = input("\nNome: ")
    email = input("Email: ")

    if not verificar_email(email):
        print("Este email já está cadastrado.")
        return

    telefone = input("Telefone: ").strip()

    print("\nQual sua modalidade de preferência?\n")
    for i, mod in enumerate(modalidades, start=1):
        print(f" {i}. {mod.title()}")

    pref = input("\n")

    if pref.isdigit() and 1 <= int(pref) <= len(modalidades):
            pref = modalidades[int(pref) - 1]
    else:
        print("Modalidade inválida")
        return

    print("\nQual seu nível nessa modalidade(1 à 3)?\n")
    for i, nivel in enumerate(niveis, start=1):
        print(f"{i}. {nivel.title()}")

    level = input("\n").strip()

    if level.isdigit() and 1 <= int(level) <= len(niveis):
        level = niveis[int(level) - 1]
    else:
        print("Nível inválido.")
        return

    usuario = {
        "nome": nome.title(),
        "email": email.strip(),
        "telefone": telefone.strip(),
        "modalidade": pref,
        "nivel": level,
        "eventos": []
    }

    usuario_atual = usuario
    inscricoes.append(usuario)

    print("\nSEU USUÁRIO FOI CADASTRADO COM SUCESSO!\n")


def consultar_eventos(mod, regiao):

    if usuario_atual is None:
        print("Você precisa realizar seu cadastro antes de consultar os eventos.")
        return

    if usuario_atual["modalidade"] != mod:
        print(f"Você está cadastrado na modalidade {usuario_atual['modalidade'].title()}.")
        return

    if mod in eventos[regiao]:
        for i, ev in enumerate(eventos[regiao][mod], start=1):
            print(f"\n{i}. {ev['nome']}")
            print(f"Nível: {ev['nivel']}")
            print(f"Vagas: {ev['vagas']}")
    else:
        print("Modalidade inválida")
        return

    part = input("\nGostaria de se inscrever em algum evento(sim ou não)?\n").lower().strip()

    if part == "sim":
        inscricao_evento(regiao, mod, usuario_atual)

    elif part == "não" or part == "nao":
        return

    else:
        print("Resposta inválida.")
        return


def modalidade(regiao):
    if regiao in eventos:
        lista_modalidades = list(eventos[regiao].keys())

        for i, mod in enumerate(lista_modalidades, start=1):
            print(f" {i}. {mod.title()}")

        escolha = input("\nEscolha uma modalidade: ").strip()

        if escolha.isdigit() and 1 <= int(escolha) <= len(lista_modalidades):
            mod = lista_modalidades[int(escolha) - 1]
            consultar_eventos(mod, regiao)
        else:
            print("Modalidade inválida")

def regioes():
    print("-- LOCAIS DE EVENTOS --")

    for i, regiao in enumerate(eventos, start=1):
        print(f"{i}. {regiao.title()}")

    regiao = input("Escolha uma região(1 à 5): ").strip()

    lista_regioes = list(eventos.keys())

    if regiao.isdigit() and 1 <= int(regiao) <= len(lista_regioes):
        regiao = lista_regioes[int(regiao) - 1]
        modalidade(regiao)
    else:
        print("Região inválida")


def main():
    while True:
        print("\n--- MENU DE BUSCA ---")
        print("1. Cadastro")
        print("2. Eventos")
        print("3. Meus Eventos")
        print("4. Consultar inscrições")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        match opcao:
            case "1":
                cadastro()
            case "2":
                regioes()
            case "3":
                meus_eventos()
            case "4":
                consultar_inscricoes(inscricoes)
            case "0":
                print("\nEncerrando o sistema...")
                break
            case _:
                print("\n[!] Opção inválida.")

main()