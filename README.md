# EWC Assessment Repository

Welcome to the EWC Assessment repository! This project demonstrates an approach to fill in PDF with Json object data with the help of Statement Transformers and PYMUPDF.

## Project Overview

The layout understanding and fields extraction of the PDF is done using the PYMUPDF. Once the fields are extracted the data of the Json so processed from the Statement Trasnformers are mapped to the most apt field and then the said field is filled in the PDF using the Json data.

## Installation Instructions

1. Clone this repository:
git clone https://github.com/Vanssh-k/AbsintheLabs_Task.git

2. Install dependencies:
pip install pymupdf sentence-transformers scikit-learn numpy

3. Start the development server:
python3 ./src/main.py