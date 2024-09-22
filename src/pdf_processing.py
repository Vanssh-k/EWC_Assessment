import fitz 
from constant import json, english_keys
from utils import calculate_white_space, clean_text_preserving_whitespace, get_json_value
from json_mapping import find_most_similar_sentence, find_similarity

def get_text_blocks_with_whitespace(pdf_path, custom_bbox):
    doc = fitz.open(pdf_path)    
    texts, coords, white_spaces, checkboxes = [], [], [], []
    custom_rect = fitz.Rect(custom_bbox)

    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        print(f"\nProcessing Page {page_num + 1} within custom rectangle: {custom_rect}")
        
        text_instances = page.get_text("dict")['blocks']
        text_areas = [] 
        
        for block in text_instances:
            if 'lines' in block:
                for line in block['lines']:
                    for span in line['spans']:
                        text = clean_text_preserving_whitespace(span['text']);
                        
                        if text and text != '0' and len(text) < 50 and len(text) != 1:
                            bbox = fitz.Rect(span['bbox'])
                            
                            if custom_rect.intersects(bbox):
                                text_areas.append((text, bbox))
                                
        
        text_areas.sort(key=lambda item: (item[1].y0, item[1].x0)) 
        
        for i, (text, bbox) in enumerate(text_areas):
            texts.append(text)
            coords.append(bbox)
            white_spaces.append(calculate_white_space(custom_rect, bbox, text_areas, i))
            checkboxes.append(text.startswith(' '))
    
    doc.close()
    
    return texts, coords, white_spaces, checkboxes

def finding_checkbox_question(checkboxes, coords, texts):
    checkbox_question_indices = [False] * len(texts) 
    checkbox_qa_link = [-1] * len(texts);
    value = False;

    for index, checkbox in enumerate(checkboxes):
        if(checkbox == True):
            if(value != checkbox):
                checkbox_coord = coords[index]
                
                search_rect = fitz.Rect(
                 checkbox_coord.x0 - 20,  
                 checkbox_coord.y0 - 12,  
                 checkbox_coord.x1,        
                 checkbox_coord.y0          
                )
                
                for i, (text, coord) in enumerate(zip(texts, coords)):
                 if search_rect.intersects(coord):  
                     checkbox_question_indices[i] = True 
                     break 
            checkbox_qa_link[index] = i;
        value = checkbox;

    return checkbox_question_indices, checkbox_qa_link

def populating_pdf_with_json_data(pdf_path, output_pdf_path, texts, coords, white_spaces, checkboxes, checkbox_question_indices, checkbox_qa_link): 
    doc = fitz.open(pdf_path)
    page = doc.load_page(0)
    MINIMUM_SPACE_BELOW = 5

    for index, (text, coord, whitespace, checkbox, checkbox_question_indice) in enumerate(zip(texts, coords, white_spaces, checkboxes, checkbox_question_indices)):
        if not checkbox:
            if not checkbox_question_indice:
                most_similar_sentence, similarity_score = find_most_similar_sentence(text, english_keys)
                value = str(get_json_value(json, most_similar_sentence) or "")
            
                text_width = len(text) * 2

                insertion_x = coord.x1 + 5  
                insertion_y = coord.y0  
            
                if whitespace["below"] > whitespace["right"]:  
                    insertion_x = coord.x0  
                    insertion_y = coord.y1 + 7  
                elif whitespace["right"] < text_width and whitespace["below"] >= MINIMUM_SPACE_BELOW:
                    insertion_x = coord.x0  
                    insertion_y = coord.y1 + 7  
                else : 
                    insertion_x = coord.x1 + 5 
                    insertion_y = coord.y1 
                

                page.insert_text((insertion_x, insertion_y), value, fontsize=10, color=(0, 0, 0))
            else:
                most_similar_sentence, similarity_score = find_most_similar_sentence(text, english_keys)
                value = get_json_value(json, most_similar_sentence)
                similarity = 0
                y = -1;
                for i, answers in enumerate(checkbox_qa_link):
                    if(answers == index):
                        s = find_similarity(value, texts[i])
                        if(s > similarity):
                            similarity = s
                            y = i;

                answer_coord = coords[y];

                tick_x = answer_coord.x0 - 12  
                tick_y = answer_coord.y0 + 19 
        
                tick_mark = "✓"
                page.insert_text((tick_x, tick_y), tick_mark, fontsize=50, color=(0, 0, 0))
        
                print(f"Tick mark inserted for text: {texts[y]} at position ({tick_x}, {tick_y})")
    
    
    doc.save(output_pdf_path)
    doc.close()
    print(f"Values populated in PDF and saved as '{output_pdf_path}'.")