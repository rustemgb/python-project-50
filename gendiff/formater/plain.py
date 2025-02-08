def converting_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)
    

def get_diff_format_plain(item, path=''):

    key = item.get('key')
    current_path = f"{path}.{key}" if path else key
    status = item.get('status')

    old_value = converting_value(item.get('old_value'))
    new_value = converting_value(item.get('new_value'))
    value = converting_value(item.get('value'))

    if status == 'added':
        return (f"Property '{current_path}' was added with value: {value}")
    if status == 'deleted':
        return (f"Property '{current_path}' was removed")
    if status == 'changed':
        return (f"Property '{current_path}' was updated. "
                        f"From {old_value} to {new_value}")
    if status == 'nested':
        children = item.get('children')
        return format_plain(children, current_path)
        
    return None


def format_plain(diff, path=''):
    result = []

    for item in diff:
        formated_item = get_diff_format_plain(item, path)
        if formated_item is not None:
            result.append(formated_item)
    
    return '\n'.join(result)
