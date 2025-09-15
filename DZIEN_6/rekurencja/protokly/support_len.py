from typing import Protocol,runtime_checkable

@runtime_checkable
class SupportsLen(Protocol):
    def __len__(self) -> int: ...

def total_lenght(objs: list[SupportsLen]) -> int:
    return sum(len(o) for o in objs)

assert total_lenght(["abc",(1,2),{"x":1,"y":7}]) == 7
