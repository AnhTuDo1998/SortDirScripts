import os
import shutil
import argparse
import fnmatch

"""
    This Python script is to sort files in a folders into categories, where each category is a subdir in the output dir
    path. 
    
    To customise the ext file to sort, add in the ext format below.
"""
parser = argparse.ArgumentParser(description=" This script sort the target folder's files into Documents, Pictures, ..."
                                             "Videos, Music, Executables and Others depending on the extension of file")
parser.add_argument("input_dir", help="Directory to be sorted", type=str)
parser.add_argument("-o", "--output_dir", type=str, help=" Output path to store Documents, Videos,...")

# define a list of ext for the categories needed to be sorted. To be added on
document_ext = ['Documents', '.pdf', '.xls', '.xlsx', '.doc', '.docx', '.ppt', '.pptx', '.txt']
audio_ext = ['Music', '.mp3', '.wma', '.wav']
photo_ext = ['Pictures', '.jpeg', '.jpg', '.bmp', '.gif', '.png', '.cr2']
video_ext = ['Videos', '.m4v', '.mp4', '.mov', '.mpg', '.mpeg']
exe_ext = ['Executables', '.exe']
ext_list = [document_ext, audio_ext, photo_ext, video_ext, exe_ext]

# define the directories name to store the result in
dir_list = ['Documents', 'Pictures', 'Videos', 'Music', 'Executables', 'Others']


# Helper function to create directories to sort into
def create_dir(output_dir):
    for dir_name in dir_list:
        try:
            os.mkdir(output_dir + '/' + dir_name + '/')
            print("Created" + dir_name)
        except FileExistsError as exc:
            # print(exc)
            continue


# Sort files into directories
def sort_dir(input_dir, output_dir):
    done_match_file_ext = False
    files = os.scandir(input_dir)
    for file in files:
        if file.is_file():
            # print(file)
            for list_of_ext in ext_list:
                if done_match_file_ext:
                    done_match_file_ext = False
                    break
                for ext in list_of_ext:
                    # print(ext)
                    if fnmatch.fnmatch(file.name, "*" + ext):
                        print(file.name + " detected as" + " " + list_of_ext[0])
                        shutil.move(input_dir + '/' + file.name, output_dir + '/' + list_of_ext[0] + '/')
                        print("Moved to " + list_of_ext[0])
                        done_match_file_ext = True
                        break
            try:
                print("File category is unclear")
                shutil.move(input_dir + '/' + file.name, output_dir + '/' + 'Others' + '/')
                print("Moved to Others")
            except shutil.Error:
                continue


def main():
    args = parser.parse_args()
    input_dir = args.input_dir
    output_dir = args.output_dir
    create_dir(output_dir)
    sort_dir(input_dir, output_dir)


if __name__ == '__main__':
    main()
