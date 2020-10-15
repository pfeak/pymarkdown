from functools import reduce

from type import Type


class Table:
    SPLIT_SYMBOL = F"{Type.TABLE.value}"

    def __init__(self, row: int = 2, col: int = 2):
        self.__set_row(row)
        self.__set_col(col)

        self.__head = [''] * col
        self.__split = [self.SPLIT_SYMBOL] * col
        self.__table = [[''] * col for _ in range(row)]

    def __set_row(self, row: int = 2):
        if not isinstance(row, int):
            raise TypeError(f"row: {row} type is not int")

        if row < 0:
            raise ValueError(f"row {row} must be larger than or equal to 0")

        self.__row = row

    def __set_col(self, col: int = 2):
        if not isinstance(col, int):
            raise TypeError(f"col: {col} type is not int")

        if col < 0:
            raise ValueError(f"col {col} must be larger than or equal to 0")

        self.__col = col

    def get_table(self):
        table = self.__table[:]
        table.insert(0, self.__split)
        table.insert(0, self.__head)
        return table

    def get_content(self):
        # resolve head
        head = self.__head[:]
        [head.__setitem__(i, head[i] if head[i].endswith(
            Type.TABLE_SPLIT.value) else head[i] + Type.TABLE_SPLIT.value) for i in range(self.__col)]

        # resolve split
        split = self.__split[:]
        [split.__setitem__(i, Type.TABLE.value + Type.TABLE_SPLIT.value) for i in range(self.__row)]

        # resolve table
        table = self.__table[:]
        [table[i].__setitem__(j, table[i][j] if table[i][j].endswith(
            Type.TABLE_SPLIT.value) else table[i][j] + Type.TABLE_SPLIT.value)
         for i in range(self.__row) for j in range(self.__col)]

        # list to str
        def table_handler(x, y):
            for col in y:
                x += col
            x += Type.SEP.value
            return x

        head = reduce(lambda x, y: x + y, head) + Type.SEP.value
        split = reduce(lambda x, y: x + y, split) + Type.SEP.value
        table = reduce(table_handler, table, "")

        return head + split + table

    def resize(self, row: int = None, col: int = None):
        if not isinstance(row, int):
            raise TypeError(f"row: {row} type is not int")

        if not isinstance(col, int):
            raise TypeError(f"col: {col} type is not int")

        row = self.__row if not row or row < 0 else row
        col = self.__col if not col or col < 0 else col

        head = [''] * col
        split = [self.SPLIT_SYMBOL] * col
        table = [[''] * col for _ in range(row)]

        # reset head
        [head.__setitem__(i, self.__head[i]) for i in range(self.__col if self.__col < col else col)]

        # reset split

        # reset table
        [table[i].__setitem__(j, self.__table[i][j])
         for i in range(self.__row if self.__row < row else row)
         for j in range(self.__col if self.__col < col else col)]

        self.__set_row(row)
        self.__set_col(col)
        self.__head = head
        self.__split = split
        self.__table = table

    def head(self, head: list) -> None:
        if not isinstance(head, list):
            raise TypeError(f"head: {head} type is not list")

        if len(head) > self.__col:
            raise ValueError(f"head: {head} length must be lower than or equal to {self.__col}")

        [self.__head.__setitem__(i, head[i]) for i in range(len(head))]

    def set_head(self, col: int = 0, text: str = '') -> None:
        if not isinstance(col, int):
            raise TypeError(f"col: {col} type is not int")

        if not isinstance(text, str):
            raise TypeError(f"text: {text} type is not str")

        if col >= self.__col or col < 0:
            raise ValueError(f"col {col} must be 0~{self.__col - 1}")

        self.__head[col] = text

    def set_value(self, row: int = 0, col: int = 0, value: str = '') -> None:
        if not isinstance(row, int):
            raise TypeError(f"row: {row} type is not int")

        if not isinstance(col, int):
            raise TypeError(f"col: {col} type is not int")

        if not isinstance(value, str):
            raise TypeError(f"value: {value} type is not str")

        if row < 0:
            raise ValueError(f"row {row} must be larger than or equal to 0")

        if col >= self.__col or col < 0:
            raise ValueError(f"col {col} must be 0~{self.__col - 1}")

        self.__table[row][col] = value
