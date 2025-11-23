import json
from decimal import Decimal

def pretty_json(value, indent=2, _level=0):
	pad = ' ' * (indent * _level)
	pad_next = ' ' * (indent * (_level + 1))

	# dict
	if isinstance(value, dict):
		if not value:
			return '{}'
		items = []
		for k, v in value.items():
			items.append(f"{pad_next}{json.dumps(k, ensure_ascii=False)}: {pretty_json(v, indent, _level+1)}")
		return '{\n' + ',\n'.join(items) + '\n' + pad + '}'

	# list
	if isinstance(value, list):
		if not value:
			return '[]'
		items = [f"{pad_next}{pretty_json(v, indent, _level+1)}" for v in value]
		return '[\n' + ',\n'.join(items) + '\n' + pad + ']'

	# booleans
	if isinstance(value, bool):
		return 'true' if value else 'false'

	# null
	if value is None:
		return 'null'

	# Decimal (from json.loads with parse_float)
	if isinstance(value, Decimal):
		# format without scientific notation
		return format(value, 'f')

	# float
	if isinstance(value, float):
		return format(value, 'f')

	# int
	if isinstance(value, int):
		return str(value)

	# string
	if isinstance(value, str):
		return json.dumps(value, ensure_ascii=False)

	# fallback
	return json.dumps(value, ensure_ascii=False)