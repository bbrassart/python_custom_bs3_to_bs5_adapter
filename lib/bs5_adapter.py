import sys
import errno
import json


def replace_text_in_file(input_file):
    predefined_classes_file = open("bs3_to_bs5_class_correspondance.json")
    predefined_classes = json.load(predefined_classes_file)

    with open(input_file, "r") as file:
        content = file.read()

    for class_name, replacement in predefined_classes.items():
        content = content.replace(class_name, replacement)

    with open(input_file, "w") as file:
        file.write(content)

    print("Replacement completed.")

def process_file(input_file):
    try:
        extension = input_file.split(".")[-1].lower()
        allowed_extensions = ["slim", "html", "js", "jsx", "tsx"]

        if extension in allowed_extensions:
            replace_text_in_file(input_file)
        else:
            print(
                "Unsupported file extension: {extension}. Only .slim, .html, .js and .jsx files are supported."
            )
    except EnvironmentError as err:
        if err.errno == errno.ENOENT:  # ENOENT = No entity
            print("Input file not found.")
        else:
            raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python replace_text.py <input_file>")
    else:
        input_file = sys.argv[1]
        process_file(input_file)
