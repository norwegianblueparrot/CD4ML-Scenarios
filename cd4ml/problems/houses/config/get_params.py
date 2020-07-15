# parameters for running the pipeline

from cd4ml.problems.houses.config.problem_params import problem_params
from cd4ml.problems.houses.config.ml_model_params import model_parameters
from cd4ml.problems.houses.config.ml_fields import get_ml_fields

pipeline_params = {'problem_name': 'houses',
                   'problem_params': problem_params,
                   'model_params': model_parameters,
                   'ml_fields': get_ml_fields()}