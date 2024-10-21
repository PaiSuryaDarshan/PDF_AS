import sys
import os
import Annotation_marking_Segregate as AM_S

if sys.platform == 'darwin':
    LIT_REV_DIR = "/Users/pai.suryadarshan/Desktop/Academics/Year_3/(3000 word) Lit. Rev"
if sys.platform == 'win32':
    LIT_REV_DIR = "D:\iCloudDrive\Desktop\Academics\\Desktop\Academics\Year_3\(3000 word) Lit. Rev"

SORTED_DIR = sorted(os.listdir(LIT_REV_DIR))

for index, filename in enumerate(SORTED_DIR):
    options = str(index) + " ====> " + filename
    print(options)

print(os.listdir(LIT_REV_DIR))

# papername = ""

# pdf_path = LIT_REV_DIR + '\ '.strip() + papername

# list_of_extracts = AM_S.complete_function(pdf_path)

# MOTIVATION_Yel  = list_of_extracts[0] 
# METHODS_Grn     = list_of_extracts[1] 
# CONTEXT_Blu     = list_of_extracts[2] 
# RESULTS_Pur     = list_of_extracts[3] 
# UNKNOWN_FUNC_Pin= list_of_extracts[4] 
# FUTURE_red      = list_of_extracts[5]   
# INTERPRETATION_Ora= list_of_extracts[6] 
# TITLE_Bla       = list_of_extracts[7] 
# UNKNOWN_FUNC_Gra= list_of_extracts[8] 
# UNKNOWN_FUNC_LBl= list_of_extracts[9] 

# AM_S.Segregate(".\Extracts\_0_TITLE.txt",   TITLE_Bla)                    
# AM_S.Segregate(".\Extracts\_1_MOTIVATION.txt", MOTIVATION_Yel)                    
# AM_S.Segregate(".\Extracts\_2_METHODS.txt", METHODS_Grn)                    
# AM_S.Segregate(".\Extracts\_3_CONTEXT.txt", CONTEXT_Blu)                    
# AM_S.Segregate(".\Extracts\_4_RESULTS.txt", RESULTS_Pur)                    
# AM_S.Segregate(".\Extracts\_5_INTERPRETATION.txt", INTERPRETATION_Ora)                    
# AM_S.Segregate(".\Extracts\_6_FUTURE.txt", FUTURE_red)                    

# ----------------------------------------------------------------
#* REFERENCE FOR DEVELOPER
# ----------------------------------------------------------------

# list_of_extracts is in the order
# yellow, green, blue, purple, pink, red, orange, black, gray, light_blue