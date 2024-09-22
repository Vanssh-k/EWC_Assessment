from pdf_processing import get_text_blocks_with_whitespace, finding_checkbox_question, populating_pdf_with_json_data, get_shape_area
from os.path import dirname, join
current_dir = dirname(__file__)

pdf_path = join(current_dir, "../US-commercial-invoice.pdf")
output_pdf_path = join(current_dir,  "../output_modified.pdf")

x0, y0, x1, y1 = get_shape_area(pdf_path);
custom_bbox = (x0, y0, x1, y1);

texts, coords, white_spaces, checkboxes = get_text_blocks_with_whitespace(pdf_path, custom_bbox)

checkbox_question_indices, checkbox_qa_link = finding_checkbox_question(checkboxes, coords, texts)

populating_pdf_with_json_data(pdf_path, output_pdf_path, texts, coords, white_spaces, checkboxes, checkbox_question_indices, checkbox_qa_link)


