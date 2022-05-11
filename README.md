# Entrega - Kanvas

<p>
Uma API que tem a finalidade de cadastrar cursos em uma plataforma, criar usuários, promover usuários para instrutores, vincular intrutores para cursos e cadastrar alunos em cursos já criados.
</p>

## Ferramentas utilizadas
<ul>
<li>Python3</li>
<li>Django</li>
<li>Django Rest Framework</li>
<li>SQlite3</li>
</ul>

## Funcionalidades

<ul>
  <li>Registro de usuários.</li>
  <li>Registro de cursos, assim como editar e deletar.</li>
  <li>Provover usuário para instrutor.</li>
  <li>Registrar usuário em um curso.</li>
</ul>

# Endpoints base

http://127.0.0.1:8000/ ou http://localhost:8000/

# Dicas de Uso e Endpoints

<p>A API conta com 3 tipo de acesso:</p>

<ul>
  <li>Rotas Livres</li>
  <li>Rotas Estudante</li>
  <li>Rotas Instrutor</li>
</ul>

<p>As Rotas Livre é possivel se registrar, logar, verificar cursos </br>
ja os com permissões de usuario poderá adcionar endereço a suas informações</br>
E os instrutores poderão criar curso, adcionar instrutor no curso, adcionas estudantes nos cursos editar e aparar qualquer informações em geral na aplicação


# Alguns exemplos de uso das Rotas
## Rotas

- students
- address
- courses

## Students rotas

### POST/api/accounts/

#### Descrição

```
    - Rota livre
    - Registra um novo usuráio
```

_Envio:_

```json
{
  "email": "example@gmail.com",
  "password": "1234",
  "first_name": "example",
  "last_name": "stud",
  "is_admin": false
}
```

_Resposta:_

```json
{
  "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
  "is_admin": false,
  "email": "example@gmail.com",
  "first_name": "example",
  "last_name": "stud"
}
```

### GET/api/accounts/

#### Descrição

```
    - Rota de Instrutor
    - Retorna uma lista com todos usuários cadastrados
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
[
  {
    "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
    "is_admin": false,
    "email": "example@gmail.com",
    "first_name": "example",
    "last_name": "stud"
  },
  {
    "uuid": "07e99feb-4a82-4fc7-9918-7c13db26fafc",
    "is_admin": true,
    "email": "example@adm.com",
    "first_name": "exampleadm",
    "last_name": "stud"
  }
]
```

### POST/api/login/

#### Descrição

```
    - Rota livre
    - Loga um usuário
```

_Envio:_

```json
{
  "email": "example@gmail.com",
  "password": "1234"
}
```

_Resposta:_

```json
{
  "token": "23ce984479c4d4e64fa4d45e6b623fef33fb630b"
}
```

## Address

### PUT/api/address/

#### Descrição

```
    - Registra um endereço á um usuário
```

_Envio:_

```json
{
  "zip_code": "123456789",
  "street": "Rua das Flores",
  "house_number": "123",
  "city": "Teresina",
  "state": "Piaui",
  "country": "Brasil"
}
```

_Resposta:_

```json
{
  "uuid": "3b573ca6-9bd4-4051-bf0f-3ff526ffc237",
  "street": "Rua das Flores",
  "house_number": 123,
  "city": "Teresina",
  "state": "Piaui",
  "zip_code": "123456789",
  "country": "Brasil",
  "users": [
    {
      "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
      "is_admin": false,
      "email": "example@gmail.com",
      "first_name": "example",
      "last_name": "stud"
    }
  ]
}
```

## Courses

### POST/api/courses/

#### Descrição

```
    - Rota de Instrutor
    - Registra um curso
```

_Envio:_

```json
{
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git"
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### GET/api/courses/

#### Descrição

```
    - Rota de Instrutor
    - Retorna a lista de todos os cursos
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
[
  {
    "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
    "name": "Django",
    "demo_time": "9:00",
    "link_repo": "http://django.ts.com/git",
    "instructor": null,
    "students": []
  }
]
```

### GET/api/courses/<course_id>/

#### Descrição

```
    - Rota de Instrutor
    - Retorna o curso correspondente
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### PATCH/api/courses/<course_id>/

#### Descrição

```
    - Rota de Instrutor
    - Altera um ou mais campos do curso
```

_Envio:_

```json
{
  "demo_time": "10:00"
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "10:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": null,
  "students": []
}
```

### PUT/api/courses/<course_id>/registrations/instructor/

#### Descrição

```
    - Rota de Instrutor
    - Registra um intrutor ao curso
```

_Envio:_

```json
{
  "instructor_id": "07e99feb-4a82-4fc7-9918-7c13db26fafc"
}
```

_Resposta:_

```json
{
  "uuid": "1f756e0c-b9e6-41ff-8126-11cf7213b5de",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": {
    "uuid": "d170ac51-f9fc-4f32-89eb-c72d6b3aaeeb",
    "is_admin": true,
    "email": "example@adm.com",
    "first_name": "exampleadm",
    "last_name": "stud"
  },
  "students": []
}
```

### PUT/api/courses/<course_id>/registrations/students/

#### Descrição

```
    - Rota de Instrutor
    - Registra alunos ao curso
```

_Envio:_

```json
{
  "students_id": [
    "97f62170-a9a5-411b-b2ba-d409608fc288",
    "907f6fe1-56c1-4043-beb7-0c8b56cb68b6"
  ]
}
```

_Resposta:_

```json
{
  "uuid": "7a8bcf53-4d1b-4a4b-af9e-c8838ef2d567",
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "http://django.ts.com/git",
  "instructor": {
    "uuid": "07e99feb-4a82-4fc7-9918-7c13db26fafc",
    "is_admin": true,
    "email": "exmaple@adm.com",
    "first_name": "exampleadm",
    "last_name": "stud"
  },
  "students": [
    {
      "uuid": "97f62170-a9a5-411b-b2ba-d409608fc288",
      "is_admin": false,
      "email": "example@gmail.com",
      "first_name": "exmaple",
      "last_name": "stud"
    },
    {
      "uuid": "907f6fe1-56c1-4043-beb7-0c8b56cb68b6",
      "is_admin": false,
      "email": "example2@gmail.com",
      "first_name": "example2",
      "last_name": "stud"
    }
  ]
}
```

### DELETE/api/courses/<course_id>/

#### Descrição

```
    - Rota de Instrutor
    - Deleta um curso registrado
```

_Envio:_

```json
nobody
```

_Resposta:_

```json
nocontent
```

### Diagrama de Relacionamento

<img src="https://i.imgur.com/2SfGBO0.png"/>

# Relatório de testes 

Todas as atividades do trimestre possuem requisitos mínimos obrigatórios:


<header>**Importante!**</header>

O **formato dos JSONs** de todas as requisições e respostas deve coincidir com os formatos especificados nos enunciados.

As **URLs** definidas devem ser as mesmas especificadas.

Os **códigos de status HTTP** também devem ser iguais aos definidos para as atividades.

</section>

Para auxiliar na checagem desses requisitos e verificar se tudo está de acordo com essas três regras, serão disponibilizados arquivos de testes para cada atividade. Esses arquivos terão o objetivo de garantir que os requisitos mínimos obrigatórios estão sendo atendidos em seu projeto, além de auxiliar a equipe de ensino durante a correção das atividades.

Cada atividade terá um link para seu respectivo arquivo de testes. Basta adicioná-lo à raiz do seu projeto e rodar o seguinte comando:

    python manage.py test -v 2 &> report.txt

O comando executará os testes e adicionará a saída da execução num arquivo chamado `report.txt`. Esse arquivo conterá um relatório dos testes executados e seus respectivos resultados. Caso ele aponte falhas, significa que os requisitos mínimos não estão sendo totalmente cumpridos em seu projeto. Se isso acontecer, o relatório indicará o erro encontrado e apontará o que precisa ser corrigido. Você pode gerar o relatório quantas vezes achar necessário. Apenas a versão final deve ser enviada junto com os demais arquivos do projeto.

## Utilizando banco Postgres

Existe um problema quando rodamos os testes em um banco Postgres, porque ele não reseta os IDs por padrão. Para o caso dos nossos testes, isso é uma pequena dor de cabeça.

Sendo assim, caso você queira utilizar um banco Postgres em seu projeto, será necessário incluir a configuração do SQLite apenas para rodar os testes.

    # settings.py

    import os

    ...

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': <nome-do-seu-banco>,
            'USER': <nome-do-user>,
            'PASSWORD': <senha-do-user>,
            'HOST': <db-hostname-ou-ip>, # Por estar configurado localmente vai ser no localhost ou 127.0.0.1
            'PORT': <porta-do-banco> # Por padrão o PostgreSQL roda na porta 5432
        }
    }

    test = os.environ.get('TEST')

    if test:    
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }

No momento de executar, é necessário incluir a variável `TEST` antes do comando.

    TEST=TEST python manage.py test -v 2 &> report.txt
