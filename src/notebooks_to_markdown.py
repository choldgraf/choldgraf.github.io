from subprocess import check_call
import numpy as np
import os
import os.path as op
import shutil as sh
from glob import glob
import nbformat as nbf
from nbclean import NotebookCleaner

SITE_ROOT = os.path.expanduser('~/github/publicRepos/choldgraf.github.io')
TEMPLATE_PATH = os.path.expanduser('~/github/publicRepos/choldgraf.github.io/assets/templates/jekyllmd.tpl')
POSTS_FOLDER = os.path.join(SITE_ROOT, '_posts')
IMAGES_FOLDER ='images'
REPLACE = False
ipynb_files = glob(os.path.join(SITE_ROOT, 'notebooks/**/*.ipynb'), recursive=True)
markdown_files = glob(os.path.join(SITE_ROOT, 'notebooks/**/*.md'), recursive=True)
if REPLACE is False:
    new_ipynb_files = [ii for ii in ipynb_files
                       if not os.path.exists(os.path.join(POSTS_FOLDER, os.path.basename(ii).replace('.ipynb', '.md')))]
    print("Skipping {} ipynb files".format(len(ipynb_files) - len(new_ipynb_files)))
    ipynb_files = new_ipynb_files

for ifile in ipynb_files:
    filename = op.basename(ifile).replace('.ipynb', '')
    ifile_tmp = ifile+'_TMP'
    year = int(os.path.basename(ifile).split('-')[0])

    # Clean up the file before converting
    cleaner = NotebookCleaner(ifile)
    cleaner.remove_cells(empty=True)
    cleaner.remove_cells(tag='hidden')
    cleaner.clear('stderr')
    cleaner.save(ifile_tmp)

    # Run nbconvert moving it to the output folder
    build_call = '--FilesWriter.build_directory={}'.format(POSTS_FOLDER)
    images_call = '--NbConvertApp.output_files_dir={}'.format(os.path.join('..', IMAGES_FOLDER, str(year), 'ntbk'))
    check_call(['jupyter', 'nbconvert',
                '--to', 'markdown', '--template', TEMPLATE_PATH,
                images_call, build_call, ifile_tmp])
    os.remove(ifile_tmp)
    
    # Read in the markdown and replace each image file with the site URL
    IMG_STRINGS = ['../../../images', '../../images']
    path_md = os.path.join(POSTS_FOLDER, os.path.basename(ifile).replace('.ipynb', '.md'))
    with open(path_md, 'r') as ff:
        lines = ff.readlines()
    for ii, line in enumerate(lines):
        for IMG_STRING in IMG_STRINGS:
            line = line.replace(IMG_STRING, '{{ base.url }}/images')
        lines[ii] = line

    # Define a featured image if images exist
    images_files = glob(op.join(IMAGES_FOLDER, str(year), 'ntbk', '{}*.png'.format(filename)))
    if len(images_files) > 0:
        featured_line = [ii for ii in lines if 'featured_image' in ii]
        if len(featured_line) > 0:
            featured_ix = int(featured_line[0].split(':')[-1].strip())
        else:
            featured_ix = 0
        image_nums = [float('{}.{}'.format(ii.split('_')[-2], ii.split('_')[-1].replace('.png', '')))
                      for ii in images_files]
        ixs_sorted = np.argsort(image_nums)
        featured_image = images_files[ixs_sorted[featured_ix]]
        ix_yaml_start = lines.index('---\n', 0)
        lines.insert(ix_yaml_start +1, 'image: "/{}"\n'.format(featured_image))

    # Write back to disk
    with open(path_md, 'w') as ff:
        ff.writelines(lines)

# Copy the markdown files
print('Copying {} markdown files'.format(len(markdown_files)))
for ifile in markdown_files:
    file_name = os.path.basename(ifile)
    sh.copy2(ifile, os.path.join(POSTS_FOLDER, file_name))
