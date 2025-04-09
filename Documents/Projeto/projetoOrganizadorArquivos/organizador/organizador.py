import os

def listarArquivos(pasta):
    """
        Lista todos os arquivos (não pastas) dentro de um diretório especificado.

        Parâmetros:
            pasta (str): Caminho da pasta onde os arquivos serão buscados.

        Retorna:
            list: Lista contendo os caminhos completos dos arquivos encontrados.

        Observações:
            - Se a pasta não existir, uma mensagem será exibida e uma lista vazia será retornada.
            - Se a pasta estiver vazia, também será exibida uma mensagem.
        """
    lista = []
    if not os.path.exists(pasta):
        print(f'A pasta "{pasta}" não existe')
        return []
    try:
        itens = os.listdir(pasta)
        for item in itens:
            arq = os.path.join(pasta, item)
            if os.path.isfile(arq):
                lista.append(arq)
        if not lista:
            print('A pasta existe, mas não contém arquivos.')
        return lista
    except Exception as e:
        print(f'Erro ao listar os arquivos: {e}')
        return []

def organizarArquivos(arquivos):
    """
    Classifica arquivos em categorias com base em suas extensões.

    Parâmetros:
        arquivos (list): Lista de caminhos completos dos arquivos a serem categorizados.

    Retorna:
        dict: Dicionário contendo listas de arquivos organizados por categoria:
              'Imagens', 'Vídeos', 'Documentos' e 'Outros'.

    Observações:
        - As extensões conhecidas são agrupadas nas três categorias principais.
        - Arquivos com extensões não reconhecidas são adicionados à categoria 'Outros'.
        - A categorização não diferencia letras maiúsculas/minúsculas nas extensões.
    """
    geral = {
        'Imagens': ['.jpg', '.png', '.jpeg', '.gif'],
        'Vídeos': ['.mp4', '.mov'],
        'Documentos': ['.pdf', '.docx', '.txt']
    }
    final = {
        'Imagens': [],
        'Vídeos': [],
        'Documentos': [],
        'Outros': []
    }
    for arquivo in arquivos:
        nome, extensao = os.path.splitext(arquivo)
        encontrou = False
        for categorias, lista_extensoes in geral.items():
            if extensao in lista_extensoes:
                final[categorias].append(arquivo)
                encontrou = True
                break
        if not encontrou:
            final['Outros'].append(arquivo)
    return final

def criaPastas(pasta, categorizados):
    """
        Cria subpastas dentro de uma pasta principal com base nas categorias fornecidas.

        Parâmetros:
            pasta (str): Caminho da pasta principal onde as subpastas serão criadas.
            categorizados (dict): Dicionário contendo as categorias como chaves (ex: 'Imagens', 'Documentos').

        Observações:
            - Se a subpasta já existir, nada é sobrescrito (comportamento controlado por exist_ok=True).
            - Cada chave do dicionário gera uma subpasta com o mesmo nome.
        """
    for categorias in categorizados:
        caminho = os.path.join(pasta, categorias)
        os.makedirs(caminho, exist_ok=True)
    print(f"📁 Pasta criada: {caminho}")


def moverArquivo(pasta, categorizados):
    """
       Move os arquivos para suas respectivas subpastas, com base nas categorias.

       Parâmetros:
           pasta (str): Caminho da pasta principal onde os arquivos estão localizados.
           categorizados (dict): Dicionário com os arquivos organizados por categoria.

       Observações:
           - Cada arquivo é movido da pasta principal para a subpasta correspondente à sua categoria.
           - Se ocorrer um erro ao mover um arquivo (como ausência ou permissão negada), uma mensagem será exibida.
           - Utiliza shutil.move para garantir que o arquivo seja de fato transferido.
       """
    import shutil
    erros = False
    for categoria, arquivos in categorizados.items():
        for arquivo in arquivos:
            origem = arquivo
            destino = os.path.join(pasta, categoria, os.path.basename(arquivo))
            try:
                print(f"➡️ Movendo {os.path.basename(arquivo)} para {categoria}")
                shutil.move(origem, destino)
            except Exception as e:
                print(f'Erro ao mover {arquivo}: {e}')
                erros = True
    if not erros:
        print('Deu tudo certo! Arquivos movidos e organizados por subpastas.')


