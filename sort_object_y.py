obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 
'phone': [90, 33], 'pen': [155, 100], 'mouse': [200, 45], 'remote': [298, 165], 'fan': [300, 36]}

sorted_objects = [(key, value) for key, value in sorted(obj_detected.items(), 
key=lambda item: item[1][1])]

for object_name, position in sorted_objects:
    print(object_name, position)
