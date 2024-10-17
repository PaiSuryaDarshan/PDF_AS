import Annotation_marking_Segregate as AM_S

pdf_path = "D:\iCloudDrive\Desktop\Academics\Year_3\Lab\SC Papers\(Onder_Peckan) Effect of temperature on Gelation properties.pdf"
# pdf_path = "C:/Users/surya/Downloads/p1_(Song_Jian).pdf"

list_of_extracts = AM_S.complete_function(pdf_path)

WHAT_Yel    = list_of_extracts[0] 
WHY_Grn     = list_of_extracts[1] 
EXPECT_Blu  = list_of_extracts[2] 
# UNKNOWN_FUNC_Pur     = list_of_extracts[3] 
# UNKNOWN_FUNC_Pin     = list_of_extracts[4] 
How_red     = list_of_extracts[5]   
TITLE_Bla   = list_of_extracts[6] 
# UNKNOWN_FUNC_Gra     = list_of_extracts[7] 
# UNKNOWN_FUNC_LBl     = list_of_extracts[8] 

AM_S.Segregate(".\Extracts\_0_TITLE.txt", TITLE_Bla)                    
AM_S.Segregate(".\Extracts\What.txt", WHAT_Yel)                    
AM_S.Segregate(".\Extracts\Why.txt", WHY_Grn)                    
AM_S.Segregate(".\Extracts\How.txt", How_red)                    

# ----------------------------------------------------------------
# REFERENCE FOR DEVELOPER
# ----------------------------------------------------------------

# list_of_extracts is in the order
# yellow, green, blue, purple, pink, orange, black, gray, light_blue