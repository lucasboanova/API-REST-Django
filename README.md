# Django REST Framework API

## Visão Geral

Este projeto é uma API construída com Django e Django REST Framework que gerencia matrículas de alunos em cursos. Ele permite listar as matrículas de alunos em um curso específico.

## Estrutura do Projeto

O projeto é organizado da seguinte maneira:

- **models.py**: Contém os modelos `Aluno`, `Curso` e `Matricula`.
- **serializers.py**: Define os serializers para transformar os dados do modelo em JSON.
- **views.py**: Contém as views que manipulam as requisições HTTP.
- **urls.py**: Define as rotas da API.

## Modelos

### Aluno
Representa um aluno com os seguintes campos:
- `nome`: Nome do aluno.
- `cpf`: cpf do aluno 
- `rg`: Rg do aluno.
- `data_nascimento`: Data de nascimento do aluno.
### Curso
Representa um curso com os seguintes campos:
- `nome`: Nome do curso.
- `cod_curso`: Código do curso.
- `periodo`: Periodo do curso (Matutino, vespertino, Noturno)

### Matricula
Representa a matrícula de um aluno em um curso com os seguintes campos:
- `aluno`: Chave estrangeira para o modelo `Aluno`.
- `curso`: Chave estrangeira para o modelo `Curso`.
- `periodo`: Período da matrícula (CharField).

## Serializers

### ListaAlunosMatriculadosSerializer
Um serializer que transforma os dados de uma matrícula em JSON e inclui o nome do aluno:
```python
from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']
```

## Views

### ListaAlunosMatriculadosView
Uma view que retorna a lista de alunos matriculados em um curso específico:
```python
from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.selializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
```

## URLs

As URLs são definidas em `urls.py` para mapear as rotas da API:
```python
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculasViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculasViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view())
]
```

## Como Executar

### Pré-requisitos
- Python 3.x
- Django
- Django REST Framework

### Passos para Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd seu-repositorio
   ```
3. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
5. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
6. Execute as migrações:
   ```bash
   python manage.py migrate
   ```
7. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

### Testando a API
Você pode testar a API utilizando um cliente HTTP como o Postman ou o curl.

- **Endpoint**: `GET /curso/<curso_id>/matriculas/`
- **Descrição**: Retorna a lista de alunos matriculados no curso especificado.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

Este README fornece uma visão geral do projeto, incluindo sua estrutura, modelos, serializers, views, URLs e instruções sobre como executar o projeto. Ajuste conforme necessário para se adequar às especificidades do seu projeto.
