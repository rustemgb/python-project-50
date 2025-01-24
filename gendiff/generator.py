def generator(file1, file2):

    all_key = sorted(file1.keys() | file2.keys())
    deleted = file1.keys() - file2.keys()
    added = file2.keys() - file1.keys()
    result = []

    for key in all_key:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in added:
            result.append(f"  + {key}: {value2}")
        elif key in deleted:
            result.append(f"  - {key}: {value1}")

        else:
            if value1 != value2:
                result.append(f"  - {key}: {value1}")
                result.append(f"  + {key}: {value2}")
            else:
                result.append(f"    {key}: {value2}")
                
    return ('{\n' + '\n'.join(result) + '\n}').lower()