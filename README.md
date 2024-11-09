# Wikilinks-Generator-HTML
## Overview
**WikiLinkGenerator** is a Python-based tool designed to streamline the process of adding Wikipedia links to your HTML files. By generating HTML `<a>` tags that link to the most relevant Wikipedia articles based on your search terms, WikiLinkGenerator simplifies the task of enhancing your web content with authoritative references. Additionally, it integrates seamlessly with [Keysmith](https://www.keysmithapp.com/) on macOS, allowing for quick and easy access through customizable keyboard shortcuts.

[[[[[[METTRE LE GIF]]]]]]

## Features

- **Multi-Language Support:** Search and generate links from Wikipedia in various languages.
- **Command-Line Interface:** Easily integrate into scripts and automation workflows.
- **Modular Design:** Import functions into your Python projects for flexible usage.
- **HTML Tag Generation:** Automatically create `<a>` tags with appropriate href attributes.
- **Integration with Keysmith:** Enhance productivity by assigning keyboard shortcuts on macOS.
- **Error Handling:** Gracefully handles network issues and invalid inputs.

## Installation

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### As a Command-Line Tool

You can use Wikilinks-Generator-HTML directly from the command line to generate HTML `<a>` tags.

```bash
python3 wiki_link_generator.py "Search Term" --lang en
```

**Example:**

```bash
python3 wiki_link_generator.py "Artificial Intelligence" --lang en
```

**Output:**

```html
<a href="https://en.wikipedia.org/wiki/Artificial_intelligence">Artificial Intelligence</a>
```

**Parameters:**

- `Search Term` (required): The term you want to search on Wikipedia.
- `--lang` or `-l` (optional): The language code for Wikipedia (default is `en` for English).

**Supported Language Codes:**

- `en` - English
- `fr` - French
- `es` - Spanish
- `de` - German
- ... and many more.

### As an Imported Module

You can integrate Wikilinks-Generator-HTML into your Python projects by importing its functions.

```python
from wiki_link_generator import get_wikipedia_first_link, generate_html_a_tag

search_term = "Machine Learning"
language = "en"

url = get_wikipedia_first_link(search_term, language)
if url:
    html_tag = generate_html_a_tag(url, search_term)
    print(html_tag)
else:
    print(search_term)
```

## Integration with Keysmith on macOS

To enhance your workflow, you can integrate WikiLinkGenerator with [Keysmith](https://www.keysmithapp.com/) on macOS. This allows you to generate Wikipedia links quickly using keyboard shortcuts.

### Steps to Integrate

1. **Ensure WikiLinkGenerator is Installed:**
   - Follow the [Installation](#installation) section to set up WikiLinkGenerator.

2. **Create a Python Script:**
   - Save the following script as `generate_wiki_link.py` in your preferred directory (e.g., `/Users/yourusername/scripts/`).

   ```python
   #!/usr/bin/env python3
   import sys
   from wiki_link_generator import get_wikipedia_first_link, generate_html_a_tag

   def main():
       if len(sys.argv) < 2:
           print("Usage: generate_wiki_link.py \"Search Term\" [language_code]")
           sys.exit(1)
       
       search_term = sys.argv[1]
       lang = sys.argv[2] if len(sys.argv) >= 3 else 'en'
       
       url = get_wikipedia_first_link(search_term, lang)
       if url:
           html_tag = generate_html_a_tag(url, search_term)
           print(html_tag)
       else:
           print(search_term)

   if __name__ == "__main__":
       main()
   ```

3. **Make the Script Executable:**

   ```bash
   chmod +x /Users/yourusername/scripts/generate_wiki_link.py
   ```

4. **Set Up Keysmith:**
   - Open **Keysmith** on your Mac.
   - Create a new **Snippet** or **Command**.
   - **Trigger:** Assign a keyboard shortcut (e.g., `Cmd + Shift + W`).
   - **Action:** Configure to execute the Python script with the current clipboard text as an argument.

   **Example Command:**

   ```bash
   /Users/yourusername/scripts/generate_wiki_link.py "$(pbpaste)" fr | pbcopy
   ```

   **Explanation:**
   - `$(pbpaste)`: Retrieves the current clipboard text.
   - `fr`: Specifies the language code (French in this case). Omit or change as needed.
   - `| pbcopy`: Copies the generated HTML `<a>` tag back to the clipboard.

5. **Usage:**
   - **Copy** the text you want to convert into a Wikipedia link.
   - **Press** the assigned keyboard shortcut (`Cmd + Shift + W`).
   - The clipboard now contains the HTML `<a>` tag.
   - **Paste** the HTML tag wherever needed.

**Example Workflow:**

1. **Copy Text:**
   - Copy `Intelligence Artificielle` to the clipboard.

2. **Trigger Keysmith Shortcut:**
   - Press `Cmd + Shift + W`.

3. **Result:**
   - Clipboard now contains:
     ```html
     <a href="https://fr.wikipedia.org/wiki/Intelligence_artificielle">Intelligence Artificielle</a>
     ```
   - A notification (if configured) may inform you of the successful operation.

## License

This project is licensed not under the MIT License.

---

### 📚 Additional Resources

- [Keysmith Documentation](https://www.keysmithapp.com/docs/)
- [Python Official Website](https://www.python.org/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/en/latest/)

---

### 🧩 Integration with Other Projects

WikiLinkGenerator's modular design allows for easy integration into various projects:

- **Web Applications:** Dynamically generate Wikipedia links based on user input.
- **Documentation Automation:** Enhance documentation by linking to relevant Wikipedia articles.
- **Chatbots and Virtual Assistants:** Provide authoritative references in responses.
- **Content Management Systems:** Automatically enrich content with Wikipedia links.

Feel free to customize and extend WikiLinkGenerator to fit your specific needs!