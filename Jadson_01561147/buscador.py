def achar_palavra(texto, palavra):
    if palavra.lower() in texto.lower():
        return f'A palavra "{palavra}" foi encontrada no texto.'
    else:
        return f'A palavra "{palavra}" não foi encontrada no texto.'

exemplo = "olá jadson, você gosta de programação?."
buscador_de_palavra = "lucas"

resultado = achar_palavra(exemplo,buscador_de_palavra)
print(resultado)
