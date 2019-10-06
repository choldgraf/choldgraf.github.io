import os
import os.path as op
import shutil as sh
from glob import glob
from jupyter_book.build import SUPPORTED_FILE_SUFFIXES
from jupyter_book.page import page_html, write_page
from jupyter_book.page.page import page_css, page_js
from jupyter_book.utils import load_ntbk
import jupytext as jpt
from tqdm import tqdm


SITE_ROOT = op.join(op.dirname(op.abspath(__file__)), '..')
POSTS_FOLDER = os.path.join(SITE_ROOT, '_posts')
DRAFTS_FOLDER = os.path.join(SITE_ROOT, '_drafts')
IMAGES_FOLDER ='images'
REPLACE = False
all_files = glob(os.path.join(SITE_ROOT, 'content/**/*.*'), recursive=True)
all_files += glob(os.path.join(SITE_ROOT, 'drafts/**/*.*'), recursive=True)
skipped_files = []

# Update the CSS and JS with the latest jupyter-book values
with open(op.join(SITE_ROOT, 'assets', 'js', 'jupyterbook.js'), 'w') as ff:
    ff.write(page_js())

with open(op.join(SITE_ROOT, 'assets', 'css', 'jupyterbook.css'), 'w') as ff:
    ff.write(page_css())

for ifile in tqdm(all_files):
    file_name, suff = op.splitext(op.basename(ifile))
    if suff not in SUPPORTED_FILE_SUFFIXES:
        # Just copy over the file and continue
        sh.copy2(ifile, os.path.join(POSTS_FOLDER, op.basename(ifile)))
        continue

    path_new = op.join(POSTS_FOLDER, file_name + '.html')

    # If we don't want to replace files, just skip
    if REPLACE is False and op.exists(path_new):
        skipped_files.append(ifile)
        continue

    # Read in file with jupytext
    ntbk = load_ntbk(ifile)
    yaml_extra = ntbk['metadata'].get('yaml_header', '')
    markdown = '\n'.join([cell.source for cell in ntbk.cells if cell['cell_type'] == "markdown"])
    teaser = ' '.join(markdown.split(' ')[:100]).replace('\n', ' ')
    teaser = ''.join(char for char in teaser if char.lower() not in "#:/'\"\\")

    # Convert the notebook to HTML
    html, resources = page_html(ntbk, name=file_name, execute_dir=None)

    # Update the yaml frontmatter
    yaml = f'---\n{yaml_extra}\nexcerpt: "{teaser}"\n---\n'

    # Build the final HTML
    html = f"{yaml}\n\n{html}"

    # Write the HTML to disk
    out_folder = POSTS_FOLDER if f'posts{os.sep}' in ifile else DRAFTS_FOLDER
    path_html = write_page(html, out_folder, resources)
