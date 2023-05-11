# python_custom_bs3_to_bs5_adapter
A small Python script written with the help of GPT and CoPilot. The script takes one file as input and spits out a formatted file.

# What does this script do?
You can run a template file - such as a JSX, SLIM or HTML file - through the script. It replaces the detected Bootstrap 3 classes for their Bootstrap 5 classes' correspondance.
It also sometimes let you know that a Bootstrap 3 class is deprecated and does not have a BS5 counterpart.

# ChatGPT reviewed description of the script
* It holds a dictionary of BS3 to BS5 class correspondance in a JSON file called `lib/bs3_to_bs5_class_correspondance.json`
* The script takes as argument a file path
* The `#replace_text_in_file` function reads the content of the input file.
* Given the provided correspondance, it iterates through each key-value pair in the dictionary and replaces all occurrences of the keys (predefined BS3 classes) with their corresponding values (replacement BS5 classes) in the content.
* The modified content is then written back to the same input file, overwriting the original content.
* The `#process_file` function checks the file extension of the input file. If the extension is .slim, .html, or .jsx, it calls the `#replace_text_in_file` function to perform the replacement and overwrite the input file.
* If the file extension is not supported, a message is displayed indicating the unsupported extension.
* If the input file is not found, an appropriate error message is displayed.
* When the script is executed, it checks if a command-line argument specifying the input file is provided. If not, it displays a usage message.

# How to run a file through it
* Fork the repo in your machine
* In your terminal, just type from the root level of the script (`/lib` folder): `python bs5_adapter.py <path_to_your_template_file>`
* Check the modified template in your favorite IDE to see the changes compared to the previous version.
