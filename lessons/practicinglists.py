"""List diagram example."""

a: list[str] = ["one"]
b: list[str] = a
a.append("two")

print(b[1])