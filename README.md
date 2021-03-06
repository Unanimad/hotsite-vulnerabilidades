[![N|Solid](http://www.ifs.edu.br/comunicacao/images/Imagens/Marcas/IFS_puro/IFS---horizontal-01.png)](http://www.ifs.edu.br/)
# Vulnerabilidades

## Sobre
O HotSite fornece informações sobre as inseguranças descobertas, no âmbito de TI, que podem afetar as atividades exercidas bem como as informações trafegadas na rede. No HotSite as pessoas poderão verificar qual a falha foi detectadas e como solucionar, além de exibir também notícias sobre segurança da informação.

## Dependências
### Projeto
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Git](https://github.com/) | 2.14.1 | Controle de versão
| [Python](https://www.python.org/) | 3.6+ | Linguagem
| [Mysql](https://www.mysql.com/) | 5.7.19 | Banco de dados
| [Node.js](https://nodejs.org/) | v6+ | Gerenciamento das depências do Frontend
| [Virtualenv](https://virtualenv.pypa.io/) | 15.1.0 | Gerenciamento das dependências do Python
| [Supervisor](http://supervisord.org/) | 3.3.3 | Controle dos processos
| [Nginx](https://nginx.org/en/) | 1.12.1 | Servidor Web

### Backend
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [Django](https://www.djangoproject.com/) | 1.11.4 | Framework
| [Mysqlclient](https://pypi.python.org/pypi/mysqlclient/1.3.10) | 1.3.10 | Plugin de conexão com o banco de dados
| [Pillow](https://pillow.readthedocs.io/en/4.2.x/) | 4.2.1 | Biblioteca de Imagens
| [Gunicorn](http://gunicorn.org/) | 19.7.1 | Gateway de comunicação entre o servidor e a aplicação disponibilizada no servidor Web

### Frontend 
| Programa | Versão | Sobre |
| ----- | ----- | ----- |
| [bootstrap](getbootstrap.com/) | 4.0.0-beta.2 | Biblioteca do frontend
| [popper.js](https://popper.js.org/) | 1.12.5 |  Biblioteca para gerenciar elementos Popper
| [datatables.net](https://datatables.net) | 1.10.16 | Customização das tabelas e seus dados
| [datatables.net-bs](https://datatables.net) | 1.10.16 | Link do datatables com o bootstrap
| [font-awesome](http://fontawesome.io/) | 4.7.0 | Icones em fontes
| [jquery](https://jquery.com/) | 3.2.1 | Biblioteca JavaScript
| [pace-js](github.hubspot.com/pace/docs/welcome/) | 1.0.2 | Progeresso do carregamento
| [select2](https://select2.github.io/) | 4.0.4 | Customização do selectbox com suporte a busca
| [tether](tether.io/) | 1.4.0 | Posicionamento dos elementos na tela
| [toastr](https://github.com/CodeSeven/toastr) | 2.1.2 | Notificações

## Preparação
Clone o repositório

```
$ git clone https://unanimad@bitbucket.org/unanimad/ifs-vulnerabilidades.git
```
Acesse o diretório do repositório e altere para a branch **dev**
```
$ git pull origin dev
```

Crie um ambiente python virtual utilizando o **python3** como versão
```
$ virtualenv -p python3 venv
```

Ative o ambiente virtual
```
$ source venv/bin/activate
```

Instale as dependências da aplicação
```
$ pip install -r req.txt
```

Instale as dependências do frontend, não esqueça de ir até o diretório do arquivo `package.json` para executar seguinte comando
```
$ npm install
```

Colete os arquivos estáticos para o diretório relacionado
```
$ python manage.py collectstatic
```

Configure o banco de dados no arquivo `settings.py`, localizando a variável `DATABASES`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}
```

Faça as migrações
```
$ python manage.py migrate 
```

Execute a aplicação para testar com o seguinte comando
```
$ python manage.py runserver
```