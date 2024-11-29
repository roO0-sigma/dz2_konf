import json
import os

result = {}
def get_dependencies(package_name, max_depth, current_depth=0):

    if current_depth > max_depth:
        return result

    package_json_path = f"C:/Users/roO00/PycharmProjects/dz2/"

    if not os.path.exists(package_json_path + package_name + ".json"):
        return {}

    with open(package_json_path + package_name + ".json") as f:
        package_data = json.load(f)

    dependencies = package_data.get('dependencies', [])
    result[package_name] = dependencies
    for i in dependencies.keys():
        get_dependencies(i, max_depth, current_depth + 1)
    # for dep in dependencies:
    #     result[package_name] = get_dependencies(dep, max_depth, current_depth + 1, seen)

    return result