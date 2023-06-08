# -*- coding: utf-8 -*-
# import click
import logging
from pathlib import Path
# from dotenv import find_dotenv, load_dotenv

import CheetahPyAnalytics
import pandas as pd
import yaml

with open("config/config.yaml", "r") as f:
    data_config = yaml.safe_load(f)['dataset']

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    static_metrics = {"max_hr": 191
                 ,"resting_hr": 39
                 ,'ae_threshold_hr': 145
                 ,'LTthreshold_hr': 160
                 ,'ae_threshold_pwr': 252
                 ,'LTthreshold_pwr': 302
                 ,'run_settings':{'cp': 356
                                 ,'w_prime': 16900
                                 ,'pmax': 642}}

    datapp = CheetahPyAnalytics.dataset_preprocess(local_activity_store=input_filepath)
    
    print('Building Dataset using...\nload metric:\t{load_metric}\nperformance metric:\t{performance_matric}'.format(load_metric=data_config['load_metric'],
                                                                                                                     performance_matric=data_config['performance_metric']))
    datapp.pre_process(load_metric=data_config['load_metric'],
                    performance_metric=data_config['performance_metric'],
                    filter_sport=['Bike'],
                    fill_performance_forward=False)
    # mean_ = datapp.activity_data['performance_metric'].mean()
    print(f'mean peformance: {datapp.activity_data["performance_metric"].mean():0.3f}')
    datapp.processed_activity_data.to_csv(output_filepath)

if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    main(input_filepath=Path.joinpath(project_dir, 'data/raw/activity_data.csv')
         ,output_filepath=Path.joinpath(project_dir, 'data/processed/processed_activity_data.csv'))
