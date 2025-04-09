from organizador.organizador import listarArquivos, organizarArquivos, criaPastas, moverArquivo
arquivos = listarArquivos(r'C:\Users\Saulo\Desktop\teste')
print(arquivos)
categorizados = organizarArquivos(arquivos)
criaPastas(r'C:\Users\Saulo\Desktop\fotos', categorizados)
moverArquivo(r'C:\Users\Saulo\Desktop\fotos', categorizados)
