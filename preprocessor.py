"""Convert a markdown file to a post"""
import pdb
import mistune
import re
import yaml

from bs4 import BeautifulSoup, element
from pathlib import Path
from sys import argv
from typing import Tuple

from markdown_latex import markdown2html_mistune


LOCAL_PREFIX = Path(__file__).parent
PAGES_DIR = LOCAL_PREFIX / 'pages'
BLOG_SOURCE = LOCAL_PREFIX / 'posts' / 'markdown'
OUTPUT_DIR = LOCAL_PREFIX / 'posts'
TEMPLATE = LOCAL_PREFIX / 'template.html'
BLOG_INDEX = LOCAL_PREFIX / 'blog.html'
GITHUB_PREFIX = '/vluzko.github.io/'
PROD = True


def build_index():
    """Build index.html"""
    raise NotImplementedError


def parse_meta(text: str) -> dict:
    meta = yaml.safe_load(text)
    return meta


def parse_metadata(text: str) -> Tuple[dict, str]:
    start_end = re.compile(r'---\n')
    first = re.search(start_end, text)
    if first is None:
        return {}, text
    else:
        second = re.search(start_end, text[4:])
        assert second is not None
        text_start = 4 + second.end()
        meta_text = text[4:second.start() + 4]
        metadata = parse_meta(meta_text)
        main_text = text[text_start:]
        return metadata, main_text


def add_mathjax(ast: BeautifulSoup) -> BeautifulSoup:
    src_1 = "https://polyfill.io/v3/polyfill.min.js?features=es6"
    tag_1 = ast.new_tag('script', src=src_1)
    src_2 = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
    # <script id="MathJax-script" async src=></script>
    tag_2 = ast.new_tag('script', src=src_2, id='MathJax-script')
    tag_2.attrs['async'] = None

    ast.insert(0, tag_2)
    ast.insert(0, tag_1)
    return ast


def build_post_index(post_template: BeautifulSoup, content_div: element.Tag) -> BeautifulSoup:
    heading_tags = [f'h{x}' for x in range(1, 6)]
    headings = content_div.findAll(heading_tags)

    index_wrapper = post_template.new_tag('div', id='post-index')
    index = post_template.new_tag('ul', id='post-index')
    for heading in headings:
        link_text = heading.string.lower().replace(' ', '-')
        internal_link = post_template.new_tag('a')
        internal_link.attrs['href'] = f'#{link_text}'
        internal_link.string = heading.string

        item = post_template.new_tag('li')
        item.append(internal_link)
        index.append(item)

        target_link = post_template.new_tag('a')
        target_link.attrs['name'] = link_text
        heading.append(target_link)
    index_wrapper.append(index)
    top = post_template.find('div', {'id': 'main'})
    top.append(index_wrapper)
    return post_template


def process_post(post: Path) -> Tuple[dict, BeautifulSoup]:
    text = post.open().read()
    meta_data, remaining = parse_metadata(text)
    html = mistune.markdown(remaining)
    html = markdown2html_mistune(remaining)
    # import pdb
    # pdb.set_trace()
    post_content = BeautifulSoup(html, 'html.parser')

    post_template = get_template_ast()
    content_div = post_template.find('div', {'id': 'content0'})
    content_div.append(post_content)

    # Rewrite page title
    title = post_template.find('title')
    title.string = meta_data['title']

    # Build post index
    post_template = build_post_index(post_template, content_div)

    return meta_data, post_template


def process_page(post: Path, page_name: str) -> BeautifulSoup:
    text = post.open().read()
    html = mistune.markdown(text)
    content_ast = BeautifulSoup(html, 'html.parser')

    page = get_template_ast()
    content_div = page.find('div', {'id': 'content0'})
    content_div.append(content_ast)

    # Set the title
    title_element = page.find('title')
    title_element.string = page_name

    return page


def get_template_ast() -> BeautifulSoup:
    html = TEMPLATE.open().read()
    ast = BeautifulSoup(html, 'html.parser')

    navbar = ast.find('nav', {'id': 'navigation'})

    if PROD:
        link_prefix = ''
    else:
        link_prefix = str(LOCAL_PREFIX.absolute())

    for link in navbar.findAll('a'):
        href = link.attrs['href']
        new_href = f'{link_prefix}/{href}'
        link.attrs['href'] = new_href


    return ast


def generate_post_list() -> dict:
    all_meta = {}
    for f in BLOG_SOURCE.glob('**/*.md'):
        meta_data, post_ast = process_post(f)
        start_index = f.parts.index('posts') + 2
        output_path = Path(OUTPUT_DIR, *f.parts[start_index:]).with_suffix('.html')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.open('w+').write(post_ast.prettify())
        meta_data['link'] = f'/{str(Path(*output_path.absolute().parts[5:]))}'
        all_meta[f] = meta_data

    return all_meta


def generate_blog_page(post_meta: dict):
    ast = get_template_ast()
    content_div = ast.find('div', {'id': 'content0'})
    posts = ast.new_tag('ul', id='blog-index')
    for k, v in sorted(post_meta.items(), key=lambda x: x[1]['date'], reverse=True):
        link = ast.new_tag('a', href= v['link'])
        link.string = v['title']
        l_item = ast.new_tag('li')
        l_item.append(link)
        posts.append(l_item)
    content_div.append(posts)

    title_element = ast.find('title')
    title_element.string = 'Blog'

    BLOG_INDEX.open('w+').write(ast.prettify())


def generate_pages():
    for f in PAGES_DIR.glob('*.md'):
        page_name = f.stem.capitalize()
        page_ast = process_page(f, page_name)
        output_path = Path(LOCAL_PREFIX, f.stem).with_suffix('.html')
        output_path.open('w+').write(page_ast.prettify())


def generate_site():
    post_meta = generate_post_list()
    generate_pages()
    generate_blog_page(post_meta)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == 'dev':
        PROD = False
    generate_site()

