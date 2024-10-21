# Python Translator

A Python-based language translator that uses an external API to translate text between different languages. This project demonstrates how to make API calls and handle translation using Python. Along with this, it shows how file I/O is handled within python by having it read and written to a .txt file.

## Features

- Translates text between english and spanish (by default).
- Supports multiple languages based on the translation API used.
- Uses file I/O in order to read and write files.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/KidronL/python-translator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-translator
   ```

3. Install required dependencies. This project uses the `requests` library to make API calls:

   ```bash
   pip install -r requirements.txt
   ```

4. Optional: If you would like to use a different translation service, please obtain an API key from a translation service (e.g., Google Translate API, DeepL API) and add it to your code. Documentation on this API can be found here (https://pypi.org/project/translate/)

## Usage

1. Open a terminal and navigate to the project directory.
2. Run the Python script:

   ```bash
   python translator.py
   ```

3. See the result in the **translated.txt** file.

## File Structure

```bash
├── translator.py         # The main script that handles translation
├── requirements.txt      # Lists the Python dependencies
└── README.md             # This file
```

## Future Improvements

- Add support for language detection.
- Add multi language support
- Implement a graphical user interface (GUI).
- Add error handling for unsupported languages and API errors.
