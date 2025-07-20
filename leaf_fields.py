import statsapi

def extract_leaf_paths(data, path=""):
    """Recursively extract leaf-level field paths from nested JSON."""
    fields = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_path = f"{path}.{k}" if path else k
            fields.extend(extract_leaf_paths(v, new_path))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_path = f"{path}[{i}]"
            fields.extend(extract_leaf_paths(item, new_path))
    else:
        fields.append(path)
    return fields


def write_leaf_fields_to_file(json_data, output_file=None):
    """Extract leaf-level paths from JSON and write to a text file."""
    leaf_paths = extract_leaf_paths(json_data)
    if output_file is not None:
        with open(output_file, "w") as f:
            for path in leaf_paths:
                f.write(path + "\n")
        print(f"✅ Extracted {len(leaf_paths)} leaf fields to {output_file}")

boxscore = statsapi.get("game_boxscore", {'gamePk': 777103})
write_leaf_fields_to_file(boxscore,output_file="boxscore_fields.txt")