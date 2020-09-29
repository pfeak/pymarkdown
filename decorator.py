from dataclasses import dataclass
from typing import Any

from type import Type


# {tab}{label}{space}{text}[{space}{label}]{count}{linefeed}


@dataclass
class SpaceLabel:
    tab: int = 0
    space: int = 1
    count: int = 0


@dataclass
class EndLabel:
    linefeed: int = 2


@dataclass
class LabelProfile:
    __slots__ = ['single', 'text', 'space', 'end', 'args']
    single: bool
    text: str
    space: SpaceLabel
    end: EndLabel
    args: Any


class Decorator:
    """Decorator object
    """

    @staticmethod
    def markdown(label: Type = None):
        def func_wrap(func):
            def wrap(context, *args, **kwargs):
                Decorator.__process(label, func, context, *args, **kwargs)

            return wrap

        return func_wrap

    @staticmethod
    def __process(label: Type, func, context, *args, **kwargs):
        profile: LabelProfile = func(context, *args, **kwargs)
        Decorator.__handle_content(
            context=context,
            single=Handler.single(profile.single),
            tab=Handler.tab(profile.space.tab),
            label=Handler.label(label, profile.args),
            space=Handler.space(profile.space.space),
            text=Handler.text(profile.text),
            count=Handler.count(profile.space.count),
            linefeed=Handler.linefeed(profile.end.linefeed)
        )

    # {tab}{label}{space}{text}[{space}{label}]{count}{linefeed}
    @staticmethod
    def __handle_content(context, **kwargs) -> None:
        tab = kwargs['tab']
        label = kwargs['label']
        space = kwargs['space']
        text = kwargs['text']
        count = kwargs['count']
        linefeed = kwargs['linefeed']
        content = tab + label + space + text + count + linefeed \
            if kwargs['single'] else \
            tab + label + space + text + space + label + count + linefeed

        context.get_content().append(content)


class Handler:
    """Handle structure
    """

    @staticmethod
    def single(single: bool) -> bool:
        if not isinstance(single, bool):
            raise TypeError(f"single: {single} type is not bool")

        return single

    @staticmethod
    def tab(tab: int) -> str:
        if not isinstance(tab, int):
            raise TypeError(f"tab: {tab} type is not int")

        tab = 0 if tab < 0 else tab
        return tab * Type.SPACE.value

    @staticmethod
    def label(label: Type, command: Any) -> str:
        if not isinstance(label, Type):
            raise TypeError(f"label: {label} type is not Type")

        return Handler.LabelHandler.label(label, command)

    @staticmethod
    def space(space: int) -> str:
        if not isinstance(space, int):
            raise TypeError(f"space: {space} type is not int")

        space = 0 if space < 0 else space
        space = 2 if space > 2 else space
        return space * Type.SPACE.value

    @staticmethod
    def text(text: str) -> str:
        if not isinstance(text, str):
            raise TypeError(f"text: {text} type is not str")

        return text if text else Type.NULL.value

    @staticmethod
    def count(count: int) -> str:
        if not isinstance(count, int):
            raise TypeError(f"count: {count} type is not int")

        count = 0 if count < 0 else count
        count = 2 if count > 2 else count
        return count * Type.SPACE.value

    @staticmethod
    def linefeed(linefeed: int) -> str:
        if not isinstance(linefeed, int):
            raise TypeError(f"linefeed: {linefeed} type is not int")

        linefeed = 0 if linefeed < 0 else linefeed
        linefeed = 2 if linefeed > 2 else linefeed
        return linefeed * Type.SEP.value

    class LabelHandler:
        """Handle label
        """

        @staticmethod
        def label(label: Type, command: Any) -> str:
            has_attr = hasattr(Handler.LabelHandler, f"label_{label.name.lower()}")
            return getattr(Handler.LabelHandler, f"label_{label.name.lower()}")(command=command) \
                if has_attr else label.value

        @staticmethod
        def label_image(command: ()) -> str:
            url, alt, title = command
            url = url if url else ''
            alt = alt if alt else ''
            title = f" \"{title}\"" if title else ''
            return Type.IMAGE.value.replace('REPLACE_ALT', alt, 1) \
                .replace('REPLACE_URL', url, 1) \
                .replace(' REPLACE_TITLE', title, 1)

        @staticmethod
        def label_url(command: ()) -> str:
            url, title = command
            url = url if url else ''
            title = title if title else ''
            return Type.URL.value.replace('REPLACE_URL', url, 1).replace('REPLACE_TITLE', title, 1)

        @staticmethod
        def label_ordered_list(command: int) -> str:
            args_type, index = command
            replace_str = "REPLACE_NUMBER" if args_type == int else "REPLACE_NUMBER."
            return Type.ORDERED_LIST.value.replace(replace_str, str(index), 1)
