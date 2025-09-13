def read_text_file(file_path: str) -> str:
    """Reads text from a file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def validate_input(input_text: str) -> bool:
    """Validates the provided input text to ensure it meets the necessary criteria."""
    if not input_text or len(input_text.strip()) == 0:
        return False
    if len(input_text) > 5000:  # Example limit for input text length
        return False
    return True