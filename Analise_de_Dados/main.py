# Passo 1 - Importar as bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import os

# Passo 2 - Carregar as entradas de dados
input_1 = pd.read_excel('input_1 6.xlsx')
input_2 = pd.read_excel('input_2 6.xlsx')

# Passo 3 - juntar as duas entradas em um data frame
df_base = pd.merge(input_1, input_2, how='outer')

# Passo 4 - Criar a coluna de qualidade, ja realizando o calculo para cada célula
df_base['Quality'] = ((df_base['Contador 1'] + df_base['Contador 2']) / df_base['Contador 3']) * 100

# Passo 5 - Varre o data frame base verificando se a coluna qualidade é maior que 70 e adicionando na coluna Status 'OK' e 'NOK'
for i in df_base.index:
    if df_base.at[i,'Quality'] >= 70:
        df_base.at[i, 'Status'] = 'OK'
    else: 
        df_base.at[i, 'Status'] = 'NOK'

# Passo 6 - Criar uma condição para inserir o nome do site via terminal
while True:
    site_name = input('Digite o nome do(s) sites selecionados separados por "," ou "todos": ')

    if site_name == 'todos':
        df_filtrado = df_base[['Site', 'Cell', 'Date', 'Quality', 'Status']].copy()
        break
    else:
        site = [i.strip() for i in site_name.split(',')]
        df_filtrado = df_base[df_base['Site'].isin(site)]
        if df_filtrado.empty:
            print('Site não encontrado" Tente novamente.')
        else:
            df_filtrado.drop(columns=['Contador 1', 'Contador 2', 'Contador 3'], inplace=True)
            break
    
# Passo 7 - Transformar o data frame criado em um arquivo excel
os.makedirs("relatorios", exist_ok=True)
df_filtrado.sort_values(by='Date')
df_filtrado.to_excel('relatorios/relatório_qualidade.xlsx')

# Passo 8 - Criar um grafico para cada célula do site selecionado
os.makedirs("graficos", exist_ok=True)

for site in df_filtrado['Site'].unique():
    dados_site = df_filtrado[df_filtrado['Site'] == site]
    plt.figure()

    for cell in dados_site['Cell'].unique():    
        dados_cell = dados_site[dados_site['Cell'] == cell]
        eixo_x = dados_cell['Date']
        eixo_y = dados_cell['Quality']
        plt.plot(eixo_x, eixo_y, label=cell, marker='o')

    plt.axhline(70, color='red', linestyle='--', label='Limite 70%')

    plt.title(f'Qualidade do Sinal - {site}')
    plt.xlabel('Data')
    plt.ylabel('Qualidade (%)')
    plt.legend()
    plt.savefig('graficos/grafico_qualidade-{site}.png')

plt.show()