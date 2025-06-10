# Códigos dos candidatos para votação e seus nomes
candidatos = {
    1: "Jair Bolsonaro",
    2: "Lula da Silva",
    3: "Michel Temer",
    4: "Dilma Rousseff"
}

# Variáveis para contagem dos votos
votos_candidatos = {1: 0, 2: 0, 3: 0, 4: 0}  # Contagem de votos por candidato
nulos = 0  # Contagem de votos nulos
branco = 0  # Contagem de votos em branco

print("\nCANDIDATOS:\n")
# Imprime os candidatos na tela
print("1 - Jair Bolsonaro")
print("2 - Lula da Silva")
print("3 - Michel Temer")
print("4 - Dilma Rousseff")
print(" ")

# Imprime outras opções na tela
print("5 - VOTO NULO")
print("6 - VOTO EM BRANCO")
print("0 - Encerrar Votação")
print("\n")

# Votação em loop infinito com while
# O break interrompe o loop
while True:
    voto = int(input("CODIGO DO CANDIDATO: "))

    # Verifica se o codigo é válido, e soma o voto na variavel
    if voto in candidatos:
        print(f"{candidatos[voto]}\n")  # Imprime o candidato que foi votado
        votos_candidatos[voto] += 1  # Soma o voto

    elif voto == 5:  # Voto nulo
        print("VOTO NULO\n")
        nulos += 1  # Soma o voto

    elif voto == 6:  # Voto em branco
        print("VOTO EM BRANCO\n")
        branco += 1  # Soma o voto

    elif voto == 0:  # Encerra a votação
        print("\n\n#######################################################")
        print("###########   F I M   D A   V O T A C A O   ###########")
        print("#######################################################")
        break  # Encerra o loop

    else:  # Diz que o voto é inválido
        print("\nCANDIDATO NAO ENCONTRADO\n")
        print("Por favor, tente novamente!\n")

total_votos = sum(votos_candidatos.values())
perct_nulos = (nulos / total_votos) * 100
perct_brancos = (branco / total_votos) * 100

# Imprime os resultados
print("\n\n")
print("#######################################################")
print("######## R E S U L T A D O  D A  V O T A Ç A O ########")
print("#######################################################\n")

for candidato, votos in votos_candidatos.items():  # Integra sobre os candidatos e seus votos
    # Imprime o candidato e seus votos
    print(f" - {candidatos[candidato]}: {votos}\n")

# Imprime os votos nulos
print(f"* Votos nulos: {nulos}, refere-se a {perct_nulos:.1f}% dos votos")
# Imprime os votos em branco.
print(
    f"* Votos em branco: {branco}, refere-se a {perct_brancos:.1f}% dos votos\n\n")

print(
    f"O PRESIDENTE DA REPUBLICA É: {candidatos[max(votos_candidatos, key = votos_candidatos.get)]}\n")

print("#######################################################\n")
