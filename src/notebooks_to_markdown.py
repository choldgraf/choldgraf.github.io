from subprocess import check_call
import os
from glob import glob
import nbformat as nbf

POSTS_FOLDER = '../_posts/'
IMAGES_FOLDER = '../images/'
JUPYBLOG = os.path.expanduser('~/Dropbox/github/publicRepos/jupyterblog/jupyter_to_blog.py')
ipynb_files = glob('../notebooks/**/*.ipynb', recursive=True)
for ifile in ipynb_files:
    year = int(os.path.basename(ifile).split('-')[0])

    # Clean up the file before converting
    check_call(['python', JUPYBLOG, ifile, '--inplace'])

    # Run nbconvert moving it to the output folder
    build_call = '--FilesWriter.build_directory={}'.format(POSTS_FOLDER)
    images_call = '--NbConvertApp.output_files_dir={}'.format(os.path.join(IMAGES_FOLDER, str(year), 'ntbk'))
    check_call(['jupyter', 'nbconvert',
                '--to', 'markdown',
                images_call, build_call, ifile])
    
    # Read in the markdown and replace each image file with the site URL
    IMG_STRINGS = ['../../../images', '../../images']
    path_md = os.path.join(POSTS_FOLDER, os.path.basename(ifile).replace('.ipynb', '.md'))
    with open(path_md, 'r') as ff:
        lines = ff.readlines()
    for ii, line in enumerate(lines):
        for IMG_STRING in IMG_STRINGS:
            if IMG_STRING in line:
                line = line.replace(IMG_STRING, '{{ base.url }}/images')
                lines[ii] = line
    with open(path_md, 'w') as ff:
        ff.writelines(lines)
