import os
from typing import Any

from decorator import Decorator, LabelProfile, SpaceLabel, EndLabel
from label_table import Table
from type import Type


class Markdown:
    """Markdown obj
    """

    def __init__(self):
        self.__content = list()
        self.__path = ''
        self.__export_name = 'export.md'

    def __finish(self):
        """set finish label
        """
        if len(self.__content):
            self.__content.append(self.__content.pop()[:-1])

    def export(self, export_name: str = 'export.md', *, path: str = os.getcwd(), encoding: str = 'utf-8'):
        """export to .md file
        """
        self.__finish()

        self.__path = path if path.endswith('/') else path + '/'
        self.__export_name = export_name

        with open(f'{self.get_export_path()}', "w", encoding=encoding) as f:
            f.writelines(self.__content)

    def get_content(self):
        """get content
        """
        return self.__content

    def get_export_path(self):
        """get export path
        """
        return self.__path + self.__export_name

    @Decorator.markdown(label=Type.NULL)
    def add_text(self, text: str, *, tab: int = 0, count: int = 0, linefeed: int = 2):
        """add text
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=tab, space=0, count=count),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H1)
    def add_h1(self, text: str, *, linefeed: int = 2):
        """add h1 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H2)
    def add_h2(self, text: str, *, linefeed: int = 2):
        """add h2 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H3)
    def add_h3(self, text: str, *, linefeed: int = 2):
        """add h3 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H4)
    def add_h4(self, text: str, *, linefeed: int = 2):
        """add h4 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H5)
    def add_h5(self, text: str, *, linefeed: int = 2):
        """add h5 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.H6)
    def add_h6(self, text: str, *, linefeed: int = 2):
        """add h6 label
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.STRIKETHROUGH)
    def add_strikethrough(self, text: str, *, tab: int = 0, count: int = 0, linefeed: int = 2):
        """add strikethrough label
        """
        return LabelProfile(
            single=False, text=text,
            space=SpaceLabel(tab=tab, space=0, count=count),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.BOLD)
    def add_bold(self, text: str, *, tab: int = 0, count: int = 0, linefeed: int = 2):
        """add bold label
        """
        return LabelProfile(
            single=False, text=text,
            space=SpaceLabel(tab=tab, space=0, count=count),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.QUOTE)
    def add_quote(self, text: str, *, level: int = 0, linefeed: int = 2):
        """add quote
        """
        if not isinstance(level, int):
            raise TypeError(f"level: {level} type is not int.")

        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=0, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=level)

    @Decorator.markdown(label=Type.SPLIT_LINE)
    def add_split_line(self):
        """add split line
        """
        return LabelProfile(
            single=True, text="",
            space=SpaceLabel(tab=0, space=0, count=0),
            end=EndLabel(linefeed=2),
            args=None)

    @Decorator.markdown(label=Type.UNORDERED_LIST)
    def add_unordered_list(self, text: str, *, tab: int = 0, linefeed: int = 1):
        """add unordered list
        """
        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=tab, space=1, count=0),
            end=EndLabel(linefeed=linefeed),
            args=None)

    @Decorator.markdown(label=Type.ORDERED_LIST)
    def add_ordered_list(self, *, level: int = 0, index: Any = Any, text: str = '', linefeed: int = 1):
        """add ordered list
        """
        if not isinstance(level, int):
            raise TypeError(f"level: {level} type is not int.")

        tab = 0 if level < 0 else 3 * level

        if not isinstance(index, str) and not isinstance(index, float) and not isinstance(index, int):
            raise TypeError(f"index: {index} type is not str, float or int.")

        return LabelProfile(
            single=True, text=text,
            space=SpaceLabel(tab=tab, space=1, count=2),
            end=EndLabel(linefeed=linefeed),
            args=index)

    @Decorator.markdown(label=Type.IMAGE)
    def add_image(self, url: str = '', *, alt: str = 'image_alt', title: str = 'image_title'):
        """add image
        """
        return LabelProfile(
            single=True, text="",
            space=SpaceLabel(tab=0, space=0, count=0),
            end=EndLabel(linefeed=2),
            args=(url, alt, title))

    @Decorator.markdown(label=Type.URL)
    def add_url(self, url: str = '', *, title: str = 'url_title',
                tab: int = 0, count: int = 0, linefeed: int = 2):
        """add url
        """
        return LabelProfile(
            single=True, text="",
            space=SpaceLabel(tab=tab, space=0, count=count),
            end=EndLabel(linefeed=linefeed),
            args=(url, title))

    @Decorator.markdown(label=Type.CODE)
    def add_code(self, language: str = '', *, linefeed: int = 1):
        """add code
        """
        if not isinstance(language, str):
            raise TypeError(f"language: {language} type is not str.")

        return LabelProfile(
            single=True, text="",
            space=SpaceLabel(tab=0, space=0, count=0),
            end=EndLabel(linefeed=linefeed),
            args=language)

    @Decorator.markdown(label=Type.TABLE)
    def table(self, tb: Table):
        """add table
        """
        if not isinstance(tb, Table):
            raise TypeError(f"tb: {tb} type is not Table.")

        return LabelProfile(
            single=True, text=tb.get_content(),
            space=SpaceLabel(tab=0, space=0, count=0),
            end=EndLabel(linefeed=1),
            args=None)


if __name__ == "__main__":
    md = Markdown()
    md.add_h1("Title1")
    md.add_text("Content will not change to new line.")
    md.add_text("Content in the same line.")
    md.add_h2("Title2")
    md.add_strikethrough("Content deprecated")
    md.add_split_line()
    md.add_h2("Title3")
    md.add_quote("Quote content in this line.", linefeed=0)
    md.add_bold("Bold Content", linefeed=2)
    md.add_image("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2931826153,3045777172&fm=26&gp=0.jpg")
    md.add_image("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2931826153,3045777172&fm=26&gp=0.jpg",
                 alt="hello", title="image")
    md.add_url("https://www.google.com", title='google')
    md.add_unordered_list("unordered list point 1")
    md.add_unordered_list("unordered list point 2")
    md.add_unordered_list("unordered list point 3", linefeed=2)
    md.add_ordered_list(level=0, index=1, text="ordered list point one")
    md.add_ordered_list(level=0, index=2, text="ordered list point two")
    md.add_ordered_list(level=1, index=2.1, text="dead beef1")
    md.add_ordered_list(level=0, index=3, text="ordered list point three")
    md.add_ordered_list(level=1, index=3.1, text="dead beef2")
    md.add_ordered_list(level=2, index="3.1.1", text="dead beef3")
    md.add_ordered_list(level=2, index="3.1.1", text="dead beef4")
    md.add_ordered_list(level=0, index=4, text="ordered list point four", linefeed=2)
    md.add_code("python")
    code = """import os
import datetime
time_now = datetime.datetime.now()
print(time_now)"""
    md.add_text(code, linefeed=1)
    md.add_code(linefeed=2)

    table = Table(3, 3)
    table.head(['姓名', '技能', '排行'])
    table.insert_row(0, ['刘备', '仁德', '老大'])
    table.insert_row(2, ['张飞', '勇武', '老三'])
    table.insert_row(1, ['关羽', '武圣', '老二'])
    md.table(table)

    table.set_value(2, 1, "咆哮")
    md.table(table)

    table.resize(3, 4)
    table.set_head(3, '性别')
    md.table(table)

    md.export("test.md")
