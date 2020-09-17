# pymarkdown
Use python to generate markdown.

## Usage

```python
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