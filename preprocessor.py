"""Convert a markdown file to a post"""
import mistune
import re
import yaml

from bs4 import BeautifulSoup
from pathlib import Path
from sys import argv
from typing import Tuple


OUTPUT_DIR = Path(__file__).parent / 'posts'


def build_index():
    """Build index.html"""
    raise NotImplementedError


def parse_meta(text: str) -> dict:
    meta = yaml.safe_load(text)
    return meta


def parse_metadata(text: str) -> Tuple[dict, str]:
    open_close = re.compile(r'^(---\n(.*)\n---\n)?(.*)')
    match = re.match(open_close, text)
    assert match is not None
    print(match.groups())
    groups = match.groups()
    assert len(groups) == 3
    if groups[0] is None:
        assert groups[1] is None
        return {}, groups[2]
    else:
        metadata = parse_meta(groups[1])
        return metadata, groups[2]


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


def generate_nav_page():
    raise NotImplementedError


def parse_post(post: Path):
    text = post.open().read()
    meta_data, remaining = parse_metadata(text)
    html = mistune.markdown(remaining)
    ast = BeautifulSoup(html, 'html.parser')

    with_math = add_mathjax(ast)
    import pdb
    pdb.set_trace()


if __name__ == '__main__':
    p = Path(argv[1])
    parse_post(p)

