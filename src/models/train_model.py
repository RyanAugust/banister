import logging
from pathlib import Path

from banister_model import banister_model
import pandas as pd
import numpy as np
import yaml

with open("config/config.yaml", "r") as f:
    trian_config = yaml.safe_load(f)['train']


def main():
    ## load processed data 
    data = pd.read_csv('data\processed\processed_activity_data.csv')
    print('> Data Loaded')
    # Establish model
    model = banister_model(ctlatl_start=0)

    # Train model on loaded data
    print('> Training...')
    mf = model.train(
        load_metric        =data['load_metric'],
        performance_metric =data['performance_metric'],
        initial_guess      =trian_config['initial_guess'],
        bounds             =trian_config['bounds'])
    return mf


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    mf = main()
    params = ', '.join([f'{val:0.4f}' for val in mf['x'].tolist()])
    print(f"Params: {params}")

