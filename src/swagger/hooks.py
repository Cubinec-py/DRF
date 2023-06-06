def custom_preprocessing_hook(endpoints):
    # your modifications to the list of operations that are exposed in the schema
    # for (path, path_regex, method, callback) in endpoints:
    #     print(path, path_regex, method, callback)
    print(endpoints)
    return endpoints
