# Image → MIDI

### Requisitos
- **Python 3**
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) instalado no sistema (dependência obrigatória para a análise de imagem).

### Guia Rápido de Instalação e Execução

1. Abre o terminal e acede à pasta do projeto:
   ```bash
   cd /caminho/para/ODM_2
   ```

2. Cria e inicia um ambiente virtual isolado
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Instala as dependências Python:
   ```bash
   pip install flask pytesseract pillow
   ```

4. Executa o servidor:
   ```bash
   python3 app.py
   ```

5. O projeto ficará disponível no link: **http://127.0.0.1:5001**
