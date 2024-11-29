from plantuml_generator import generate_plantuml_graph  # Импортируем функцию

def output_graph(dependencies, output_file):
    plantuml_code = "@startuml\n"
    plantuml_code += "\n".join(generate_plantuml_graph(dependencies))
    plantuml_code += "\n@enduml\n"

    print(plantuml_code)

    with open(output_file, 'w') as f:
        f.write(plantuml_code)
