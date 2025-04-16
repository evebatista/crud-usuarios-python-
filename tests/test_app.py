import unittest
from src.app import criar_usuario, listar_todos_usuarios, listar_apenas_um, deletar_usuario, usuarios

class TestApp(unittest.TestCase):

    def setUp(self):
        usuarios.clear()  # limpa a lista antes de cada teste

    def test_criar_usuario_sucesso(self):
        resultado = criar_usuario('joao', 'j@gmail.com', '123456', '555')
        self.assertEqual(resultado, 'sucesso')

    def test_criar_usuario_cpf_duplicado(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        resultado = criar_usuario('Outro', 'novo@gmail.com', 'abcd', '555')
        self.assertEqual(resultado, 'cpf ja cadastrado')

    def test_criar_usuario_email_duplicado(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        resultado = criar_usuario('Outro', 'j@gmail.com', 'abcd', '999')
        self.assertEqual(resultado, 'email ja cadastrado')

    def test_listar_todos_usuarios(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        criar_usuario('maria', 'm@gmail.com','654321', '444')
        resultado = listar_todos_usuarios()
        self.assertEqual(len(resultado), 2)

    def test_listar_todos_usuarios_vazio(self):
        resultado = listar_todos_usuarios()
        self.assertEqual(resultado, "nenhum usuario cadastrado")

    def test_listar_apenas_um_existente(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        resultado = listar_apenas_um("555")
        self.assertIsInstance(resultado, dict)
        self.assertEqual(resultado['nome'], "joao")

    def test_listar_apenas_um_inexistente(self):
        resultado = listar_apenas_um("999")
        self.assertEqual(resultado, "usuario nao encontrado")

    def test_deletar_usuario_existente(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        resultado = deletar_usuario('555')
        self.assertEqual(resultado, "usuario deletado")
        self.assertEqual(len(usuarios), 0)

    def test_deletar_usuario_inexistente(self):
        criar_usuario('joao', 'j@gmail.com', '123456', '555')
        resultado = deletar_usuario("999")
        self.assertEqual(resultado, "usuario nao encontrado")
        self.assertEqual(len(usuarios), 1)

if __name__ == "__main__":
    unittest.main()
