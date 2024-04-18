from bs4 import BeautifulSoup

def merge_files(html_file, js_file, css_file, output_file):
    with open(html_file, 'r') as f:
        html_content = f.read()

    with open(js_file, 'r') as f:
        js_content = f.read()

    with open(css_file, 'r') as f:
        css_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the head tag and insert CSS content
    head_tag = soup.find('head')
    if head_tag:
        style_tag = soup.new_tag('style')
        style_tag.string = css_content
        head_tag.append(style_tag)

    # Find the body tag and insert JavaScript content
    body_tag = soup.find('body')
    if body_tag:
        script_tag = soup.new_tag('script')
        script_tag.string = js_content
        body_tag.append(script_tag)

    # Write the modified HTML to the output file
    with open(output_file, 'w') as f:
        f.write(str(soup))

# Usage example:
merge_files('index.html', 'mathnotepad.min.js', 'mathnotepad.min.css', 'merged.html')
