# 10
coordinates: dict = {'x': 52, 'y': 18}
text: str = 'coordinates: ({x}, {y})'
print(text.format_map(coordinates))