def get_diff_format_stylish(files_with_status):
    
    result = []
    for file in files_with_status:

        old_value = str(file.get('old_value'))
        new_value = str(file.get('new_value'))
        value = str(file.get('value'))
        key = str(file.get('key'))
        status = file.get('status')

        if status == 'added':
            result.append(f'  + {key}: {value}')
        if status == 'deleted':
            result.append(f'  - {key}: {value}')
        if status == 'changed':
            result.append(f'  - {key}: {old_value}')
            result.append(f'  + {key}: {new_value}')
        if status == 'unchanged':
            result.append(f'    {key}: {value}')
        
    return ('{\n' + '\n'.join(result) + '\n}').lower()

