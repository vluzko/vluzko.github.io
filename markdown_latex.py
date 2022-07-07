"""Markdown filters with mistune

Used from markdown.py

Shamelessly stolen/modified from IPython
"""


from functools import partial


from html import escape

html_escape = partial(escape, quote=False)

from mistune import HTMLRenderer, InlineParser, Markdown
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound


def _dotall(pattern):
    """Make the '.' special character match any character inside the pattern, including a newline.

    This is implemented with the inline flag `(?s:...)` and is equivalent to using `re.DOTALL` when
    it is the only pattern used. It is necessary since `mistune>=2.0.0`, where the pattern is passed
    to the undocumented `re.Scanner`.
    """
    return f"(?s:{pattern})"


class MathInlineParser(InlineParser):
    r"""This interprets the content of LaTeX style math objects.

    In particular this grabs ``$$...$$``, ``\\[...\\]``, ``\\(...\\)``, ``$...$``,
    and ``\begin{foo}...\end{foo}`` styles for declaring mathematics. It strips
    delimiters from all these varieties, and extracts the type of environment
    in the last case (``foo`` in this example).
    """
    BLOCK_MATH_TEX = _dotall(r"(?<!\\)\$\$(.*?)(?<!\\)\$\$")
    BLOCK_MATH_LATEX = _dotall(r"(?<!\\)\\\\\[(.*?)(?<!\\)\\\\\]")
    INLINE_MATH_TEX = _dotall(r"(?<![$\\])\$(.+?)(?<![$\\])\$")
    INLINE_MATH_LATEX = _dotall(r"(?<!\\)\\\\\((.*?)(?<!\\)\\\\\)")

    # The order is important here
    RULE_NAMES = (
        "block_math_tex",
        "block_math_latex",
        "inline_math_tex",
        "inline_math_latex",
    ) + InlineParser.RULE_NAMES

    def parse_block_math_tex(self, m, state):
        # sometimes the Scanner keeps the final '$$', so we use the
        # full matched string and remove the math markers
        text = m.group(0)[2:-2]
        return "block_math", text

    def parse_block_math_latex(self, m, state):
        text = m.group(1)
        return "block_math", text

    def parse_inline_math_tex(self, m, state):
        text = m.group(1)
        return "inline_math", text

    def parse_inline_math_latex(self, m, state):
        text = m.group(1)
        return "inline_math", text


class MarkdownWithMath(Markdown):
    def __init__(self, renderer, block=None, inline=None, plugins=None):
        if inline is None:
            inline = MathInlineParser(renderer, hard_wrap=False)
        super().__init__(renderer, block, inline, plugins)

    def render(self, s):
        """Compatibility method with `mistune==0.8.4`."""
        return self.parse(s)


class IPythonRenderer(HTMLRenderer):
    def __init__(
        self,
        escape=True,
        allow_harmful_protocols=True,
        embed_images=False,
        exclude_anchor_links=False,
        anchor_link_text="¶",
        path="",
        attachments=None,
    ):
        super().__init__(escape, allow_harmful_protocols)
        self.embed_images = embed_images
        self.exclude_anchor_links = exclude_anchor_links
        self.anchor_link_text = anchor_link_text
        self.path = path
        if attachments is not None:
            self.attachments = attachments
        else:
            self.attachments = {}

    def block_code(self, code, info=None):
        lang = ""
        lexer = None
        if info:
            try:
                lang = info.strip().split(None, 1)[0]
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                code = lang + "\n" + code
                lang = None

        if not lang:
            return super().block_code(code)

        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

    def block_html(self, html):
        return super().block_html(html)

    def escape_html(self, text):
        return html_escape(text)

    def multiline_math(self, text):
        return text

    def block_math(self, text):
        return f"$${self.escape_html(text)}$$"


    def inline_math(self, text):
        return f"${self.escape_html(text)}$"


def markdown2html_mistune(source):
    """Convert a markdown string to HTML using mistune"""
    return MarkdownWithMath(renderer=IPythonRenderer(escape=False)).render(source)
