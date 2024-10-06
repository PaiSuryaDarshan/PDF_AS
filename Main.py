import Annotation_marking as AM

pdf_path = "D:/iCloudDrive/Desktop/Research Papers(2).pdf" 
# pdf_path = "C:/Users/surya/Downloads/p1_(Song_Jian).pdf"

list_of_extracts = AM.complete_function(pdf_path)

print(list_of_extracts[-1])

# ----------------------------------------------------------------
# REFERENCE FOR DEVELOPER
# ----------------------------------------------------------------

# list_of_extracts is in the order
# yellow, green, blue, purple, pink, orange, black, gray, light_blue