
# ==========================================
# 1. BASE DE DADOS DOS EVENTOS
# ==========================================

# Organiza os eventos por região e modalidade.
# Cada evento possui nome, nível exigido e vagas disponíveis.

from datetime import date

eventos = {
    "sao paulo": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 10, 20), "cancelado": True},
            {"nome": "Copa São Paulo de Futebol Amador", "nivel":
                "Intermediário", "vagas": 0, "data": date(2026, 12, 15), "cancelado": False},
            {"nome": "Torneio Metropolitano de Futebol", "nivel":
                "Avançado", "vagas": 20, "data": date(2027, 2, 10), "cancelado": False}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel":
                "Iniciante", "vagas": 1, "data": date(2026, 11, 25), "cancelado": False},
            {"nome": "Copa Paulista de Basquete", "nivel":
                "Intermediário", "vagas": 20, "data": date(2026, 9, 15), "cancelado": False},
            {"nome": "Torneio Metropolitano de Basquete", "nivel":
                "Avançado", "vagas": 15, "data": date(2027, 3, 20), "cancelado": True}
        ],
        "tenis": [
            {"nome": "Torneio Municipal de Tênis", "nivel":
                "Iniciante", "vagas": 0, "data": date(2027, 1, 12), "cancelado": True},
            {"nome": "Copa Paulista de Tênis", "nivel":
                "Intermediário", "vagas": 15, "data": date(2026, 10, 5), "cancelado": False},
            {"nome": "Circuito Metropolitano de Tênis",
             "nivel": "Avançado", "vagas": 10, "data": date(2027, 4, 18), "cancelado": True}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei",
             "nivel": "Iniciante", "vagas": 30, "data": date(2026, 12, 5), "cancelado": True},
            {"nome": "Copa Paulista de Vôlei", "nivel":
                "Intermediário", "vagas": 3, "data": date(2026, 8, 20), "cancelado": True},
            {"nome": "Torneio Metropolitano de Vôlei", "nivel":
                "Avançado", "vagas": 20, "data": date(2027, 5, 10), "cancelado": False}
        ]
    },

    "osasco": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 11, 30), "cancelado": True},
            {"nome": "Copa Osasco de Futebol", "nivel":
                "Intermediário", "vagas": 20, "data": date(2026, 9, 10), "cancelado": True}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel":
                "Iniciante", "vagas": 25, "data": date(2027, 2, 15), "cancelado": True},
            {"nome": "Copa Osasco de Basquete", "nivel":
                "Intermediário", "vagas": 20, "data": date(2026, 12, 20), "cancelado": True}
        ]
    },

    "guarulhos": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 7, 15), "cancelado": False},
            {"nome": "Copa Guarulhos de Futebol", "nivel":
                "Intermediário", "vagas": 20, "data": date(2027, 1, 25), "cancelado": True}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 12, 10), "cancelado": True},
            {"nome": "Copa Guarulhos de Vôlei", "nivel":
                "Intermediário", "vagas": 20, "data": date(2027, 3, 5), "cancelado": False}
        ]
    },

    "campinas": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 10, 12), "cancelado": True},
            {"nome": "Copa Campinas de Futebol", "nivel":
                "Intermediário", "vagas": 25, "data": date(2027, 2, 28), "cancelado": False}
        ],
        "basquete": [
            {"nome": "Campeonato Municipal de Basquete", "nivel":
                "Iniciante", "vagas": 25, "data": date(2026, 12, 18), "cancelado": False},
            {"nome": "Copa Campinas de Basquete", "nivel":
                "Intermediário", "vagas": 20, "data": date(2027, 4, 8), "cancelado": True}
        ]
    },

    "são bernardo do campo": {
        "futebol": [
            {"nome": "Campeonato Municipal de Futebol", "nivel":
                "Iniciante", "vagas": 30, "data": date(2026, 11, 28), "cancelado": True},
            {"nome": "Copa São Bernardo de Futebol", "nivel":
                "Intermediário", "vagas": 20, "data": date(2027, 1, 15), "cancelado": False}
        ],
        "volei": [
            {"nome": "Campeonato Municipal de Vôlei", "nivel":
                "Iniciante", "vagas": 25, "data": date(2026, 8, 30), "cancelado": True},
            {"nome": "Copa São Bernardo de Vôlei", "nivel":
                "Intermediário", "vagas": 20, "data": date(2027, 3, 12), "cancelado": True}
        ]
    }
}


# ==========================================
# 2. VARIÁVEIS GLOBAIS
# ==========================================

# Modalidades e níveis disponíveis para cadastro.
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

# Armazena todos os usuários cadastrados.
inscricoes = []

# Associa cada nível a um valor numérico para comparação.
classificacao = {
    "Iniciante": 1,
    "Intermediário": 2,
    "Avançado": 3
}

# Armazena o usuário que está utilizando o sistema atualmente.
usuario_atual = None


# ==========================================
# 3. CONSULTA DE PARTICIPAÇÃO
# ==========================================


def meus_eventos():
    print("\n--- PARTICIPAÇÃO DE EVENTOS ---\n")

    # Verifica se existe um usuário ativo.
    if usuario_atual is None:
        print("Você não possui usuário cadastrado")
        return

    # Verifica se o usuário possui inscrições.
    if not usuario_atual["eventos"]:
        print("Você não está participando de nenhum evento.")
        return

    # Exibe os eventos em que o usuário está inscrito.
    for evento in usuario_atual["eventos"]:
        print(f"Evento: {evento['nome']}")
        print(f"Nível: {evento['nivel']}")
        print(f"Data: {evento['data'].strftime('%d/%m/%Y')}")
        print(f"Vagas restantes: {evento['vagas']}")

        # Verifica se o evento foi cancelado.
        if evento["cancelado"]:
            print("Situação: CANCELADO")

        # Verifica se o evento já aconteceu.
        elif evento["data"] < date.today():
            print("Situação: ENCERRADO")

        # Verifica se o evento acontece hoje.
        elif evento["data"] == date.today():
            print("Situação: ACONTECE HOJE")

        else:
            print("Situação: CONFIRMADO")

        print("-------------------")


# ==========================================
# 4. INSCRIÇÃO EM EVENTOS
# ==========================================


def inscricao_evento(regiao, mod, usuario_atual):

    # Recupera os eventos da região e modalidade escolhidas.
    lista_eventos = eventos[regiao][mod]

    # Exibe os eventos disponíveis.
    for i, ev in enumerate(lista_eventos, start=1):
        print(f"{i}. {ev['nome']}")

    escolha = input("Digite o número do evento: ").strip()

    # Valida a escolha do usuário.
    if not escolha.isdigit() or not 1 <= int(escolha) <= len(lista_eventos):
        print("Evento inválido")
        return

    # Recupera o evento selecionado.
    evento = lista_eventos[int(escolha) - 1]

    # Verifica se o evento foi cancelado.
    if evento["cancelado"]:
        print("Inscrição indisponível: este evento foi cancelado.")
        return

    # Verifica se a data do evento já passou.
    if evento["data"] < date.today():
        print("Inscrição indisponível: este evento já aconteceu.")
        return

    # Compara o nível do usuário com o nível exigido pelo evento.
    if classificacao[usuario_atual["nivel"]] < classificacao[evento["nivel"]]:
        print("Seu nível é insuficiente para participar desse evento.")
        return

    # Verifica se ainda existem vagas.
    if evento["vagas"] <= 0:
        print("Não há vagas disponíveis.")
        return

    # Impede que o usuário se inscreva duas vezes no mesmo evento.
    if evento in usuario_atual["eventos"]:
        print("Você já está participando desse evento.")
        return

    # Registra a inscrição e atualiza a quantidade de vagas.
    usuario_atual["eventos"].append(evento)
    evento["vagas"] -= 1

    print(f"Inscrição realizada em {evento['nome']}!")


# ==========================================
# 5. CONSULTA DE USUÁRIOS CADASTRADOS
# ==========================================

def consultar_inscricoes(inscricoes):
    print("\n-- INSCRIÇÕES --\n")

    # Verifica se existem usuários cadastrados.
    if not inscricoes:
        print("Nenhum usuário cadastrado.")
        return

    # Percorre e exibe os dados de cada usuário.
    for usuario in inscricoes:
        print(f"Nome: {usuario['nome']}")
        print(f"Email: {usuario['email']}")
        print(f"Telefone: {usuario['telefone']}")
        print(f"Modalidade: {usuario['modalidade']}")
        print(f"Nível: {usuario['nivel']}")
        print("-------------------")


# ==========================================
# 6. VERIFICAÇÃO DE E-MAIL
# ==========================================

def verificar_email(email):

    # Percorre os usuários para identificar e-mails duplicados.
    for usuario in inscricoes:
        if usuario["email"].lower() == email.strip().lower():
            return False

    # Retorna True caso o e-mail esteja disponível.
    return True


# ==========================================
# 7. CADASTRO DE USUÁRIOS
# ==========================================

def cadastro():
    global usuario_atual

    print("Esse é o menu de inscrição para jogar nas equipes da EloEsportes\n")
    print("Digite seus dados cadastrais: ")

    # Recebe os dados pessoais.
    nome = input("\nNome: ")
    email = input("Email: ")

    # Impede o cadastro de e-mails duplicados.
    if not verificar_email(email):
        print("Este email já está cadastrado.")
        return

    telefone = input("Telefone: ").strip()

    # Exibe as modalidades disponíveis.
    print("\nQual sua modalidade de preferência?\n")

    for i, mod in enumerate(modalidades, start=1):
        print(f" {i}. {mod.title()}")

    # Recebe e valida a modalidade escolhida.
    pref = input("\n")

    if pref.isdigit() and 1 <= int(pref) <= len(modalidades):
        pref = modalidades[int(pref) - 1]
    else:
        print("Modalidade inválida")
        return

    # Exibe os níveis disponíveis.
    print("\nQual seu nível nessa modalidade(1 à 3)?\n")

    for i, nivel in enumerate(niveis, start=1):
        print(f"{i}. {nivel.title()}")

    # Recebe e valida o nível do usuário.
    level = input("\n").strip()

    if level.isdigit() and 1 <= int(level) <= len(niveis):
        level = niveis[int(level) - 1]
    else:
        print("Nível inválido.")
        return

    # Cria o dicionário com os dados do novo usuário.
    usuario = {
        "nome": nome.title(),
        "email": email.strip(),
        "telefone": telefone.strip(),
        "modalidade": pref,
        "nivel": level,
        "eventos": []
    }

    # Define o novo usuário como usuário atual e registra o cadastro.
    usuario_atual = usuario
    inscricoes.append(usuario)

    print("\nSEU USUÁRIO FOI CADASTRADO COM SUCESSO!\n")


# ==========================================
# 8. CONSULTA DE EVENTOS
# ==========================================


def consultar_eventos(mod, regiao):

    # Verifica se existe um usuário cadastrado.
    if usuario_atual is None:
        print("Você precisa realizar seu cadastro antes de consultar os eventos.")
        return

    # Verifica se a modalidade escolhida corresponde ao cadastro.
    if usuario_atual["modalidade"] != mod:
        print(f"Você está cadastrado na modalidade {usuario_atual['modalidade'].title()}.")
        return

    # Exibe os eventos disponíveis na região e modalidade.
    if mod in eventos[regiao]:
        for i, ev in enumerate(eventos[regiao][mod], start=1):
            print(f"\n{i}. {ev['nome']}")
            print(f"Nível: {ev['nivel']}")
            print(f"Vagas: {ev['vagas']}")
            print(f"Data: {ev['data'].strftime('%d/%m/%Y')}")

            if ev["cancelado"]:
                print("Situação: CANCELADO")

            elif ev["data"] < date.today():
                print("Situação: ENCERRADO")

            elif ev["data"] == date.today():
                print("Situação: ACONTECE HOJE")

            else:
                print("Situação: ATIVO")

    else:
        print("Modalidade inválida")
        return

    # Pergunta se o usuário deseja realizar uma inscrição.
    part = input("\nGostaria de se inscrever em algum evento (sim ou não)?\n").lower().strip()

    if part == "sim":
        inscricao_evento(regiao, mod, usuario_atual)

    elif part == "não" or part == "nao":
        return

    else:
        print("Resposta inválida.")
        return


# ==========================================
# 9. SELEÇÃO DE MODALIDADE
# ==========================================

def modalidade(regiao):

    # Verifica se a região existe na base de eventos.
    if regiao in eventos:

        # Recupera somente as modalidades disponíveis naquela região.
        lista_modalidades = list(eventos[regiao].keys())

        # Exibe as modalidades disponíveis.
        for i, mod in enumerate(lista_modalidades, start=1):
            print(f" {i}. {mod.title()}")

        escolha = input("\nEscolha uma modalidade: ").strip()

        # Valida a modalidade escolhida e encaminha para a consulta.
        if escolha.isdigit() and 1 <= int(escolha) <= len(lista_modalidades):
            mod = lista_modalidades[int(escolha) - 1]
            consultar_eventos(mod, regiao)
        else:
            print("Modalidade inválida")


# ==========================================
# 10. SELEÇÃO DE REGIÃO
# ==========================================

def regioes():
    print("-- LOCAIS DE EVENTOS --")

    # Exibe as regiões cadastradas.
    for i, regiao in enumerate(eventos, start=1):
        print(f"{i}. {regiao.title()}")

    regiao = input("Escolha uma região(1 à 5): ").strip()

    # Recupera as regiões disponíveis.
    lista_regioes = list(eventos.keys())

    # Valida a escolha e encaminha para a seleção de modalidade.
    if regiao.isdigit() and 1 <= int(regiao) <= len(lista_regioes):
        regiao = lista_regioes[int(regiao) - 1]
        modalidade(regiao)
    else:
        print("Região inválida")


# ==========================================
# 11. MENU PRINCIPAL
# ==========================================

def main():

    # Mantém o sistema em execução até o usuário escolher sair.
    while True:
        print("\n========== ELOESPORTES ==========")
        print("1. Cadastrar participante")
        print("2. Explorar eventos")
        print("3. Minhas inscrições")
        print("4. Consultar Usuário")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        # Direciona o usuário conforme a opção selecionada.
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


# ==========================================
# 12. EXECUÇÃO DO PROGRAMA
# ==========================================

main()
