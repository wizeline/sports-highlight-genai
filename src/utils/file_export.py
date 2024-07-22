import os
import pandas as pd

def save_to_csv(dataframe, filename):
    """
    Save the DataFrame to a CSV file in the 'output_files' directory.
    
    :param dataframe: The DataFrame to save.
    :param filename: The name of the file (without path) to save the DataFrame.
    """
    # Ensure the 'output_files' directory exists
    if not os.path.exists('output_files'):
        os.makedirs('output_files')
    
    filepath = os.path.join('output_files', filename)
    dataframe.to_csv(filepath, index=False)
    print(f"DataFrame saved to {filepath}")

def save_to_excel(dataframe, filename):
    """
    Save the DataFrame to an Excel file in the 'output_files' directory.
    
    :param dataframe: The DataFrame to save.
    :param filename: The name of the file (without path) to save the DataFrame.
    """
    # Ensure the 'output_files' directory exists
    if not os.path.exists('output_files'):
        os.makedirs('output_files')
    
    filepath = os.path.join('output_files', filename)
    dataframe.to_excel(filepath, index=False)
    print(f"DataFrame saved to {filepath}")

def save_to_json(dataframe, filename):
    """
    Save the DataFrame to a JSON file in the 'output_files' directory.
    
    :param dataframe: The DataFrame to save.
    :param filename: The name of the file (without path) to save the DataFrame.
    """
    # Ensure the 'output_files' directory exists
    if not os.path.exists('output_files'):
        os.makedirs('output_files')
    
    filepath = os.path.join('output_files', filename)
    dataframe.to_json(filepath, orient='records', lines=True)
    print(f"DataFrame saved to {filepath}")
