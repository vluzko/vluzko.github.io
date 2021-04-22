"""Convert a markdown file to a post"""
from pathlib import Path


def build_index():
    """Build index.html"""
    raise NotImplementedError


def parse_post(post: Path):
    raise NotImplementedError
