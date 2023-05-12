import sys
import errno
import json
import re


def replace_text_in_file(input_file):
    predefined_classes_file = open("bs3_to_bs5_class_correspondance.json")
    predefined_classes = json.load(predefined_classes_file)

    with open(input_file, "r") as file:
        content = file.read()

    for class_name, replacement in predefined_classes.items():
        pattern = r'(?<=[.\s\'"])' + re.escape(class_name)  # Regex pattern to match word preceded by ., space, ' or "
        content = re.sub(pattern, replacement, content)

    with open(input_file, "w") as file:
        file.write(content)

    print("Replacement completed for {}.".format(input_file))


def process_file(input_files):
    if isinstance(input_files, str):
        input_files = [input_files] # convert a single file to a list

    for input_file in input_files:
        try:
            extension = input_file.split(".")[-1].lower()
            allowed_extensions = ["slim", "html", "js", "jsx", "tsx"]

            if extension in allowed_extensions:
                replace_text_in_file(input_file)
            else:
                print(
                    "Unsupported file extension for {}: {}. Only .slim, .html, .js and .jsx files are supported.".format(
                        input_file, extension
                 )
                )
        except EnvironmentError as err:
            if err.errno == errno.ENOENT:  # ENOENT = No entity
                print("File {} not found.".format(input_file))
            else:
                raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_text.py <input_file>")
    else:
        input_file = sys.argv[1:]
        process_file(input_file)
