usuarios = []

def criar_usuario(nome, email, senha, cpf):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return "cpf ja cadastrado"
        if usuario['email'] == email:
            return 'email ja cadastrado'
       
    usuario ={
        "nome":nome,
        "email":email,
        "senha": senha,
        "cpf": cpf
    }

    usuarios.append(usuario)
    return "sucesso"


def listar_todos_usuarios():
    if not usuarios:
        return 'nenhum usuario cadastrado'
    return usuarios 

    
def listar_apenas_um(cpf):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return 'usuario nao encontrado'
    
def deletar_usuario(cpf):
    for i, usuario in enumerate(usuarios):
        if usuario['cpf'] == cpf:
            del usuarios[i]
            return('usuario deletado')
    return('usuario nao encontrado')