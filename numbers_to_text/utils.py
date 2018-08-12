def reversed_split_into_chunks(iterable, size: int) -> list:
    for i in range(len(iterable), 0, -size):
        yield iterable[max(i - size, 0):i]