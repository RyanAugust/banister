import logging
from pathlib import Path

from banister_model import banister_model
import pandas as pd
import numpy as np


def main():
    ## load processed data 
    data = pd.read_csv('data/processed/banister_data.csv')
    print(data)
    # Establish model
    model = banister_model(ctlatl_start=0)

    # Train model on loaded data
    mf = model.fit(
        loat_metric=data['load_metric']
        ,performance_metric=data['performance_metric']
                    #   k1         , k2        , p0        , CTLS      , ATLS
        ,initial_guess=[0.1        , 0.5       , 50        , 45        , 7     ]
        ,bounds=       [(.1,1.90)  , (.1,2.90) , (50,70)   , (30,50)   , (5,12)])
    return mf


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())

    main()

