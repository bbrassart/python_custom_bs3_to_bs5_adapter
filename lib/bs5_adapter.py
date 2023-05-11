import sys
import errno


def replace_text_in_file(input_file, search_text, replace_text):
    with open(input_file, "r") as file:
        content = file.read()

    modified_content = content.replace(search_text, replace_text)
    print("Replacement completed.")
    return modified_content


def process_file(input_file):
    try:
        extension = input_file.split(".")[-1].lower()
        output_file = "{input_file}_bs5.{extension}".format(
            input_file=input_file, extension=extension
        )
        allowed_extensions = ["slim", "html", "jsx", "tsx"]

        if extension in allowed_extensions:
            modified_content = replace_text_in_file(
                input_file, "margin-top-small", "mt-15"
            )
            if modified_content:
                with open(output_file, "w") as file:
                    file.write(modified_content)
            else:
                print("No content to write to output file.")
        else:
            print(
                "Unsupported file extension: {extension}. Only .slim, .html, and .jsx files are supported."
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
