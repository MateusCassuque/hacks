import pypdf

arquivo = open('Fomulário Digital SME.pdf', 'rb')
leitor = pypdf.PdfReader(arquivo)
paginas = len(leitor.pages)
pagina = leitor.pages[0]

texto = pagina.extract_text()
print(texto)
