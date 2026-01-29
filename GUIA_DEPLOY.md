# 🚀 GUIA RÁPIDO DE DEPLOY

## Resumo em 5 Passos

### 1️⃣ Criar Repositório no GitHub
```
1. Acesse github.com
2. Clique em "New repository"
3. Nome: qrcode-validator
4. Marque "Public" e "Add README"
5. Clique em "Create repository"
```

### 2️⃣ Fazer Upload dos Arquivos
```
1. No repositório, clique "Add file" → "Upload files"
2. Arraste TODOS os arquivos do projeto
3. Commit message: "Initial commit"
4. Clique em "Commit changes"
```

### 3️⃣ Deploy no Vercel (Backend)
```
1. Acesse vercel.com
2. Login com GitHub
3. "Add New" → "Project"
4. Selecione "qrcode-validator"
5. Clique em "Deploy"
6. COPIE A URL: https://qrcode-validator-xxx.vercel.app
```

### 4️⃣ Atualizar URL no Código
```
1. No GitHub, abra "index.html"
2. Clique no lápis (editar)
3. Encontre linha ~380:
   const API_URL = 'https://seu-backend.vercel.app/validate';
   
4. Troque por SUA URL do Vercel:
   const API_URL = 'https://qrcode-validator-xxx.vercel.app/api/validate';
   
5. "Commit changes"
```

### 5️⃣ Ativar GitHub Pages (Frontend)
```
1. No repositório: "Settings" → "Pages"
2. Source: Branch "main" | Folder "/ (root)"
3. Clique em "Save"
4. Aguarde 2 minutos
5. Acesse: https://SEU-USUARIO.github.io/qrcode-validator/
```

## ✅ Checklist Final

- [ ] Repositório criado no GitHub
- [ ] Todos os arquivos enviados
- [ ] Deploy no Vercel concluído
- [ ] URL do backend atualizada no index.html
- [ ] GitHub Pages ativado
- [ ] Site acessível e funcionando

## 🔍 Testando

1. Acesse seu site GitHub Pages
2. Faça upload de um PDF com QR codes
3. Verifique se os QR codes são detectados
4. Veja se a validação funciona

## ❌ Se algo der errado

### Backend não funciona
- Teste: https://seu-projeto.vercel.app/api/health
- Deve retornar: {"status": "healthy"}
- Se não funcionar, refaça o deploy no Vercel

### Frontend não carrega
- Aguarde 5 minutos após ativar Pages
- Limpe cache: Ctrl + Shift + Delete
- Verifique em Settings → Pages se está "Active"

### QR codes não são detectados
- Verifique se o PDF tem QR codes visíveis
- Teste com um PDF diferente
- Alguns QR codes muito pequenos podem falhar

## 📞 Precisa de Ajuda?

Leia o README.md completo para mais detalhes!

---

**Tempo estimado total: 15 minutos** ⏱️
