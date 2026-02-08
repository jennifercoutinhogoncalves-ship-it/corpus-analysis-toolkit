# Corpus Linguistics with Python: Final Project
# Summer Semester 2024
# Jennifer Coutinho Goncalves - 1001682


# ------------------ EXAMPLE SCRIPT --------------------------------

import module_CL_jennifer_coutinho_goncalves
from nltk.corpus import gutenberg

gutenberg_files = gutenberg.fileids()

# 1. Corpora Statistics
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 1. CORPORA STATISTICS " + "*" * 40 + "\n" + "-" * 104)                             # get better overview            
module_CL_jennifer_coutinho_goncalves.corpora_statistics(gutenberg_files)
#module_CL_jennifer_coutinho_goncalves.corpora_statistics_words(gutenberg_files)                                                # preprocessed tokens

# 2. Term Frequency
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 2. TERM FREQUENCY " + "*" * 40 + "\n" + "-" * 104)                                
fdist_global = module_CL_jennifer_coutinho_goncalves.term_frequency(gutenberg_files)
module_CL_jennifer_coutinho_goncalves.term_frequency_visualisation(fdist_global)

# 3. Type-Token Ratio
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 3. TYPE-TOKEN RATIO " + "*" * 40 + "\n" + "-" * 104)                           
module_CL_jennifer_coutinho_goncalves.type_token_ratio(gutenberg_files)
#module_CL_jennifer_coutinho_goncalves.type_token_ratio_all(gutenberg_files)                                                    # tokens not preprocessed


# 4. N-Gram Analysis
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 4. N-GRAM ANALYSIS " + "*" * 40 + "\n" + "-" * 104) 
module_CL_jennifer_coutinho_goncalves.ngram_analysis(gutenberg_files)


# 5. Concordance
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 5. CONCORDANCE " + "*" * 40 + "\n" + "-" * 104) 
module_CL_jennifer_coutinho_goncalves.concordance(gutenberg_files)


# 6. Collocations / Multiword Expressions
print("\n" + "-" * 122 + "\n" + "*" * 40 + " 6. COLLOCATIONS / MULTIWORD EXPRESSIONS " + "*" * 40 + "\n" + "-" * 122) 
module_CL_jennifer_coutinho_goncalves.collocations(gutenberg_files)


# 7. Unique Word List
print("\n" + "-" * 104 + "\n" + "*" * 40 + " 7. UNIQUE WORD LISTS " + "*" * 40 + "\n" + "-" * 104) 
module_CL_jennifer_coutinho_goncalves.unique_word_list(gutenberg_files)
