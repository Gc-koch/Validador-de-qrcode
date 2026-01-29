# 🔍 Validador de QR Codes - OneDrive/SharePoint

Sistema completo para leitura e validação de QR codes em arquivos PDF, verificando se os links do OneDrive/SharePoint estão funcionando corretamente.

## 🚀 Funcionalidades

- ✅ Leitura automática de QR codes em PDFs
- ✅ Validação de links do OneDrive e SharePoint
- ✅ Interface moderna e responsiva
- ✅ Suporte para múltiplos arquivos PDF
- ✅ Exportação de relatórios em CSV e Excel
- ✅ Filtros por status (válidos/erros)
- ✅ Backend Python para validação robusta
- ✅ Deploy fácil no GitHub Pages + Vercel

## 📋 Pré-requisitos

- Conta no GitHub
- Conta no Vercel (gratuita)
- Navegador web moderno

## 🛠️ Instalação e Deploy

### Opção 1: Deploy Completo (Frontend + Backend)

#### Passo 1: Criar Repositório no GitHub

1. Acesse [GitHub](https://github.com) e faça login
2. Clique em "New repository" (botão verde)
3. Preencha:
   - **Repository name**: `qrcode-validator`
   - **Description**: `Validador de QR Codes para OneDrive/SharePoint`
   - Marque: ✅ Public
   - ✅ Add a README file
4. Clique em "Create repository"

#### Passo 2: Fazer Upload dos Arquivos

1. No repositório criado, clique em "Add file" → "Upload files"
2. Arraste todos os arquivos do projeto:
   ```
   qrcode-validator/
   ├── index.html
   ├── vercel.json
   ├── README.md
   └── api/
       ├── app.py
       └── requirements.txt
   ```
3. Escreva uma mensagem de commit: `Initial commit`
4. Clique em "Commit changes"

#### Passo 3: Deploy do Backend no Vercel

1. Acesse [Vercel](https://vercel.com) e faça login com sua conta GitHub
2. Clique em "Add New" → "Project"
3. Selecione o repositório `qrcode-validator`
4. Configure o projeto:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - Clique em "Deploy"
5. Aguarde o deploy finalizar (2-3 minutos)
6. Copie a URL gerada (ex: `https://qrcode-validator.vercel.app`)

#### Passo 4: Atualizar URL do Backend no Frontend

1. No GitHub, abra o arquivo `index.html`
2. Clique no ícone de edição (lápis)
3. Encontre a linha (aproximadamente linha 380):
   ```javascript
   const API_URL = 'https://seu-backend.vercel.app/validate';
   ```
4. Substitua pela URL do Vercel (adicione `/api/validate`):
   ```javascript
   const API_URL = 'https://qrcode-validator.vercel.app/api/validate';
   ```
5. Clique em "Commit changes"

#### Passo 5: Habilitar GitHub Pages

1. No repositório, vá em "Settings" → "Pages"
2. Em "Source", selecione:
   - **Branch**: `main`
   - **Folder**: `/ (root)`
3. Clique em "Save"
4. Aguarde 1-2 minutos
5. A URL do site estará disponível: `https://SEU-USUARIO.github.io/qrcode-validator/`

### Opção 2: Deploy Apenas Frontend (Validação Básica)

Se preferir usar apenas o frontend sem backend:

1. Siga os passos 1, 2 e 5 acima
2. No arquivo `index.html`, a validação será feita localmente
3. Limitação: Validação menos precisa devido às restrições CORS do navegador

## 📖 Como Usar

1. Acesse o site: `https://SEU-USUARIO.github.io/qrcode-validator/`
2. Arraste ou selecione um ou mais arquivos PDF
3. Aguarde a análise automática
4. Visualize os resultados:
   - 🟢 Verde = Link válido
   - 🔴 Vermelho = Link com erro
5. Use os filtros para ver apenas válidos ou erros
6. Exporte o relatório em CSV ou Excel

## 🔧 Estrutura do Projeto

```
qrcode-validator/
├── index.html              # Frontend - Interface web
├── vercel.json            # Configuração do Vercel
├── README.md              # Documentação
└── api/
    ├── app.py             # Backend Flask - API de validação
    └── requirements.txt   # Dependências Python
```

## 🌐 APIs Disponíveis

### POST /api/validate
Valida uma única URL

**Request:**
```json
{
  "url": "https://sharepoint.com/..."
}
```

**Response:**
```json
{
  "valid": true,
  "url": "https://sharepoint.com/...",
  "error": null,
  "timestamp": 1234567890
}
```

### POST /api/validate-batch
Valida múltiplas URLs

**Request:**
```json
{
  "urls": [
    "https://sharepoint.com/...",
    "https://onedrive.com/..."
  ]
}
```

**Response:**
```json
{
  "results": [...],
  "total": 2,
  "valid_count": 1,
  "error_count": 1
}
```

### GET /api/health
Verifica status da API

## 🐛 Solução de Problemas

### Backend não está validando
- Verifique se a URL do backend está correta no `index.html`
- Teste acessando: `https://seu-backend.vercel.app/api/health`
- Deve retornar: `{"status": "healthy"}`

### QR codes não estão sendo detectados
- Verifique se o PDF contém QR codes válidos
- Tente aumentar a resolução do PDF
- Alguns QR codes muito pequenos podem não ser detectados

### Erro CORS
- Certifique-se de que o backend está rodando no Vercel
- Verifique se `flask-cors` está instalado

### GitHub Pages não atualizou
- Aguarde até 5 minutos após o commit
- Limpe o cache do navegador (Ctrl + F5)
- Verifique em Settings → Pages se está habilitado

## 🔒 Segurança

- O backend não armazena nenhuma URL ou dado
- Todas as validações são feitas em tempo real
- Não há coleta de informações pessoais

## 📊 Limitações

- QR codes muito pequenos (<100x100px) podem não ser detectados
- PDFs protegidos por senha não podem ser processados
- Links que exigem autenticação aparecerão como erro

## 🤝 Contribuindo

Sinta-se à vontade para:
- Abrir issues para reportar bugs
- Sugerir melhorias
- Fazer pull requests

## 📝 Licença

MIT License - Livre para uso pessoal e comercial

## 👨‍💻 Desenvolvimento Local

Para testar localmente:

### Frontend
```bash
# Abra index.html diretamente no navegador
# ou use um servidor local:
python -m http.server 8000
# Acesse: http://localhost:8000
```

### Backend
```bash
cd api
pip install -r requirements.txt
python app.py
# API disponível em: http://localhost:5000
```

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique a seção "Solução de Problemas"
2. Abra uma issue no GitHub
3. Consulte a documentação do Vercel e GitHub Pages

---

**Desenvolvido com ❤️ para facilitar a validação de QR codes em PDFs**
