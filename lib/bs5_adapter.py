import sys
import errno


def replace_text_in_file(input_file):
    predefined_classes = {
        # Margins
        "margin-small": "m-15",
        "margin-top-small": "mt-15",
        "margin-bottom-small": "mb-15",
        "margin-left-small": "ms-15",
        "margin-right-small": "me-15",
        "margin-medium": "m-25",
        "margin-top-medium": "mt-25",
        "margin-bottom-medium": "mb-25",
        "margin-left-medium": "ms-25",
        "margin-right-medium": "me-25",
        "margin-large": "m-35",
        "margin-top-large": "mt-35",
        "margin-bottom-large": "mb-35",
        "margin-left-large": "ms-35",
        "margin-right-large": "me-35",
        "margin-xlarge": "m-48",
        "margin-top-xlarge": "mt-48",
        "margin-bottom-xlarge": "mb-48",
        "margin-left-xlarge": "ms-48",
        "margin-right-xlarge": "me-48",
        # Horizontal Margins
        "h-margin-small": "mx-15",
        "h-margin-medium": "mx-25",
        "h-margin-large": "mx-35",
        "h-margin-xlarge": "mx-48",
        # Vertical Margins
        "v-margin-small": "my-15",
        "v-margin-medium": "my-25",
        "v-margin-large": "my-35",
        "v-margin-xlarge": "my-48",
        # Paddings
        "padding-small": "p-15",
        "padding-top-small": "pt-15",
        "padding-bottom-small": "pb-15",
        "padding-left-small": "ps-15",
        "padding-right-small": "pe-15",
        "padding-medium": "p-25",
        "padding-top-medium": "pt-25",
        "padding-bottom-medium": "pb-25",
        "padding-left-medium": "ps-25",
        "padding-right-medium": "pe-25",
        "padding-large": "p-35",
        "padding-top-large": "pt-35",
        "padding-bottom-large": "pb-35",
        "padding-left-large": "ps-35",
        "padding-right-large": "pe-35",
        "padding-xlarge": "p-48",
        "padding-top-xlarge": "pt-48",
        "padding-bottom-xlarge": "pb-48",
        "padding-left-xlarge": "ps-48",
        "padding-right-xlarge": "pe-48",
        # Horizontal Paddings
        "h-padding-small": "px-15",
        "h-padding-medium": "px-25",
        "h-padding-large": "px-35",
        "h-padding-xlarge": "px-48",
        # Vertical Paddings
        "v-padding-small": "py-15",
        "v-padding-medium": "py-25",
        "v-padding-large": "py-35",
        "v-padding-xlarge": "py-48",
    }

    with open(input_file, "r") as file:
        content = file.read()

    for class_name, replacement in predefined_classes.items():
        content = content.replace(class_name, replacement)

    print("Replacement completed.")
    return content


def process_file(input_file):
    try:
        extension = input_file.split(".")[-1].lower()
        output_file = "{input_file}_bs5.{extension}".format(
            input_file=input_file, extension=extension
        )
        allowed_extensions = ["slim", "html", "jsx", "tsx"]

        if extension in allowed_extensions:
            modified_content = replace_text_in_file(input_file)
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
