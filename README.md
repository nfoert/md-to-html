# md-to-html

A simple script which turns a markdown file with html and adds a fully customizable header and footer above and below it. Useful for quickly creating styled html emails by only editing one markdown file

## Installation

First, clone this repository:
```bash
git clone https://github.com/nfoert/md-to-html
cd md-to-html
```

Next, create a python virtual environment and activate it (linux shown here)
```bash
python -m venv .venv
source ./.venv/bin/activate
```

Next, install the required dependencies
```bash
pip install -r requirements.txt
```

# Usage

First, create `header.html`. Modify this file and `footer.html` to add your own header and footer if required. You can adjust the styles in `styles.py` to format the page how you wish.

Next, edit `body.md`. This will become the body of the document. You can use normal markdown formatting and it will all be converted as needed.

Finally, run the script using the following command. The final html file will be saved in the `output` directory
```bash
python main.py
```

## Development Usage

You can run the script using the `--dev` option, and the output will be saved to `index.html` in the current directory instead of `output`. This is useful for being able to reload the document and not have to adjust the file path if it outputs with different filenames.

```bash
python main.py --dev
```

