import yaml

DATAHUB_CHART_PATH = 'charts/datahub-executor-worker/Chart.yaml'
with open(DATAHUB_CHART_PATH) as datahub_chart_yaml:
    datahub_chart_obj = yaml.safe_load(datahub_chart_yaml)
    dependencies = datahub_chart_obj['dependencies']
    for dependency in dependencies:
        dependency_version_main_chart = dependency['version']
        repository = dependency['repository'].replace("file://./", "")
        subchart_path = DATAHUB_CHART_PATH.replace("Chart.yaml", "") + repository + '/Chart.yaml'
        with open(subchart_path) as subchart_yaml:
            subchart_obj = yaml.safe_load(subchart_yaml)
            subchart_version = subchart_obj['version']
            if dependency_version_main_chart != subchart_version:
                raise Exception(f"Version mismatch in {subchart_path}. Main chart: {dependency_version_main_chart}, Subchart: {subchart_version}")