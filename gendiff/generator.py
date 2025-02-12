def get_added_status(key, value):
    return {
        "status": "added",
        "key": key,
        "value": value,
    }


def get_deleted_status(key, value):
    return {
        "status": "deleted",
        "key": key,
        "value": value,
    }


def get_changed_status(key, value1, value2):
    return {
        "status": "changed",
        "key": key,
        "old_value": value1,
        "new_value": value2,
    }


def get_unchanged_status(key, value):
    return {
        "status": "unchanged",
        "key": key,
        "value": value,
    }


def get_nested_status(key, value1, value2):
    return {
        "status": "nested",
        "key": key,
        "children": generator(value1, value2),
    }


def generator(file1, file2):
    all_key = sorted(file1.keys() | file2.keys())
    deleted = file1.keys() - file2.keys()
    added = file2.keys() - file1.keys()
    result = []

    for key in all_key:
        value1 = file1.get(key)
        value2 = file2.get(key)

        if key in added:
            result.append(get_added_status(key, value2))
        elif key in deleted:
            result.append(get_deleted_status(key, value1))

        elif isinstance(value1, dict) and isinstance(value2, dict):
            result.append(get_nested_status(key, value1, value2))
        elif value1 != value2:
            result.append(get_changed_status(key, value1, value2))
        else:
            result.append(get_unchanged_status(key, value1))

    return result
