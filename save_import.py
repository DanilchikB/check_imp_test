def save_import(line: str, where_to_save: set)->None:
    """Save found imported objects"""
    import_objects = ''.join(line.strip().split('import')[1:]).replace(' ', '')
    where_to_save.update(import_objects.split(','))