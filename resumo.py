import requests

def obter_resumo_noticias():
       """
       Obtém um resumo das últimas notícias de negócios.
       
       Retorna:
              str: Resumo das notícias.
       """

       url = ('https://newsapi.org/v2/top-headlines?'
              'category=business&'
              'sortBy=popularity&'
              'sortBy=popularity&'
              'pageSize=13&'
              'page=1&'
              'apiKey=')

       response = requests.get(url)
       dados = response.json()
       artigos = dados.get("articles", [])

       resumo = ""

       for i, artigo in enumerate(artigos):
          
          source = artigo["source"]["name"]
          titulo = artigo["title"]
          descricao = artigo["description"]
          conteudo = artigo["content"]
          url_artigo = artigo["url"]

          resumo += f"{titulo}\n{descricao}\n{url_artigo}\n\n"

       print(f"Artigo {i+1}")
       print(f"Fonte: {source}")
       print(f"Título: {titulo}")
       print(f"Descrição: {descricao}")
       print(f"Conteúdo:\n{conteudo}")
       print(f"URL: {url_artigo}")
       print("\n" + "-"*80 + "\n")

       return resumo