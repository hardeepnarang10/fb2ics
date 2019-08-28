from os import listdir, path


def target_file(resources_path, instruction_string):

    # List all files in resources_path folder.
    files_in_res_folder = listdir(resources_path)

    # Split filename and extension into tuples. Append these tuples into ext list object.
    ext_list = []
    for each_file in files_in_res_folder:
        ext_list.append(path.splitext(each_file))               # Returns tuple (filename, extension) in each iteration.

    # Check for HTML files in resources_path folder.
    num_of_html_files = (str(ext_list).lower().count(".html"))
    if num_of_html_files < 1:
        print("\nNo HTML file found in '" + resources_path.strip(".\\") + "' folder.")
        print(instruction_string)
        exit(-1)
    elif num_of_html_files > 1:
        print("\nMany HTML files found in '" + resources_path.strip(".\\") + "' folder.")                                   ################ Specify through args ###########
        print("\nMake sure only the webpage with saved facebook birthdays information is placed in the '" + resources_path.strip(".\\") + "' folder.")
        exit(-1)

    # Return target HTML file (to scrape birthday info from) with relative path.
    for each_tuple in ext_list:
        if ".html" in str(each_tuple).lower():
            target_file = each_tuple[0] + each_tuple[1]
            relative_target_path = resources_path + "\\" + target_file
            return relative_target_path
