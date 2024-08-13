import pandas as pd
import os
from faker import Faker
from datetime import datetime
import random

fake = Faker(["pt_BR"])

def gerar_email(nome):
    nome_limpo = nome.lower().replace(" ", ".")
    return f"{nome_limpo}@example.com"

def gerar_clientes(num_clientes, start_id):
    clientes = []
    for i in range(start_id, start_id + num_clientes):
        nome = fake.name()
        email = gerar_email(nome)
        cliente = {
            'ClienteID': i,
            'Nome': nome,
            'Email': email,
            'DataCadastro': fake.date()
        }
        clientes.append(cliente)
    return clientes

def gerar_produtos(num_produtos, start_id):
    produtos = []
    for i in range(start_id, start_id + num_produtos):
        produto = {
            'ProdutoID': i,
            'Nome': fake.word(),
            'Categoria': fake.word(),
            'Preco': round(random.uniform(50, 500), 2)
        }
        produtos.append(produto)
    return produtos

def gerar_pedidos(num_pedidos, num_clientes, num_produtos):
    return [{'PedidoID': i, 'ClienteID': random.randint(0, num_clientes - 1), 'ProdutoID': random.randint(0, num_produtos - 1), 'Quantidade': random.randint(1, 5), 'DataPedido': fake.date()} for i in range(num_pedidos)]

# Configurações
num_novos_clientes = random.randint(1, 20)
num_novos_produtos = random.randint(1, 4)

# Caminhos dos arquivos
arquivo_clientes = '/home/sergio/dev/suslake/clientes_ficticios.csv'
arquivo_produtos = '/home/sergio/dev/suslake/produtos_ficticios.csv'


# Verificar e carregar dados existentes
if os.path.exists(arquivo_clientes):
    df_clientes_existente = pd.read_csv(arquivo_clientes)
    ultimo_id_cliente = df_clientes_existente['ClienteID'].max() + 1
else:
    df_clientes_existente = pd.DataFrame()
    ultimo_id_cliente = 0

if os.path.exists(arquivo_produtos):
    df_produtos_existente = pd.read_csv(arquivo_produtos)
    ultimo_id_produto = df_produtos_existente['ProdutoID'].max() + 1
else:
    df_produtos_existente = pd.DataFrame()
    ultimo_id_produto = 0

# Gerar dados
novos_clientes = gerar_clientes(num_novos_clientes, ultimo_id_cliente)
novos_produtos = gerar_produtos(num_novos_produtos, ultimo_id_produto)

# Criar DataFrames
df_novos_clientes = pd.DataFrame(novos_clientes)
df_novos_produtos = pd.DataFrame(novos_produtos)
df_clientes_atualizado = pd.concat([df_clientes_existente, df_novos_clientes], ignore_index=True)
df_produtos_atualizado = pd.concat([df_produtos_existente, df_novos_produtos], ignore_index=True)

# Salvar em arquivos CSV
df_clientes_atualizado.to_csv(arquivo_clientes, index=False)
df_produtos_atualizado.to_csv(arquivo_produtos, index=False)

print(f"Dados fictícios gerados e salvos as {datetime.now()}")
print(f"Numero de clientes antes: {ultimo_id_cliente}")
print(f"Numero de produtos antes: {ultimo_id_produto}")
print(f"Novos clientes: {len(novos_clientes)}")
print(f"Novos produtos: {len(novos_produtos)}")
print(f"Novo numero de clientes: {len(df_clientes_atualizado)}")
