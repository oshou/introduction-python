import os

EXTENSION_MAP = {
    'py': 'python',
    'md': 'markdown',
    'markdown': 'markdown'
}


def find_extension(filepath):
    path, ext = os.path.splitext(filepath)
    return EXTENSION_MAP.get(ext.lstrip('.'), 'NONE')
