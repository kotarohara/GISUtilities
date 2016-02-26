# http://gis.stackexchange.com/questions/26257/how-can-i-iterate-over-map-layers-in-qgis-python
# layers = iface.legendInterface().layers()

# QgsMapLayerRegistry
# http://qgis.org/api/classQgsMapLayerRegistry.html
street_layer_name = "street_edge"
neighborhood_layer_name = "neighborhood"
street_layer = QgsMapLayerRegistry.instance().mapLayersByName(street_layer_name)[0]
neighborhood_layer = QgsMapLayerRegistry.instance().mapLayersByName(neighborhood_layer_name)[0]

# Using vector layer
# http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/vector.html
# Qgis Geometry
# http://qgis.org/api/classQgsGeometry.html
street_count = {}
distance = {}
for neighborhood in neighborhood_layer.getFeatures():
    neighborhood_id = neighborhood.attributes()[1]
    street_count[neighborhood_id] = 0
    distance[neighborhood_id] = 0
    for street in street_layer.getFeatures():
        if neighborhood.geometry().intersects(street.geometry()):
            distance[neighborhood_id] += street.geometry().length()
    break

print distance
"""
print street_count
{0: 284, 1: 244, 2: 83, 3: 130, 4: 45, 5: 81, 6: 91, 7: 99, 8: 161, 9: 156, 10: 102, 11: 275, 12: 88, 13: 112, 14: 34, 15: 128, 16: 137, 17: 326, 18: 102, 19: 147, 20: 158, 21: 77, 22: 179, 23: 152, 24: 78, 25: 94, 26: 76, 27: 87, 28: 258, 29: 64, 30: 77, 31: 243, 32: 78, 33: 127, 34: 134, 35: 76, 36: 78, 37: 132, 38: 70, 39: 122, 40: 57, 41: 247, 42: 46, 43: 68, 44: 61, 45: 85, 46: 160, 47: 183, 48: 52, 49: 61, 50: 69, 51: 58, 52: 35, 53: 82, 54: 138, 55: 124, 56: 26, 57: 97, 58: 60, 59: 108, 60: 52, 61: 135, 62: 66, 63: 84, 64: 33, 65: 60, 66: 61, 67: 41, 68: 38, 69: 35, 70: 50, 71: 44, 72: 163, 73: 59, 74: 121, 75: 44, 76: 53, 77: 49, 78: 124, 79: 40, 80: 94, 81: 163, 82: 90, 83: 120, 84: 23, 85: 90, 86: 92, 87: 56, 88: 41, 89: 82, 90: 87, 91: 91, 92: 64, 93: 79, 94: 60, 95: 115, 96: 12, 97: 92, 98: 105, 99: 74, 100: 77, 101: 61, 102: 61, 103: 38, 104: 53, 105: 95, 106: 75, 107: 124, 108: 70, 109: 61, 110: 33, 111: 97, 112: 54, 113: 105, 114: 75, 115: 80, 116: 45, 117: 184, 118: 75, 119: 120, 120: 127, 121: 36, 122: 70, 123: 72, 124: 61, 125: 428, 126: 89, 127: 78, 128: 153, 129: 50, 130: 57, 131: 62, 132: 49, 133: 113, 134: 85, 135: 85, 136: 110, 137: 56, 138: 83, 139: 65, 140: 81, 141: 39, 142: 47, 143: 65, 144: 109, 145: 73, 146: 114, 147: 94, 148: 70, 149: 103, 150: 87, 151: 44, 152: 50, 153: 84, 154: 140, 155: 54, 156: 106, 157: 236, 158: 110, 159: 103, 160: 26, 161: 163, 162: 31, 163: 80, 164: 134, 165: 33, 166: 44, 167: 320, 168: 58, 169: 86, 170: 50, 171: 148, 172: 77, 173: 57, 174: 84, 175: 17, 176: 26, 177: 79, 178: 95, 179: 41, 180: 34, 181: 86, 182: 56, 183: 56, 184: 67, 185: 54, 186: 38, 187: 30, 188: 37, 189: 45, 190: 29, 191: 55}
"""

    