"""Convert a markdown file to a post"""
import mistune
import re
import yaml

from bs4 import BeautifulSoup
from pathlib import Path
from sys import argv
from typing import Tuple


LOCAL_PREFIX = Path(__file__).parent
SOURCE_DIR = LOCAL_PREFIX / 'posts' / 'markdown'
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


def process_post(post: Path, link_start: str='/home/vincent') -> Tuple[dict, BeautifulSoup]:
    text = post.open().read()
    meta_data, remaining = parse_metadata(text)
    html = mistune.markdown(remaining)
    test_ast = BeautifulSoup(html, 'html.parser')

    page = get_template_ast()
    content_div = page.find('div', {'id': 'content0'})
    content_div.append(test_ast)

    return meta_data, page


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


def generate_post_list():
    all_meta = {}
    for f in SOURCE_DIR.glob('**/*.md'):
        meta_data, post_ast = process_post(f)

        output_path = Path(OUTPUT_DIR, *f.parts[2:]).with_suffix('.html')
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.open('w+').write(post_ast.prettify())
        meta_data['link'] = str(output_path)
        all_meta[f] = meta_data

    return all_meta


def generate_nav_page(post_meta: dict):
    ast = get_template_ast()
    content_div = ast.find('div', {'id': 'content0'})
    posts = ast.new_tag('ul')
    for k, v in post_meta.items():
        link = ast.new_tag('a', href= v['link'])
        link.string = v['title']
        l_item = ast.new_tag('li')
        l_item.append(link)
        posts.append(l_item)
    content_div.append(posts)
    BLOG_INDEX.open('w+').write(ast.prettify())


def generate_blog():
    post_meta = generate_post_list()
    generate_nav_page(post_meta)


if __name__ == '__main__':
    if len(argv) > 1 and argv[1] == 'dev':
        PROD = False
    generate_blog()

