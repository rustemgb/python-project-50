def converting_value(value, indent_count=2):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        indent = " " * (indent_count + 4)
        result = []

        for key, inner_value in value.items():
            convert_value = converting_value(inner_value, indent_count + 4)
            result.append(f'{indent}  {key}: {convert_value}')

        string_format = '\n'.join(result)
        end_indent = " " * (indent_count + 2)   
        return f"{{\n{string_format}\n{end_indent}}}"
    return f'{value}'
    

def get_diff_format_stylish(diff, indent_count=2):

    indent = " " * indent_count
    result = []

    for item in diff:
        old_value = converting_value(item.get('old_value'), indent_count)
        new_value = converting_value(item.get('new_value'), indent_count)
        value = converting_value(item.get('value'), indent_count)

        key = item.get('key')
        status = item.get('status')

        if status == 'added':
            result.append(f'{indent}+ {key}: {value}')
        if status == 'deleted':
            result.append(f'{indent}- {key}: {value}')
        if status == 'changed':
            result.append(f'{indent}- {key}: {old_value}')
            result.append(f'{indent}+ {key}: {new_value}')
        if status == 'unchanged':
            result.append(f'{indent}  {key}: {value}')
        if status == 'nested':
            children = get_diff_format_stylish(
                item.get('children'), indent_count + 4)
            result.append(f'{indent}  {key}: {children}')
        
    string_format = '\n'.join(result)
    end_indent = " " * (indent_count - 2)    
    return f"{{\n{string_format}\n{end_indent}}}"
