from pathlib import Path
import sys

results = []


def get_dash_files_and_folders(rootfolder, results):
    for item in rootfolder.glob('*'):
        if item.name == 'clients.py':
            results.append(item)
        if not item.is_dir():
            continue
        if item.name == 'berserk':
            results.append(item)
    return results


for item in sys.path:
    item = Path(item)
    if not item.is_dir():
        continue
    results = get_dash_files_and_folders(item, results)

if results:
    print('Found following files & folders:')
    print(results)
else:
    print('No dash found in sys.path!')
