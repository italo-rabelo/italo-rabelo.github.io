from jinja2 import Environment, FileSystemLoader
import json
import markdown2

# Carregar dados do JSON
with open('data/posts.json', 'r') as json_file:
    posts = json.load(json_file)

# Configurar ambiente Jinja2
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('post_template.html')

# Gerar páginas HTML
for post in posts:
    # Simular o conteúdo do arquivo Markdown (substitua com leitura real do arquivo)
    markdown_content = f"# {post['title']}\n\n{post['description']}\n\n*Author: {post['author']}*"

    # Converter Markdown para HTML
    html_content = markdown2.markdown(markdown_content)

    # Renderizar HTML usando o template
    output = template.render(title=post['title'], description=post['description'], author=post['author'], content=html_content)

    # Salvar a página HTML gerada
    with open(f'static/{post["title"].replace(" ", "_")}.html', 'w') as html_file:
        html_file.write(output)
