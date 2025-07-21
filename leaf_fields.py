import statsapi
from pprint import pprint
import pandas as pd
import csv
from datetime import date


def extract_leaf_paths(data, path=""):
    """Recursively extract leaf-level field paths from nested JSON."""
    fields = []
    if isinstance(data, dict):
        for k, v in data.items():
            if k == "copyright":
                continue
            new_path = f"{path}.{k}" if path else k
            fields.extend(extract_leaf_paths(v, new_path))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            fields.extend(extract_leaf_paths(item, new_path))
    else:
        fields.append((path, data))
    return fields



def extract_leaf_fields(data, file=None):
    flat = extract_leaf_paths(data)
    summary = []

    max_depth = 0
    for path, values in flat:
        levels = path.split('.')
        max_depth = max(max_depth, len(levels))
        entry = {
                'field_path': path,
                'value': values if values else None,
                'data_type': type(values).__name__ if values else "None"
            }
        for i, level in enumerate(levels):
            entry[f'level_{i+1}'] = level
        summary.append(entry)

    # Ensure all rows have the same number of level columns
    for row in summary:
        for i in range(1, max_depth + 1):
            row.setdefault(f'level_{i}', None)
            
    if file is not None:
        df = pd.DataFrame(summary)
        df.to_csv(file, index=False)
        print(f"✅ Summary written to {file}")

endpoint = 'schedule'
# params = {'gamePk': 777103}
params = {'startDate':date.today(), 'endDate': date.today(), 'sportId': 1}
dataset = statsapi.get(endpoint, params)
extract_leaf_fields(dataset,file=f"{endpoint}_fields.csv")