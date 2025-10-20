# Função para cadastrar notas
def cadastrar_notas():
    notas = []
    while True:
        nota = input("Digite a nota do aluno (ou 'sair' para finalizar): ")
        if nota.lower() == 'sair':
            break
        try:
            nota = float(nota)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida! Digite entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")
    return notas

# Função para calcular a média
def calcular_media(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para determinar situação
def determinar_situacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

# Função para gerar relatório final
def gerar_relatorio(notas, media, situacao):
    print("\n=== RELATÓRIO FINAL ===")
    print("Notas do aluno:", notas)
    print(f"Média: {media:.2f}")
    print("Situação:", situacao)

# Programa principal
if __name__ == "__main__":
    notas_aluno = cadastrar_notas()
    media_aluno = calcular_media(notas_aluno)
    situacao_aluno = determinar_situacao(media_aluno)
    gerar_relatorio(notas_aluno, media_aluno, situacao_aluno)
