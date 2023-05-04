import os
import glob


def select_lmzc_files(data_folder_path):
    # Get all XML files in the selected data folder
    xml_files = glob.glob(os.path.join(data_folder_path, "*.xml"))

    # Filter only the XML files with "LMZC" in the file name
    lmzc_files = [file for file in xml_files if "LMZC" in os.path.basename(file)]

    # Return the list of selected files
    return lmzc_files
