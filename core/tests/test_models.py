import uuid
from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self):
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        file = get_file_path(None, 'teste.png')
        self.assertTrue(len(file), len(self.filename))


class ServicoTestCase(TestCase):
    def setUp(self):
        self.servico = mommy.make('Servico')

    def test_str(self):
        self.assertEquals(str(self.servico), self.servico.servico)


class CargoTestCase(TestCase):
    def setUp(self):
        self.cargo = mommy.make('Cargo')

    def test_str(self):
        self.assertEquals(str(self.cargo), self.cargo.cargo)


class ClienteTestCase(TestCase):
    def setUp(self):
        self.cliente = mommy.make('Cliente')

    def test_str(self):
        self.assertEquals(str(self.cliente), self.cliente.nome)


class ComentarioTestCase(TestCase):
    def setUp(self):
        self.comentario = mommy.make('Comentario')

    def test_str(self):
        self.assertEquals(str(self.comentario), self.comentario.comentario)


class FuncionarioTestCase(TestCase):
    def setUp(self):
        self.funcionario = mommy.make('Funcionario')

    def test_str(self):
        self.assertEquals(str(self.funcionario), self.funcionario.nome)


class RecursoTestCase(TestCase):
    def setUp(self):
        self.recurso = mommy.make('Recurso')

    def test_str(self):
        self.assertEquals(str(self.recurso), self.recurso.nome)
