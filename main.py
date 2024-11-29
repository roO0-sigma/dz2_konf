from config import load_config
from dependency_parser import get_dependencies
from output_handler import output_graph

if __name__ == "__main__":
    # Загрузка конфигурации из файла config.ini
    config = load_config('config.ini')

    # Получение зависимостей для указанного пакета
    dependencies = get_dependencies(config['package_name'], int(config['max_depth']))

    # Вывод графа зависимостей в файл
    output_graph(dependencies, config['output_file'])
