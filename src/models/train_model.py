import logging
from pathlib import Path

from banister_model import banister_model
import pandas as pd
import numpy as np
import yaml

with open("config/config.yaml", "r") as f:
    trian_config = yaml.safe_load(f)['train']


def main(input_data_path):
    ## load processed data 
    data = pd.read_csv(input_data_path)
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
    if trian_config['output_plot']:
        predicted_performance = model.model(load_metric=data['load_metric'], params=mf['x'])
        model_performance_plot(true_performance=data['performance_metric'],
                               predicted_performance=predicted_performance)
    return mf

def model_performance_plot(true_performance, predicted_performance):
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1,1, figsize=(10,6), dpi=200)
    true_az = true_performance[true_performance > 0]
    pred_az = predicted_performance[true_performance > 0]
    ax.scatter(true_az.index, true_az, color='blue', alpha=.5, label='True Performance')
    ax.scatter(true_az.index, pred_az, color='red', alpha=.5, label='Predicted Performance')
    ax.legend()
    fig.savefig('performance_plot.png')





if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]
    input_data_path = Path.joinpath(project_dir, 'data/processed/processed_activity_data.csv')

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    mf = main(input_data_path=input_data_path)
    params = ', '.join([f'{val:0.4f}' for val in mf['x'].tolist()])
    print(f"Params: {params}")

