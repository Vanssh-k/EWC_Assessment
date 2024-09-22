from constant import shipmentKeyMap

def calculate_white_space(page_rect, group_bbox, text_areas, current_index):
    whitespace = {}
    closest_right, closest_below = None, None

    for i, (text, bbox) in enumerate(text_areas):
        if i == current_index:
            continue
        
        if bbox.y0 >= group_bbox.y1 and (closest_below is None or bbox.y0 < closest_below.y0):
            closest_below = bbox
        
        if bbox.y0 == group_bbox.y0 and bbox.x0 >= group_bbox.x1 and (closest_right is None or bbox.x0 < closest_right.x0):
            closest_right = bbox

    whitespace["below"] = closest_below.y0 - group_bbox.y1 if closest_below else page_rect.y1 - group_bbox.y1
    
    if closest_right:
        whitespace["right"] = closest_right.x0 - group_bbox.x1
    else:
        whitespace["right"] = page_rect.x1 - group_bbox.x1

    return whitespace


def clean_text_preserving_whitespace(text):
    lines = text.splitlines()
    cleaned_lines = [line for line in lines if line.strip() != '']  
    return "\n".join(cleaned_lines)


def get_json_value(json_object, label):
    key = shipmentKeyMap.get(label)
    if key is None:
        return None

    path = key.split('.')
    value = json_object.get(path[0]);
    
    for segment in path[1:]:
        if isinstance(value, str):
            return value
        elif isinstance(value, dict):
            value = value.get(segment)
        elif isinstance(value, list):
            index = int(segment)
            if index < len(value):
                value = value[index]
            else:
                return None
        else:
            return None
        
        if value is None:
            return None
    
    return value
