from dataclasses import dataclass
from typing import Any, Tuple

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
            single=StructHandler.single(profile.single),
            tab=StructHandler.tab(profile.space.tab),
            label=LabelHandler.label(label, profile.args),
            space=StructHandler.space(profile.space.space),
            text=StructHandler.text(profile.text),
            count=StructHandler.count(profile.space.count),
            linefeed=StructHandler.linefeed(profile.end.linefeed)
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


class StructHandler:
    """Handle structure
    """

    @staticmethod
    def single(single: bool) -> bool:
        return single

    @staticmethod
    def tab(tab: int) -> str:
        tab = 0 if tab < 0 else tab
        return tab * Type.SPACE.value

    @staticmethod
    def space(space: int) -> str:
        space = 0 if space < 0 else space
        return space * Type.SPACE.value

    @staticmethod
    def text(text: str) -> str:
        return text if text else Type.NULL.value

    @staticmethod
    def count(count: int) -> str:
        count = 0 if count < 0 else count
        return count * Type.SPACE.value

    @staticmethod
    def linefeed(linefeed: int) -> str:
        linefeed = 0 if linefeed < 0 else linefeed
        return linefeed * Type.SEP.value


class LabelHandler:
    """Handle label
    """

    @staticmethod
    def label(label: Type, command: Any) -> str:
        has_attr = hasattr(LabelHandler, f"label_{label.name.lower()}")
        return getattr(LabelHandler, f"label_{label.name.lower()}")(command=command) if has_attr else label.value

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
