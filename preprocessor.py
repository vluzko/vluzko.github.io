"""Convert a markdown file to a post"""
import mistune
import re
import yaml

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
    print(match.groups())
    groups = match.groups()
    assert len(groups) == 3
    if groups[0] is None:
        assert groups[1] is None
        return {}, groups[2]
    else:
        metadata = parse_meta(groups[1])
        return metadata, groups[2]


def parse_post(post: Path):
    text = post.open().read()
    meta_data, remaining = parse_metadata(text)
    html = mistune.markdown(remaining)
    print(html)


if __name__ == '__main__':
    p = Path(argv[1])
    parse_post(p)

