import pypdf

arquivo = open('hoje22-08-2024.pdf', 'rb')
leitor = pypdf.PdfReader(arquivo)
paginas = len(leitor.pages)
pagina = leitor.pages[0]

texto = pagina.extract_text()
print(texto)
