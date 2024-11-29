def generate_plantuml_graph(dependencies, parent=None, seen=None):
    if seen is None:
        seen = set()

    lines = []
    for parent in dependencies.keys():

        for dep in dependencies[parent].keys():
            lines.append(f'    {parent} --> {dep}')
            seen.add(dep)


        # if sub_deps:
        #     lines.extend(generate_plantuml_graph(sub_deps, dep, seen))

    return lines