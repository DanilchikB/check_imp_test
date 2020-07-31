def delete_import(line: str, where_to_remove: set)->None:
    """Removes from the set if the imported object is in use"""
    for import_object in where_to_remove.copy():
        if import_object in line:
            where_to_remove.discard(import_object)
