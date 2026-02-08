
# Corpus Linguistics with Python: Final Project
# Summer Semester 2024
# Jennifer Coutinho Goncalves - 1001682

# -----------------------------------COMMENTS ----------------------------------------------------

# before using this module you will need to make sure you have installed NLTK and matplotlib
# just in case you have not, you will find a instruction in the following sections

# the term "global" refers to the entire corpus
# the term "local" refers to an individual document of the corpus

# if visualisations windwos are opened, please make sure that they are always closed afterwards 

# ------------------------ INSTALLING AND DOWNLOADING NLTK ---------------------------------------

# this module uses NLTK and BLA BLA. Before using it,it must be downloaded and installed

# go to your terminal and type:
# python3 -m pip install nltk

# import nltk

# to download the tools and corpora from NLTK, you can use the download method:
# nltk.download()

# ----------------------------- INSTALLING MATPLOTLIP --------------------------------------------

# !python3 -m pip install matplotlib   



# ---------------------------- DOCUMENTED PYTHON MODULE -------------------------------------------

# import any required modules

import os                               # import for directory paths
import re                               # import regex

from nltk import Text                   # import text
from nltk.text import Text              
from nltk import FreqDist               # import for term frequency calculation
from nltk import ngrams                 # import for n-gram analysis
from nltk import bigrams
from nltk import trigrams
from nltk.corpus import gutenberg       # import gutenberg corpus from nltk

import matplotlib.pyplot as plt         # import for visualisation


# Preprocess tokens

# This code defines a function named "preprocess".
# The preprocess function takes a list of tokens as input and processes it by converting it to lowercase. 
# This helps ensure consistency in the analysis by treating words with different cases as the same word. 
# Furthermore, it uses regex to exclude punctuation and other non-alphabetic characters.

# Function to preprocess the text

def preprocess(tokens):
    
    processed_tokens = []                                       # initialize list for preprocessed tokens
    
    for token in tokens:                                        # iterate over each token
        token = token.lower()                                   # convert into lowercase; providing more accurate term frequency analysis
        
        if re.match("^[a-z]+$", token):                         # only lowercase letters a-z; exclude punctuation
            processed_tokens.append(token)                      # append list 
            
    return processed_tokens



# 1. Corpora Statistics

# This code defines a function named "corpora_statistics", which computes and displays both local and global statistics for a collection of text files inthe Gutenberg corpus.
# The function iterates through each file, counting the total number of tokens and lines for each file, and then displays these counts for each file individually.
# After processing all the files, the function computes and displays the total number of documents, tokens, and lines across the entire corpus.

# I created two versions of the code because I wasn't certain if "tokens" should include punctuation or focus solely on words. 
# The first version counts all tokens, including punctuation, which seemed appropriate for general statistics.
# However, if the goal is to count only the words, the second function is more suitable.

# Function to compute corpora statistics

def corpora_statistics(gutenberg_files):

    # to get a better overview
    print("\n" + "-" * 88 + "\nLOCAL STATISTICS: Total number of tokens and lines in each file of the Gutenberg corpus\n" + "-" * 88 + "\n")
    

    token_global = 0                                 # initialize token count for global number of tokens 
    line_global = 0                                  # initialize line count for global number of line

    for gutenberg_file in gutenberg_files:           # iterate over each file in gutenberg corpus
        token = gutenberg.words(gutenberg_file)      # assign variable; access tokens

        f = gutenberg.open(gutenberg_file)           # open file
    
        line_local = 0                               # initialize line count for local number of lines 
    
        for line in f:                                   # iterate over each line in file 
            line_local += 1                              # increment by 1 for each line passed; compute local number of lines
        
        f.close()                                        # close file handler
    
        token_local = len(token)                         # assign varibale; compute number of local number of token
        token_global += token_local                      # compute global number of token
        line_global += line_local                        # compute global number of lines
    

# display statistics

# LOCAL STATISTICS
        print("Total number of tokens in file", '"' + gutenberg_file + '"', ":", token_local)      # display local number of tokens
        print("Total number of lines in file", '"' + gutenberg_file + '"', ":", line_local)        # display local number of lines
        print("\n")                                                                                # separate to get a better overview 
    

# GLOBAL STATISTICS
    # to get a better overview
    print("-" * 87 + "\nGLOBAL STATISTICS: Total number of documents, tokens and lines of the Gutenberg corpus\n" + "-" * 87 + "\n")

    # number of documents in the corpus
    number_gutenberg_files = len(gutenberg_files)                                 # assign variable; compute number of documents
    
    print("Total number of documents in the corpus:", number_gutenberg_files)     # display number of documents

    print("\nTotal number of tokens in the corpus:", token_global)                # display global number of tokens 
    print("\nTotal number of lines in the corpus:", line_global)                  # display global number of lines



# Same Code with preprocessed tokens, i.e. just words

def corpora_statistics_words(gutenberg_files):

    # to get a better overview
    print("\n" + "-" * 88 + "\nLOCAL STATISTICS: Total number of tokens and lines in each file of the Gutenberg corpus\n" + "-" * 88 + "\n")
    

    token_global = 0                                    # initialize token count for global number of tokens 
    line_global = 0                                     # initialize line count for global number of line

    for gutenberg_file in gutenberg_files:              # iterate over each file in gutenberg corpus
        token = gutenberg.words(gutenberg_file)         # assign variable; access tokens

        token = preprocess(token)                       # preprocess tokens

        f = gutenberg.open(gutenberg_file)              # open file
    
        line_local = 0                                  # initialize line count for local number of lines 
    
        for line in f:                                   # iterate over each line in file 
            line_local += 1                              # increment by 1 for each line passed; compute local number of lines
        
        f.close()                                        # close file handler
    
        token_local = len(token)                         # assign varibale; compute number of local number of token
        token_global += token_local                      # compute global number of token
        line_global += line_local                        # compute global number of lines
    

# display statistics

# LOCAL STATISTICS
        print("Total number of tokens in file", '"' + gutenberg_file + '"', ":", token_local)      # display local number of tokens
        print("Total number of lines in file", '"' + gutenberg_file + '"', ":", line_local)        # display local number of lines
        print("\n")                                                                                # separate to get a better overview 
    

# GLOBAL STATISTICS
    # to get a better overview
    print("-" * 87 + "\nGLOBAL STATISTICS: Total number of documents, tokens and lines of the Gutenberg corpus\n" + "-" * 87 + "\n")

    # number of documents in the corpus
    number_gutenberg_files = len(gutenberg_files)                                 # assign variable; compute number of documents
    
    print("Total number of documents in the corpus:", number_gutenberg_files)     # display number of documents

    print("\nTotal number of tokens in the corpus:", token_global)                # display global number of tokens 
    print("\nTotal number of lines in the corpus:", line_global)                  # display global number of lines



# 2. Term Frequency

# This code defines a function named "term_frequency".
# The term_frequency function calculates the frequency for each file in the Gutenberg corpus, as well as the frequency in the whole corpus.
# For each file, it gets the tokens, cleans them using the preprocess function, and then calculates how often each term is used using the FreqDist function.
# The computed frequencies are written to the output file "term_frequency_output.txt". 
# Finally, the function displays that the local and global term frequencies have been saved to the file.

# I didn't include a version without preprocessing because it makes more sense to focus solely on words for "term" frequency analysis.


# Function to calculate the term frequency

def term_frequency(gutenberg_files, output2="term_frequency_output_jennifer_coutinho_goncalves.txt"):
    
    fdist_global = FreqDist()

    with open(output2, "w") as fout:                            # open file for writing
        
        for gutenberg_file in gutenberg_files:                  # iterate over each file in gutenberg corpus
            
            tokens = gutenberg.words(gutenberg_file)            # assign avriable; create text object
            
            tokens = preprocess(tokens)                         # preprocess tokens 
            
            fdist = FreqDist(tokens)                            # compute frequency 
            
            fdist_global.update(fdist)                          # update global frequency 
        
            # LOCAL TERM FREQUENCY 
            print("-" * 80 + "\nThe Term Frequency in", '"' + gutenberg_file + '"\n' + "-" * 80, file=fout)                 # display file name; get a better overview 
            
            for word in fdist:                                                                                              # iterate over each word in fdist

                print("Word:", '"' + word + '"' + "\t" * 4 , "Absolute Frequency:", fdist[word], file = fout)               # display absolute frequency; get a better overview 
                print("\t" * 5, "Relative Frequency:", fdist.freq(word), "\n", file = fout)                                 # display relative frequency; get a better overview 
                
        
        # GLOBAL TERM FREQUENCY
        print("-" * 80 + "\nThe Global Term Frequency\n" + "-" * 80, file=fout)                                             # get a better overview 
        
        for word in fdist_global:

            print("Word:", '"' + word + '"' + "\t" * 5 , "Absolute Frequency:", fdist_global[word], file = fout)            # display absolute frequency; get a better overview 
            print("\t" * 6, "Relative Frequency:", fdist_global.freq(word), "\n", file = fout)                              # display relative frequency; get a better overview 
            

    # display that output is stored in output file
    print("\nThe local and global term frequencies were written to the file:", '"' + output2 + '"')                         # display where output is stored
    print("\nHere you can see where the file is located", os.getcwd())                                                      # get working directory 

    return fdist_global


# VISUALISATION OF TERM FREQUENCY

# This code defines two functions named "plot_top_terms" and "term_frequency_visualisation". 
# The plot_top_terms function extracts and preprocesses tokens and shows the top 20 most frequent terms. 
# The term_frequency_visualisation function displays a menu that allows the user to choose what should be visualized.
# Based on the user's input, the corresponding text's term frequency is plotted. 
# The loop continues until the user chooses to exit. 
# The visualisation window must also be closed. 


def plot_top_terms(gutenberg_file):

    tokens = gutenberg.words(gutenberg_file)                        # assign variable, access tokens
    tokens = preprocess(tokens)                                     # preprocess tokens 
    
    fdist = FreqDist(tokens)                                        # compute frequency

    fdist.plot(20, title="Top 20 Terms in " + gutenberg_file)       # show top 20 term of specified file



def term_frequency_visualisation(fdist_global):

    print("\nYou now have the option of visualising the top 20 most frequent words.")

    while True:                                                     # loop to repeat 
        print("\n--------------------------------------------")
        print("Choose which text you want to visualize:\n")
        print("1. austen-emma.txt")
        print("2. austen-persuasion.txt")
        print("3. austen-sense.txt")
        print("4. bible-kjv.txt")
        print("5. blake-poems.txt")
        print("6. bryant-stories.txt")
        print("7. burgess-busterbrown.txt")
        print("8. carroll-alice.txt")
        print("9. chesterton-ball.txt")
        print("10. chesterton-brown.txt")
        print("11. chesterton-thursday.txt")
        print("12. edgeworth-parents.txt")
        print("13. melville-moby_dick.txt")
        print("14. milton-paradise.txt")
        print("15. shakespeare-caesar.txt")
        print("16. shakespeare-hamlet.txt")
        print("17. shakespeare-macbeth.txt")
        print("18. whitman-leaves.txt")
        print("19. Global Frequency")
        print("20. exit")
        print("--------------------------------------------")

        # assign variable; input for user to choose an action
        user_choice = input("\nPlease choose which text you want to visualize (1-18) or type '19' for global or '20' to exit:")
        print("\n ! Please close the window with the visualisation in order to go on !")

        # loop depending on users choice
        if user_choice == "1": 
            plot_top_terms('austen-emma.txt')                               # visualize top 20 terms
        elif user_choice == "2": 
            plot_top_terms('austen-persuasion.txt')
        elif user_choice == "3": 
            plot_top_terms('austen-sense.txt')  
        elif user_choice == "4":
            plot_top_terms('bible-kjv.txt')
        elif user_choice == "5":
            plot_top_terms('blake-poems.txt')
        elif user_choice == "6":
            plot_top_terms('bryant-stories.txt')
        elif user_choice == "7":
            plot_top_terms('burgess-busterbrown.txt')
        elif user_choice == "8":
            plot_top_terms('carroll-alice.txt')
        elif user_choice == "9":
            plot_top_terms('chesterton-ball.txt')
        elif user_choice == "10":
            plot_top_terms('chesterton-brown.txt')
        elif user_choice == "11":
            plot_top_terms('chesterton-thursday.txt')
        elif user_choice == "12":
            plot_top_terms('edgeworth-parents.txt')
        elif user_choice == "13":
            plot_top_terms('melville-moby_dick.txt')
        elif user_choice == "14":
            plot_top_terms('milton-paradise.txt')
        elif user_choice == "15":
            plot_top_terms('shakespeare-caesar.txt')
        elif user_choice == "16":
            plot_top_terms('shakespeare-hamlet.txt')
        elif user_choice == "17":
            plot_top_terms('shakespeare-macbeth.txt')
        elif user_choice == "18":
            plot_top_terms('whitman-leaves.txt')
        elif user_choice == "19":
            fdist_global.plot(20)
        elif user_choice == "20":                                               # exit loop
            break
        else: 
            print("\nInvalid input. Please enter a number from 1 to 20.")       # handle invalid input



# 3. Type-Token Ratio

# This code defines a function named "type_token_ratio" that calculates the local and global Type-Token Ratio.
# For each file, it computes the types and tokens to compute the local type-token ratio and displays it.
# After processing all files, it computes the type-token ratio for the entire corpus by combining tokens from all files.

# I created two versions of the code because I wasn't certain if "tokens" should include punctuation or focus solely on words. 
# The first version uses preprocessed tokens as it seems appropriate for this type of calculation.
# However, if the goal is to count all tokens, the second function is more suitable.

# Function for computing the type-token ratio

def type_token_ratio(gutenberg_files):
    
    tokens_global = []                                              # initialize list to store all token

    # to get a better overview
    print("\n" + "-" * 88 + "\nLOCAL TYPE-TOKEN RATIO\n" + "-" * 88 + "\n")
    
    
    for gutenberg_file in gutenberg_files:                          # iterate over each file in gutenberg corpus
        tokens = gutenberg.words(gutenberg_file)                    # assign variable; access tokens

        tokens = preprocess(tokens)                                 # preprocess tokens
        
        types = set(tokens)                                         # get local unique words (types)
        
        num_tokens = len(tokens)                                    # compute local number of tokens
        num_types = len(types)                                      # compute local number of types
        
        ttr_local = num_types / num_tokens                          # compute local type-token ratio 
        
        # LOCAL TYPE-TOKEN RATIO
        print("Type-Token Ratio for file", '"' + gutenberg_file + '"', ":", ttr_local, "\n")         # display local type-token ratio
        
        tokens_global.extend(tokens)                                # add tokens to global list

    
    types_global = set(tokens_global)                               # get global unique words (types)
    
    num_tokens_global = len(tokens_global)                          # compute global number of tokens
    num_types_global = len(types_global)                            # compute global number of types
    
    ttr_global = num_types_global / num_tokens_global               # compute global type-token ratio

    # to get a better overview
    print("-" * 87 + "\nGLOBAL TYPE-TOKEN RATIO\n" + "-" * 87 + "\n") 
    
    # GLOBAL TYPE-TOKEN RATIO
    print("Global Type-Token Ratio:", ttr_global)                   # display global type-token ratio

    

# Same Code with all tokens, i.e. not preprocessed      

def type_token_ratio_all(gutenberg_files):
    
    tokens_global = []                                              # initialize list to store all token

    # to get a better overview
    print("\n" + "-" * 88 + "\nLOCAL TYPE-TOKEN RATIO\n" + "-" * 88 + "\n")
    
    
    for gutenberg_file in gutenberg_files:                          # iterate over each file in gutenberg corpus
        tokens = gutenberg.words(gutenberg_file)                    # assign variable; access tokens
        
        types = set(tokens)                                         # get local unique words (types)
        
        num_tokens = len(tokens)                                    # compute local number of tokens
        num_types = len(types)                                      # compute local number of types
        
        ttr_local = num_types / num_tokens                          # compute local type-token ratio 
        
        # LOCAL TYPE-TOKEN RATIO
        print("Type-Token Ratio for file", '"' + gutenberg_file + '"', ":", ttr_local, "\n")         # display local type-token ratio
        
        tokens_global.extend(tokens)                                # add tokens to global list

    
    types_global = set(tokens_global)                               # get global unique words (types)
    
    num_tokens_global = len(tokens_global)                          # compute global number of tokens
    num_types_global = len(types_global)                            # compute global number of types
    
    ttr_global = num_types_global / num_tokens_global               # compute global type-token ratio

    # to get a better overview
    print("-" * 87 + "\nGLOBAL TYPE-TOKEN RATIO\n" + "-" * 87 + "\n") 
    
    # GLOBAL TYPE-TOKEN RATIO
    print("Global Type-Token Ratio:", ttr_global)                   # display global type-token ratio


# 4. N-Gram Analysis

# This code defines a function named "ngram_analysis" that generates and saves local and global n-grams (unigrams, bigrams, and trigrams). 
# For each file, it extracts tokens, generates n-grams, and writes them to an output file.
# Then it combines tokens from all files to generate and save global n-grams
# A confirmation message is displayed that the lists have been saved to the file.
# Finally, the path were the output file is located is displayed.

# Function to generate ngrams 

def ngram_analysis(gutenberg_files, output4 = "ngrams_output_jennifer_coutinho_goncalves.txt"):
    
    with open(output4, "w") as fout:                                        # open file for writing

        # LOCAL NGRAMS
        print("-" * 80 + "\nLOCAL NGRAMS\n" + "-" * 80, file=fout)          # get a better overview
        
        for gutenberg_file in gutenberg_files:                              # iterate over each file in gutenberg corpus
            tokens = gutenberg.words(gutenberg_file)                        # assign variable; access tokens
            
            unigrams_local = list(ngrams(tokens, 1))                        # assign variable; generate local unigram
            bigrams_local = list(bigrams(tokens))                           # assign variable; generate local bigram
            trigrams_local = list(trigrams(tokens))                         # assign variable; generate local trigram
            
            print("\nUnigrams for:", gutenberg_file, file=fout)
            print(unigrams_local, file=fout)                                 # display local unigrams
            
            print("\nBigrams for:", gutenberg_file, file=fout)
            print(bigrams_local, file=fout)                                  # display local bigrams
            
            print("\nTrigrams for:", gutenberg_file, file=fout)
            print(trigrams_local, file=fout)                                 # display local trigrams
        

        # GLOBAL NGRAMS
        print("-" * 80 + "\nGLOBAL NGRAMS\n" + "-" * 80, file=fout)          # get a better overview

        all_tokens = []                                                      # initialize list to store all token
        
        for gutenberg_file in gutenberg_files:                               # iterate over each file in gutenberg corpus                              
            tokens = gutenberg.words(gutenberg_file)                         # assign variable; access tokens
            
            all_tokens.extend(tokens)                                        # append list
        
        unigrams_global = list(ngrams(all_tokens, 1))                        # assign variable; generate global unigram 
        bigrams_global = list(bigrams(all_tokens))                           # assign variable; generate global bigram
        trigrams_global = list(trigrams(all_tokens))                         # assign variable; generate global trigram
        
        print("\nGlobal Unigrams:", file=fout)
        print(unigrams_global, file=fout)                                     # display global unigrams
        
        print("\nGlobal Bigrams:", file=fout)
        print(bigrams_global, file=fout)                                      # display global bigrams
        
        print("\nGlobal Trigrams:", file=fout)
        print(trigrams_global, file=fout)                                     # display global trigrams

    print("\nThe ngrams were written to the file:", '"' + output4 + '"')      # display where output is stored
    print("\nHere you can see where the file is located", os.getcwd())        # get working directory 



# 5. Concordance

# This code defines a function named "concordance" that allows users to interactively generate and display the local and global concordance.
# The user is repeatedly asked to enter a word for which they want to see the concordance until they choose to exit.
# The user then has the choice of viewing the concordance in individual texts, all texts, or the entire corpus.
# The function then generates the chosen concordance for the specified word, and displays it.
# The loop continues until the user chooses to stop.
# This function allows the user to analyze how a particular word appears across different texts or the entire corpus.

# Function to access concordance

def concordance(gutenberg_files):
        
    while True:                                                                                                             # loop to repeat input
        # input for the user to choose a word for concordance
        user_word = input("\nEnter the WORD for which you want the concordance to be displayed or type 'exit' to quit: ")   # assign variable; access word for concordance
        
        if user_word.lower() == 'exit':                                                                                     # convert to lowercase
            break                                                                                                           # exit loop
        
        # display options
        print("\n----------------------------------------------------")
        print("Choose which concordance you want to be displayed:\n")
        print("1. austen-emma.txt")
        print("2. austen-persuasion.txt")
        print("3. austen-sense.txt")
        print("4. bible-kjv.txt")
        print("5. blake-poems.txt")
        print("6. bryant-stories.txt")
        print("7. burgess-busterbrown.txt")
        print("8. carroll-alice.txt")
        print("9. chesterton-ball.txt")
        print("10. chesterton-brown.txt")
        print("11. chesterton-thursday.txt")
        print("12. edgeworth-parents.txt")
        print("13. melville-moby_dick.txt")
        print("14. milton-paradise.txt")
        print("15. shakespeare-caesar.txt")
        print("16. shakespeare-hamlet.txt")
        print("17. shakespeare-macbeth.txt")
        print("18. whitman-leaves.txt")
        print("19. show concordance for all files individually")
        print("20. show concordance for the entire corpus")
        print("21. exit")
        print("----------------------------------------------------")

        # input for user to make a choice
        user_choice = input("\nPlease choose an option (1-21): ")                                                           # input choice

        # loop depending on users choice
        if user_choice == "1":
            tokens = gutenberg.words('austen-emma.txt')                                                                     # access token
            text = Text(tokens)                                                                                             # create text object
            print("\nConcordance for:", '"' + user_word + "'" + "in 'austen-emma.txt':")
            text.concordance(user_word)                                                                                     # display concordance
        elif user_choice == "2":
            tokens = gutenberg.words('austen-persuasion.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'austen-persuasion.txt':")
            text.concordance(user_word)
        elif user_choice == "3":
            tokens = gutenberg.words('austen-sense.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'austen-sense.txt':")
            text.concordance(user_word)
        elif user_choice == "4":
            tokens = gutenberg.words('bible-kjv.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'bible-kjv.txt':")
            text.concordance(user_word)
        elif user_choice == "5":
            tokens = gutenberg.words('blake-poems.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'blake-poems.txt':")
            text.concordance(user_word)
        elif user_choice == "6":
            tokens = gutenberg.words('bryant-stories.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'bryant-stories.txt':")
            text.concordance(user_word)
        elif user_choice == "7":
            tokens = gutenberg.words('burgess-busterbrown.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'burgess-busterbrown.txt':")
            text.concordance(user_word)
        elif user_choice == "8":
            tokens = gutenberg.words('carroll-alice.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'carroll-alice.txt':")
            text.concordance(user_word)
        elif user_choice == "9":
            tokens = gutenberg.words('chesterton-ball.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'chesterton-ball.txt':")
            text.concordance(user_word)
        elif user_choice == "10":
            tokens = gutenberg.words('chesterton-brown.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'chesterton-brown.txt':")
            text.concordance(user_word)
        elif user_choice == "11":
            tokens = gutenberg.words('chesterton-thursday.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'chesterton-thursday.txt':")
            text.concordance(user_word)
        elif user_choice == "12":
            tokens = gutenberg.words('edgeworth-parents.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'edgeworth-parents.txt':")
            text.concordance(user_word)
        elif user_choice == "13":
            tokens = gutenberg.words('melville-moby_dick.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'melville-moby_dick.txt':")
            text.concordance(user_word)
        elif user_choice == "14":
            tokens = gutenberg.words('milton-paradise.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'milton-paradise.txt':")
            text.concordance(user_word)
        elif user_choice == "15":
            tokens = gutenberg.words('shakespeare-caesar.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'shakespeare-caesar.txt':")
            text.concordance(user_word)
        elif user_choice == "16":
            tokens = gutenberg.words('shakespeare-hamlet.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'shakespeare-hamlet.txt':")
            text.concordance(user_word)
        elif user_choice == "17":
            tokens = gutenberg.words('shakespeare-macbeth.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'shakespeare-macbeth.txt':")
            text.concordance(user_word)
        elif user_choice == "18":
            tokens = gutenberg.words('whitman-leaves.txt')
            text = Text(tokens)
            print("\nConcordance for:", '"' + user_word + "'" + "in 'whitman-leaves.txt':")
            text.concordance(user_word)
            
        elif user_choice == "19":
            
            # concordance for all individual files
            for gutenberg_file in gutenberg_files:
                tokens = gutenberg.words(gutenberg_file)
                text = Text(tokens)

                print("\nConcordance for:", '"' + user_word + "'" + "in", '"' + gutenberg_file + '":')
                text.concordance(user_word)
                
        elif user_choice == "20":
            
            # concordance for the entire corpus
            all_tokens = []                                                                                 # initialize list to store all token
            
            for gutenberg_file in gutenberg_files:                                                          # iterate over each file in gutenberg corpus
                tokens = gutenberg.words(gutenberg_file)                                                    # assign variable; access tokens
                
                all_tokens.extend(tokens)                                                                   # append list
                
            text_corpus = Text(all_tokens)                                                                  # assign variable; create text object
            
            print("\nGlobal Concordance for" + '"' + user_word + "':")
            text_corpus.concordance(user_word)                                                              # display global concordance
            
        elif user_choice == "21":
            break                                                                                           # exit the loop
        else:
            print("\nInvalid input. Please enter a number from 1 to 21.")                                   # handle invalid input 



# 6. Collocations / Multiword Expressions

# This code defines a function named "collocations", which generates and displays local and global collocations.
# The function iterates through each file and generates and displays the collocations for each file individually.
# After processing all the files, it generates and displays the collocations for the entire corpus.

# Function to access collocations / multiword expression

def collocations(gutenberg_files):

    
    # LOCAL COLLOCATIONS
    print("-" * 80 + "\nLOCAL COLLOCATIONS\n" + "-" * 80)                   # get a better overview
    
    
    for gutenberg_file in gutenberg_files:                                  # iterate over each file in gutenberg corpus
        tokens = gutenberg.words(gutenberg_file)                            # assign variable; access tokens
        text = Text(tokens)                                                 # assign variable; create text object

        print("\nCollocations for", '"' + gutenberg_file + '"', ":\n")      
        text.collocations()                                                 # access and display collocations

    # GLOBAL COLLOCATIONS
    print("-" * 80 + "\nGLOBAL COLLOCATIONS\n" + "-" * 80)                  # get a better overview

    all_tokens = []                                                         # initialize list to store all token

    for gutenberg_file in gutenberg_files:                                  # iterate over each file in gutenberg corpus
        tokens = gutenberg.words(gutenberg_file)                            # assign variable; access tokens
        
        all_tokens.extend(tokens)                                           # append list

    text_corpus = Text(all_tokens)                                          # create text object

    print(f"\nGlobal Collocations:\n")
    text_corpus.collocations()                                              # display global collocations



# 7. Unique Word List

# This code defines a function named "unique_word_list", which generates and writes local and global unique word lists to an output file.
# The function opens an output file for writing.
# The function iterates through each file and creates a list of unique words to the output file for each file individually.
# After processing all the files, it creates a global list of unique words for the entire corpus.
# The unique words are sorted alphabetically, and a confirmation message is displayed that the lists have been saved to the file.
# Finally, the path were the output file is located is displayed.


# Function to generate unique word lists

def unique_word_list(gutenberg_files, output7="unique_word_list_output_jennifer_coutinho_goncalves.txt"):
    
    with open(output7, "w") as fout:                                            # open file for writing

        # LOCAL UNIQUE WORD LISTS
        print("-" * 80 + "\nLOCAL UNIQUE WORD LISTS\n" + "-" * 80, file=fout)   # get a better overview
        
        for gutenberg_file in gutenberg_files:                                  # iterate over each file in gutenberg corpus
            tokens = gutenberg.words(gutenberg_file)                            # assign variable; access tokens
            
            tokens = preprocess(tokens)                                         # assign variable; preprocess tokens
            
            unique_words = set(tokens)                                          # assign variable; access local unique words

            print("\nUnique Word List for", '"' + gutenberg_file + '"', ":\n", file=fout)
            
            for word in sorted(unique_words):                                   # sort alphabetically for a better overview
                print(word, file=fout)                                          # display local unique word lists in output file
                
        
        # GLOBAL UNIQUE WORD LIST
        print("-" * 80 + "\nGLOBAl UNIQUE WORD LIST\n" + "-" * 80, file=fout)   # get a better overview 
        
        all_tokens = []                                                         # initialize list to store all token                                              
        
        for gutenberg_file in gutenberg_files:                                  # iterate over each file in gutenberg corpus
            tokens = gutenberg.words(gutenberg_file)                            # assign variable; access tokens        
            
            tokens = preprocess(tokens)                                         # assign variable; preprocess tokens
            
            all_tokens.extend(tokens)                                           # append list
        
        unique_words_global = set(all_tokens)                                   # assign variable; access global unique words

        print("\nGlobal Unique Word List:\n", file=fout)                        # get a better overview
        
        for word in sorted(unique_words_global):                                # sort alphabetically for a better overview
            print(word, file = fout)                                            # display global unique word list in output

    print("\nThe local and global unique word lists were written to the file:", '"' + output7 + '"')        # display where output is stored 
    print("\nHere you can see where the file is located", os.getcwd())                                      # get working directory 

                       


