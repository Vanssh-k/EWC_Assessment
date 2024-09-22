from pdf_processing import get_text_blocks_with_whitespace, finding_checkbox_question, populating_pdf_with_json_data
from os.path import dirname, join
current_dir = dirname(__file__)


pdf_path = join(current_dir, "../US-commercial-invoice.pdf")
output_pdf_path = join(current_dir,  "../output_modified.pdf")

custom_bbox = (17.280000686645508, 99.96002197265625 , 594.7200317382812, 750.239990234375)

texts, coords, white_spaces, checkboxes = get_text_blocks_with_whitespace(pdf_path, custom_bbox)

checkbox_question_indices, checkbox_qa_link = finding_checkbox_question(checkboxes, coords, texts)

populating_pdf_with_json_data(pdf_path, output_pdf_path, texts, coords, white_spaces, checkboxes, checkbox_question_indices, checkbox_qa_link)


