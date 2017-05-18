r1 = {
	# x and y coordinates of the bottom-left corner of the rectangle
	'x': 2, 'y': 4,
	#width and height of rectangle
	'w': 5, 'h': 12 }

r2 = {
	'x': 4, 'y': 3,
	'w': 10, 'h': 10 }
r3 = {}

r3['x'] = max(r1['x'], r2['x'])
r3['y'] = max(r1['y'], r2['y'])
r3['w'] = min(r1['x']+r1['w'], r2['x']+r2['w']) - r3['x']
r3['h'] = min(r1['x']+r1['h'], r2['y']+r2['h']) - r3['y']

print(r3)