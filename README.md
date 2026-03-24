🚀 FastAPI Learning Project

API REST desenvolvida com FastAPI para fins de estudo, abordando:

Criação de endpoints
Manipulação de dados em memória
Integração com API externa
Estrutura inicial de backend
🧪 Funcionalidades
📌 Tasks (CRUD simples em memória)
POST /tasks/ → Criar tarefa
GET /tasks → Listar tarefas
PUT /tasks/{task_id} → Marcar tarefa como concluída
🌐 Integração com API externa
GET /external-users
Retorna usuários consumidos da API pública:

👉 https://jsonplaceholder.typicode.com/users

Resposta tratada:

[
  {
    "name": "Leanne Graham",
    "email": "Sincere@april.biz"
  }
]
🚀 Tecnologias utilizadas
Python 3.x
FastAPI
Uvicorn
Requests
⚙️ Como rodar o projeto
1. Clonar o repositório
git clone https://github.com/SEU-USUARIO/SEU-REPO.git
cd SEU-REPO
2. Criar ambiente virtual
python -m venv .venv
3. Ativar ambiente

Windows:

.venv\Scripts\activate
4. Instalar dependências
pip install fastapi uvicorn requests
5. Rodar a API
python -m uvicorn main:app --reload
📄 Documentação automática

Após subir a API, acesse:

👉 http://127.0.0.1:8000/docs

Interface interativa para testar os endpoints.

🧠 Observações
Os dados das tarefas são armazenados em memória
Ao reiniciar o servidor, os dados são perdidos
Projeto com foco educacional
📈 Próximos passos (evolução)
 Separar em camadas (routes, services, schemas)
 Adicionar banco de dados (SQLite/PostgreSQL)
 Implementar validação com Pydantic
 Autenticação com JWT
 Dockerizar aplicação
👨‍💻 Autor

Raimundo Gregório Alencar da Silva

LinkedIn: https://linkedin.com/in/gregorio-alencar-711813110
GitHub: https://github.com/GregorioAlencar