import platform
from enum import Enum, unique


@unique
class Type(Enum):
    """Markdown type
    """
    # Place holder
    NULL = ""
    SPACE = " "

    # Markdown single symbol
    H1 = "#"
    H2 = "##"
    H3 = "###"
    H4 = "####"

    # Markdown double symbol
    BOLD = "**"
    STRIKETHROUGH = "~~"

    if platform.system() == "Windows":
        SEP = '\r\n'
    elif platform.system() == "Linux":
        SEP = '\n'
    else:  # for mac os
        SEP = '\r'


class Decorator:
    """Decorator object
    """
    @staticmethod
    def markdown(label: Type = None):
        def func_wrap(func):
            def wrap(self, *args, **kwargs):
                text, single, space, end = func(self, *args, **kwargs)
                tmp_label = label.value if label else ""
                tmp_text = text if text else ""
                tmp_space = Type.SPACE.value if space else Type.NULL.value
                tmp_end = 2 * Type.SEP.value if end else Type.NULL.value
                content = tmp_label + tmp_space + tmp_text if single \
                    else tmp_label + tmp_space + tmp_text + tmp_space + tmp_label
                self.content.append(content + tmp_end)

            return wrap

        return func_wrap


class Markdown:
    """Markdown obj
    """
    def __init__(self):
        self.content = list()

    def export(self, export_name: str = 'export.md', encoding: str = 'utf-8'):
        self.__finish()
        with open(export_name, "w", encoding=encoding) as f:
            f.writelines(self.content)

    def __finish(self):
        self.content.append(self.content.pop()[:-1])

    @Decorator.markdown(label=Type.NULL)
    def add_text(self, text: str, single: bool = True, space: bool = False, end: bool = True):
        """add text
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H1)
    def add_h1(self, text: str, single: bool = True, space: bool = True, end: bool = True):
        """add h1 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H2)
    def add_h2(self, text: str, single: bool = True, space: bool = True, end: bool = True):
        """add h2 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H3)
    def add_h3(self, text: str, single: bool = True, space: bool = True, end: bool = True):
        """add h3 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H4)
    def add_h4(self, text: str, single: bool = True, space: bool = True, end: bool = True):
        """add h4 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.BOLD)
    def add_bold(self, text: str, single: bool = False, space: bool = False, end: bool = False):
        """add bold label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.STRIKETHROUGH)
    def add_strikethrough(self, text: str, single: bool = False, space: bool = False, end: bool = False):
        """add strikethrough label
        """
        return text, single, space, end


if __name__ == "__main__":
    md = Markdown()
    md.add_h1("标题1")
    md.add_text("这是一个测试文档")
    md.add_text("打开文档记录。", end=False)
    md.add_text("这句话不会换行")
    md.add_h2("标题2")
    md.add_text("内容内容内容内容内容")
    md.add_strikethrough("这部分更新了", end=True)
    md.add_h2("标题3")
    md.add_bold("哈哈哈")
    md.add_text("内容")
    md.export("test.md")
