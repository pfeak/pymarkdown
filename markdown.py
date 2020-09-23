import os

from type import Type


class Decorator:
    """Decorator object
    """

    @staticmethod
    def markdown(label: Type = None):
        def func_wrap(func):
            def wrap(context, *args, **kwargs):
                Decorator.__process_main(label, func, context, *args, **kwargs)

            return wrap

        return func_wrap

    @staticmethod
    def __process_main(label: Type, func, context, *args, **kwargs):
        if label == Type.IMAGE:
            text, single, space, end, image = func(context, *args, **kwargs)
            Decorator.__process_image(context=context, label=label, text=text, single=single, space=space, end=end,
                                      image=image)
        else:
            text, single, space, end = func(context, *args, **kwargs)
            Decorator.__process_symbol(context=context, label=label, text=text, single=single, space=space, end=end)

    @staticmethod
    def __process_symbol(label: Type, **kwargs):
        Decorator.__handle_content(
            kwargs['context'],                          # handle context
            Decorator.__handle_text(kwargs['text']),    # handle text
            label.value if label else "",               # handle label
            Decorator.__handle_space(kwargs['space']),  # handle space
            kwargs['single'],                           # handle single
            Decorator.__handle_end(kwargs['end'])       # handle end
        )

    @staticmethod
    def __process_image(label: Type, **kwargs):
        url, alt, title = kwargs['image']
        url = url if url else ''
        alt = alt if alt else ''
        title = f" \"{title}\"" if title else ''
        tmp_label = label.value if label else ""
        tmp_label = tmp_label.replace('REPLACE_ALT', alt, 1) \
            .replace('REPLACE_URL', url, 1) \
            .replace(' REPLACE_TITLE', title, 1)
        Decorator.__handle_content(
            kwargs['context'],                          # handle context
            Decorator.__handle_text(kwargs['text']),    # handle text
            tmp_label,                                  # handle label
            Decorator.__handle_space(kwargs['space']),  # handle space
            kwargs['single'],                           # handle single
            Decorator.__handle_end(kwargs['end'])       # handle end
        )

    @staticmethod
    def __handle_content(context, text: str, label: str, space: str, single: bool, end: str) -> None:
        context.get_content().append(
            label + space + text + end if single else label + space + text + space + label + end)

    @staticmethod
    def __handle_text(text: str) -> str:
        return text if text else ""

    @staticmethod
    def __handle_space(space: bool) -> str:
        return Type.SPACE.value if space else Type.NULL.value

    @staticmethod
    def __handle_end(end: bool) -> str:
        return 2 * Type.SEP.value if end else Type.NULL.value


class Markdown:
    """Markdown obj
    """

    def __init__(self):
        self.__content = list()
        self.__path = ''
        self.__export_name = 'export.md'

    def __finish(self):
        self.__content.append(self.__content.pop()[:-1])

    def export(self, export_name: str = 'export.md', *, path: str = os.getcwd(), encoding: str = 'utf-8'):
        self.__finish()

        self.__path = path if path.endswith('/') else path + '/'
        self.__export_name = export_name

        with open(f'{self.get_export_path()}', "w", encoding=encoding) as f:
            f.writelines(self.__content)

    def get_content(self):
        return self.__content

    def get_export_path(self):
        return self.__path + self.__export_name

    @Decorator.markdown(label=Type.NULL)
    def add_text(self, text: str, *, single: bool = True, space: bool = False, end: bool = True):
        """add text
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H1)
    def add_h1(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h1 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H2)
    def add_h2(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h2 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H3)
    def add_h3(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h3 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H4)
    def add_h4(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h4 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H5)
    def add_h5(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h5 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.H6)
    def add_h6(self, text: str, *, single: bool = True, space: bool = True, end: bool = True):
        """add h6 label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.BOLD)
    def add_bold(self, text: str, *, single: bool = False, space: bool = False, end: bool = False):
        """add bold label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.STRIKETHROUGH)
    def add_strikethrough(self, text: str, *, single: bool = False, space: bool = False, end: bool = False):
        """add strikethrough label
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.QUOTE)
    def add_quote(self, text: str, *, single: bool = True, space: bool = False, end: bool = True):
        """add quote
        """
        return text, single, space, end

    @Decorator.markdown(label=Type.SPLIT_LINE)
    def add_split_line(self, *, single: bool = True, space: bool = False, end: bool = True):
        """add split line
        """
        text = ''
        return text, single, space, end

    @Decorator.markdown(label=Type.IMAGE)
    def add_image(self, url: str = '', *, alt: str = 'image', title: str = ''):
        """add image
        """
        text = ''
        single = True
        space = False
        end = True
        return text, single, space, end, (url, alt, title)


if __name__ == "__main__":
    md = Markdown()
    md.add_h1("Title1")
    md.add_text("Content will not change to new line.", end=False)
    md.add_text("Content in the same line.")
    md.add_h2("Title2")
    md.add_strikethrough("Content deprecated", end=True)
    md.add_split_line()
    md.add_h2("Title3")
    md.add_quote("Quote content in this line.", end=False)
    md.add_bold("Bold Content", end=True)
    md.add_image(
        "https://timgsa.baidu.com/timg?image"
        "&quality=80&size=b9999_10000&sec=1600850864228"
        "&di=a9ef2aeb8fa4b61feb965a806cf3e69f"
        "&imgtype=0&src=http%3A%2F%2Fimg4.imgtn.bdimg.com%2Fit%2Fu%3D159562664%2C875509196%26fm%3D214%26gp%3D0.jpg")
    md.add_image("https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=2931826153,3045777172&fm=26&gp=0.jpg",
                 alt="hello", title="image")
    md.export("test.md")
