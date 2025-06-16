# 📩 Daily Business News Summary via Email

Este projeto automatiza o envio de um resumo diário das principais notícias de negócios diretamente para sua caixa de entrada.

## ✨ Funcionalidades

- Consulta automática à [NewsAPI](https://newsapi.org/) para obter as manchetes mais recentes da categoria "Business".
- Geração de um resumo simples e direto com título, descrição e link da notícia.
- Envio diário por e-mail com conteúdo formatado.
- Execução automatizada com a biblioteca `schedule` ou via serviços como o [PythonAnywhere](https://www.pythonanywhere.com/).

## 🛠️ Tecnologias utilizadas

- Python 3
- [requests](https://pypi.org/project/requests/)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [email.mime](https://docs.python.org/3/library/email.mime.html)
- [NewsAPI](https://newsapi.org/)
- [PythonAnywhere](https://www.pythonanywhere.com/) (para automação gratuita)
