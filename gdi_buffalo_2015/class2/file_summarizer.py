
import os
import pandas as pd

if __name__ == "__main__":
    files_data = []

    for temp_file in os.listdir('.'):
       files_data.append(temp_file)

    dataframe = pd.DataFrame(files_data)
    dataframe.to_excel("fileSummaries.xlsx")

# what does listdir('.') do? which library is to_excel in?
