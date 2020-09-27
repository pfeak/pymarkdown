# pymarkdown

Use python to generate markdown.

## Usage

* init `Markdown` object

```python
from markdown import Markdown
md = Markdown()
```

* add text

```python
from markdown import Markdown
md = Markdown()
md.add_text("content")
md.add_text("open file.", end=False)
md.add_text("this raw will not exe '\n'")
```

* h1~h2

```python
from markdown import Markdown
md = Markdown()
md.add_h1("title 1")
md.add_h2("title 2")
md.add_h2("title 3")
```

* add strikethrough, bold

```python
from markdown import Markdown
md = Markdown()
md.add_strikethrough("update", end=True)
md.add_bold("bold text")
```

* export to `.md`

```python
from markdown import Markdown
# new class obj
md = Markdown()
# add content
md.add_h1("title 1")
md.add_text("content 1")
md.add_text("open file.", end=False)
md.add_text("this raw will not exe '\n'")
md.add_h2("title 2")
md.add_text("content 2")
md.add_strikethrough("update", end=True)
md.add_h2("title 3")
md.add_bold("bold text")
md.add_text("content 3")
# export to .md
md.export("test.md")
```
