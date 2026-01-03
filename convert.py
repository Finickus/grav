import os
import re

# Define replacements
replacements = {
    'has-text-centered': 'text-center',
    'is-primary': 'bg-primary',
    'is-info': 'bg-info',
    'is-warning': 'bg-warning',
    'is-danger': 'bg-danger',
    'is-success': 'bg-success',
    'is-secondary': 'bg-secondary',
    'is-bold': 'fw-bold',
    'box': 'card',
    'columns': 'row',
    'column is-half': 'col-md-6',
    'column is-4-tablet': 'col-lg-3',
    'column is-6-tablet': 'col-lg-6',
    'column is-3-tablet': 'col-lg-4',
    'column is-12': 'col-12',
    'column is-8': 'col-8',
    'column is-4': 'col-4',
    'column is-6': 'col-6',
    'column is-7': 'col-7',
    'column is-5': 'col-5',
    'column is-9': 'col-9',
    'column is-one-third': 'col-md-4',
    'column is-one-sixth': 'col-md-2',
    'column is-half-desktop': 'col-lg-6',
    'column is-full-tablet': 'col-md-12',
    'column is-12-tablet': 'col-md-12',
    'column is-8-desktop': 'col-lg-8',
    'column is-4-desktop': 'col-lg-4',
    'column is-6-desktop': 'col-lg-6',
    'column is-5-desktop': 'col-lg-5',
    'button is-': 'btn btn-',
    ' is-large': ' btn-lg',
    ' is-fullwidth': ' w-100',
    ' is-outlined': ' btn-outline-',
    'hero is-': 'div class="bg-',
    'has-background-': 'bg-',
    'card-header has-background-': 'card-header bg-',
    'notification is-': 'div class="alert alert-',
    ' is-light': '',
    'is-rounded': 'rounded',
    'is-striped': '',
    'is-bordered': '',
    'is-fullwidth': '',
    'is-hoverable': '',
    'table is-': 'table ',
    ' is-multiline': '',
    ' is-centered': '',
    ' is-vcentered': '',
    ' is-variable is-6': '',
    ' is-mobile is-centered': '',
    ' is-mobile': '',
    ' has-shadow': ' shadow',
    ' mb-5': ' mb-4',
    ' mt-5': ' mt-4',
    ' mt-6': ' mt-5',
    ' mb-6': ' mb-5',
    'title is-1': 'display-1',
    'title is-2': 'display-2',
    'title is-3': 'display-3',
    'title is-4': 'display-4',
    'title is-5': 'display-5',
    'title is-6': 'display-6',
    'subtitle is-1': 'h2 display-1',
    'subtitle is-2': 'h2 display-2',
    'subtitle is-3': 'h2 display-3',
    'subtitle is-4': 'h2 display-4',
    'subtitle is-5': 'h2 display-5',
    'subtitle is-6': 'h2 display-6',
    'is-size-1': 'fs-1',
    'is-size-2': 'fs-2',
    'is-size-3': 'fs-3',
    'is-size-4': 'fs-4',
    'is-size-5': 'fs-5',
    'is-size-6': 'fs-6',
    'is-size-7': 'fs-7',
    'has-text-white': 'text-white',
    'has-text-dark': 'text-dark',
    'has-text-primary': 'text-primary',
    'has-text-info': 'text-info',
    'has-text-warning': 'text-warning',
    'has-text-danger': 'text-danger',
    'has-text-success': 'text-success',
    'has-text-grey': 'text-muted',
    'is-widescreen': '',
    'mr-2': 'me-2',
    'mr-3': 'me-3',
    'ml-0': 'ms-0',
    'ml-4': 'ms-4',
    'mt-4': 'mt-4',
    'mb-4': 'mb-4',
    'p-4': 'p-4',
    'py-5': 'py-5',
    'px-4': 'px-4',
}

def convert_file(filepath):
    print(f"Converting {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Walk the directory
count = 0
for root, dirs, files in os.walk('user/bludit'):
    for file in files:
        if file == 'index.txt':
            filepath = os.path.join(root, file)
            convert_file(filepath)
            count += 1

print(f"Conversion completed for {count} files.")
