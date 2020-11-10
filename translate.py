'''
Python data translating + formatting tool
Research by Gordon Johnson '21
with help from Kasey McFadden '22

Authentication Setup
https://cloud.google.com/docs/authentication/getting-started

export GOOGLE_APPLICATION_CREDENTIALS="[PATH]"
e.g. export GOOGLE_APPLICATION_CREDENTIALS="/Users/kaseym/Desktop/translateKey.json"
'''

import pandas as pd
from google.cloud import translate_v2 as translate

# Converts csv file f to a dataframe, calls translateText 
# with items in column number colNum, adds a column called 
# 'Translated' that contains translated text, returns dataframe.
def addTransColumn(f, colNum, target):
    df = pd.read_csv(f)
    column = df.columns[colNum]
    col = df[column]
    
    transList = []
    for item in col:
        transList.append(translateText(item, target))
    
    df['Translated'] = transList
    return df

# translates text to target language
def translateText(text, target):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)

    # print(u"Text: {}".format(result["input"]))
    # print(u"Translation: {}".format(result["translatedText"]))
    # print(u"Detected source language: {}".format(result["detectedSourceLanguage"]))
    return result["translatedText"]

def main():
    # # # # # # # # # # # # # # # # # # # # # # # # #
    target = "en"         # target language
    f = 'sample.csv'      # csv input file name
    colNum = 0            # column number to translate
    outFile = 'out.csv'   # chosen name of output file
    # # # # # # # # # # # # # # # # # # # # # # # # #
    df = addTransColumn(f, colNum, target)
    print(df)
    df.to_csv(outFile)

if __name__ == '__main__':
    main()