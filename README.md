# python_custom_bs3_to_bs5_adapter
A small Python script written with the help of GPT and CoPilot. The script takes one or more file paths as input and overwrite the original content of the files. converting Bootstrap 3 classes to Bootstrap 5.
Note that this script also adds correspondance to a lot of classes that do not exist in BS3. The script has been used in a particular context, in which there were a lot of custom classes built on top 
of Bootstrap 3.

# What does this script do?
You can run one or multiple template files - such as a JSX, JS, SLIM or HTML file - through the script. It replaces the detected Bootstrap 3 classes for their Bootstrap 5 classes' correspondance.
It also lets you know if a Bootstrap 3 class is deprecated and does not have a BS5 counterpart.

# ChatGPT reviewed description of the script
* It holds a dictionary of BS3 to BS5 class correspondance in a JSON file called `lib/bs3_to_bs5_class_correspondance.json`
* The script takes as argument one or multiple file paths
* The `#replace_text_in_file` function reads the content of input files.
* Given the provided correspondance, it iterates through each key-value pair in the dictionary and replaces all occurrences of the keys (predefined BS3 classes) with their corresponding values (replacement BS5 classes) in the content.
* The modified content is then written back to the same input file, overwriting the original content.
* The `#process_file` function checks the file extension of input files. If the extension is .slim, .js, .html, or .jsx, it calls the `#replace_text_in_file` function to perform the replacement and overwrite input files.
* If the file extension is not supported, a message is displayed indicating the unsupported extension.
* If the input file is not found, an appropriate error message is displayed.
* When the script is executed, it checks if a command-line argument specifying the input file is provided. If not, it displays a usage message.

# How to run a file through it
* Fork the repo in your machine
* In your terminal, just type from the root level of the script (`/lib` folder): `python bs5_adapter.py <path_to_your_first_template_file> <path_to_your_second_template_file>`
* Check modified templates in your favorite IDE to see, adapt and validate the changes.

