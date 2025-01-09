contatos = ( 
    ('Godoy', '3457-4133'),
    ('leticia', '3457-4123'),
    ('sidiney', '3457-4163')
)
telefone_godoy = contatos[0][1]
print(telefone_godoy)
for nome, telefone in contatos:
    if nome == 'Godoy':
        print(telefone)