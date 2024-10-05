import os

trash = '__pycache__'
utiltrash = f'utils/{trash}'
def DeleteTrash():
    if os.path.exists(trash):os.system(f"rm -r {trash}")
    if os.path.exists(utiltrash):os.system(f"rm -r {utiltrash}")
