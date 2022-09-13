from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status

class CursosTestCase(APITestCase):

    def setUp (self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(codigo_curso='CTT1', descricao='Curso teste 1', nivel='B')

    def test_requisicao_get(self):
        '''teste de requisição GET'''
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requicao_post(self):
        data = {
            'codigo_curso': 'CTT2',
            'descricao': 'Curso teste',
            'nivel': 'A'
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
