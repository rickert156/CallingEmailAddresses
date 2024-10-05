import os

trash = '__pycache__'
utiltrash = f'utils/{trash}'
temptrash = f'templates/{trash}'
sqltrash = f'sql/{trash}'
def DeleteTrash():
    if os.path.exists(trash):os.system(f"rm -r {trash}")
    if os.path.exists(utiltrash):os.system(f"rm -r {utiltrash}")
    if os.path.exists(sqltrash):os.system(f"rm -r {sqltrash}")
    if os.path.exists(temptrash):os.system(f"rm -r {temptrash}")
