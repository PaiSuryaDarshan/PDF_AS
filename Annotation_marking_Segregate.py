import fitz # PyMuPDF

# Pre-requisites
pdf_path = ""
color_lower_limit = ""
color_upper_limit = ""

def is_highlight_color(color, lower_bound, upper_bound):
    # Convert color to RGB i.e scale from [0,1] to [0, 255]
    r = color[0]*255
    g = color[1]*255
    b = color[2]*225

    return (lower_bound[0] <= r <= upper_bound[0] and 
            lower_bound[1] <= g <= upper_bound[1] and
            lower_bound[2] <= b <= upper_bound[2])

def extract_annotations_by_color(pdf_path, color_lower_limit, color_upper_limit):
    # Open the PDF document
    pdf_doc = fitz.open(pdf_path)
    all_extracted_contents_for_test_run = []
    extracted_content = []
    color_annot_for_test_run = []

    # Define color bounds
    lower_bound = color_lower_limit
    upper_bound = color_upper_limit

    # Iterate over all pages
    for page_number in range(len(pdf_doc)):
        page = pdf_doc[page_number]
        # Iterate over each annotation made within that page
        for annot in page.annots():
            # Retrieve color of annotation
            all_extracted_contents_for_test_run.append(annot.info)
            color_annot = annot.colors["stroke"]
            # Check if it meets bounds
            if is_highlight_color(color_annot, lower_bound, upper_bound):
                # Extract relevant information about annotation
                # Add points to contours of the highlights
                points = annot.vertices
                # create a quad using these points
                try:
                    quad = fitz.Quad(points)
                    clipper_shape = quad.rect
                except Exception as e:
                    # print(e)
                    clipper_shape = annot.rect

                ht = (f"Page {page_number + 1}: ") + page.get_text("text", clip=clipper_shape)
                # Add to list of extracted content
                extracted_content.append(ht)
            color_annot_for_test_run.append(color_annot)

    pdf_doc.close()
    # return extracted_content, all_extracted_contents_for_test_run, color_annot_for_test_run
    return extracted_content

def complete_function(pdf_path):
    # Yellow Highlight
    # & yellow_target = (255, 255, 0)
    yellow_lower_bound = (204, 204, 0)
    yellow_upper_bound = (255, 255, 51)
    yellow_extract = extract_annotations_by_color(pdf_path, yellow_lower_bound, yellow_upper_bound)

    # Green Highlight
    # & green_target = (0, 255, 0)  #! Light Green
    green_lower_bound = (100, 120, 100)
    green_upper_bound = (200, 255, 200)
    green_extract = extract_annotations_by_color(pdf_path, green_lower_bound, green_upper_bound)

    # Blue Highlight
    # & blue_target = (0, 0, 255)
    blue_lower_bound = (0, 0, 204)
    blue_upper_bound = (51, 51, 255)
    blue_extract = extract_annotations_by_color(pdf_path, blue_lower_bound, blue_upper_bound)

    # Purple Highlight
    # & purple_target = (128, 0, 128)
    purple_lower_bound = (102, 0, 102)
    purple_upper_bound = (153, 51, 153)
    purple_extract = extract_annotations_by_color(pdf_path, purple_lower_bound, purple_upper_bound)

    # Pink Highlight
    # & pink_target = (255, 192, 203)
    pink_lower_bound = (204, 153, 178)
    pink_upper_bound = (255, 204, 255)
    pink_extract = extract_annotations_by_color(pdf_path, pink_lower_bound, pink_upper_bound)

    # Orange Highlight
    # & orange_target = (255, 165, 0)
    orange_lower_bound = (204, 130, 0)
    orange_upper_bound = (255, 195, 51)
    orange_extract = extract_annotations_by_color(pdf_path, orange_lower_bound, orange_upper_bound)

    # Black Highlight
    # & black_target = (0, 0, 0)
    black_lower_bound = (0, 0, 0)
    black_upper_bound = (51, 51, 51)
    black_extract = extract_annotations_by_color(pdf_path, black_lower_bound, black_upper_bound)

    # Gray Highlight
    # & gray_target = (128, 128, 128)
    gray_lower_bound = (102, 102, 102)
    gray_upper_bound = (153, 153, 153)
    gray_extract = extract_annotations_by_color(pdf_path, gray_lower_bound, gray_upper_bound)

    # Light Blue Highlight
    # & light_blue_target = (173, 216, 230)
    light_blue_lower_bound = (50, 180, 200)
    light_blue_upper_bound = (200, 230, 255)
    light_blue_extract = extract_annotations_by_color(pdf_path, light_blue_lower_bound, light_blue_upper_bound)

    return (
        yellow_extract,
        green_extract,
        blue_extract,
        purple_extract,
        pink_extract,
        orange_extract,
        black_extract,
        gray_extract,
        light_blue_extract
        )

def Segregate(file, col):
    f = open(file, 'w')
    color_of_interest = col
    for i in color_of_interest:
        # fix buggy PDF formatting
        f.write(i)
    f.close()