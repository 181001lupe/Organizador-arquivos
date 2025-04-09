cat << EOF > README.md
# 🗂️ Organizador de Arquivos

Organize automaticamente os arquivos de uma pasta, separando por categorias como **Imagens**, **Vídeos**, **Documentos** e **Outros**. Feito com Python, simples de usar e muito útil no dia a dia!

![Badge Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python) ![Badge Projeto](https://img.shields.io/badge/Projeto-Concluído-green?style=for-the-badge) ![Badge Status](https://img.shields.io/badge/Organização-Automática-orange?style=for-the-badge)

## ✨ Funcionalidades

- 🔍 Lê todos os arquivos de uma pasta
- 📁 Cria subpastas por tipo de arquivo (imagem, vídeo, etc.)
- 🚚 Move os arquivos automaticamente para a pasta correta
- ⚠️ Exibe mensagens de erro amigáveis se algo der errado

## 📸 Exemplo

Antes:
\`\`\`
📂 pasta/
├── foto.jpg
├── video.mp4
├── documento.pdf
├── arquivo.exe
\`\`\`

Depois:
\`\`\`
📂 pasta/
├── Imagens/
│   └── foto.jpg
├── Vídeos/
│   └── video.mp4
├── Documentos/
│   └── documento.pdf
├── Outros/
│   └── arquivo.exe
\`\`\`

## 🚀 Como usar

1. Clone este repositório:
   \`\`\`bash
   git clone https://github.com/181001lupe/Organizador-arquivos.git
   \`\`\`

2. Navegue até a pasta do projeto:
   \`\`\`bash
   cd Organizador-arquivos
   \`\`\`

3. Execute o script principal:
   \`\`\`bash
   python main.py
   \`\`\`

> 📌 Por padrão, o script organiza os arquivos de um diretório que você define diretamente no código.

---

## 🧠 Aprendizados

Durante o desenvolvimento, foram aplicados conceitos de:

- Manipulação de arquivos e diretórios com \`os\` e \`shutil\`
- Estruturação de funções reutilizáveis
- Tratamento de exceções e validação de entradas
- Boas práticas de organização de código
- Uso do Git e GitHub para versionamento

## 🧪 Testes

O script inclui mensagens no terminal que confirmam cada etapa: listagem, organização e movimentação dos arquivos.

> Você pode fazer testes alterando a pasta de origem para verificar diferentes comportamentos.

## 👨‍💻 Autor

Feito por [Saulo Duarte](https://github.com/181001lupe)

---

