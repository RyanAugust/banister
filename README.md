Banister
==============================

Simple implimentation of banister model solver with an emphasis on the ability to experiment with different load and "performance" metrics.

## Execution

1. Customize the `config.yaml` file to your spec. for the most part this means setting the load and performance metrics here. Load and performance metrics for now should be chosen based on the values made available in the `CheetahPyAnalytics` package such that aggregation is accurate. Later versions of this model will enable hot encoding of metric calculations such that you can define your own (ie bring your own metric philosophy).
2. Run the `make_dataset` script by using `python src/data/make_dataset.py`. This will take your original activity level data from the `data/raw` dir and generate a file in the `processed` subdirectory, which is ready for model input.
3. Run the `train_model` script by using `python src/models/train_model.py`. This will train the banister model using the processed data generated in step 2 and will output both the parameters of the model and (if set in the config) a plot of true versus predicted performance measures to give you an idea of the model's accuracy versus your own data.

## FAQ
___
**What is a load metric and which one should I use?**

Load metrics are any measure of exertion an athlete undertakes via their training. In it's most simple form a 'metric' such as precieved exertion can be used. A more advanced or involved metric may be something like TSS (popularized by Andy Coggan with endurance athletes). When beginning, use whatever is available to you. As you progress, begin to learn more about devices that are specific to your sport and can provide **accurate and objective** measures of effort/load (such as power meters or heart rate straps).

**What is a performance metric and which one should I use?**

Performance metrics are very specific to both your sport and objectives. Potential metrics you may choose from are things like Functional Threshold Power or Critical Power in cycling, or possibly your time for specific distance like a 5k on the track.
It is advisable to **not** pick metrics that may be overly influenced by outside factors (ie speed or HR) unless you're able to test them in a somewhat controlled mannor (ie on a track or on days with low wind and similar weather conditions). If you are unable to account for outside factors these style of metrics may introduce noise into the model and negatively effect your ability to accurately solve for your unique parameters.

**What are the advantages and disadvantages of the banister model?**

Advantages of the banister model are it's flexability to take a multitude of varying inputs in terms of load and performance right from the start. This means that from the beginning you're working with data that is immediately relevant to you and solving for "How much load will I need to take on to reach an X performance" is available to you without supplemental calculations or assumptions—-we are instead modeling on the direct metric. 

Disadvantages of the banister model are that it assumes linear gains in performance with additional load. In more simple terms up and to the right load will **always** result in up and to the right performance. While on the surface this sounds like a vaild assumption, the devil is in the details. Things like overtraining or training specificity are not captured in the Banister model and therefore the recommendations you may generate for yourself using it will always need vailidation; that is to say that if you find you've drastically increased your training load but on test days you're not seeing the improvement you expect there are deeper issues at hand, for which the model will not be able to give you a straight forward answer to.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io
