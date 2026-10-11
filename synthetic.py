"""Synthetic non-production arithmetic for harness adoption acceptance."""


def add(left: int, right: int) -> int:
    if isinstance(left, bool) or isinstance(right, bool):
        raise TypeError("boolean inputs are not arithmetic integers")
    if not isinstance(left, int) or not isinstance(right, int):
        raise TypeError("integer inputs required")
    return left + right
