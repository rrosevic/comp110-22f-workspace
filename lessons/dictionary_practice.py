"""In-class code-writing practice."""


def zip(ks: list[str], vs: list[str]) -> dict[str, str]:
    assert len(ks) == len(vs)
    result: dict[str, str] = {}
    for i in range(0, len(ks)):
        result[ks[i]] = vs[i]
    return result