import numpy as np
from scipy import optimize
import math
import json
#                                 k1,         k2,        p0,     CTLS,  ATLS
# sample_inputs = {'initial_guess':[0.5,        0.5,       58,      45,      7]
#                  ,'bounds':      [(.1,1.90), (.1,2.90), (50,70), (30,50), (5,12)]}


class banister(object):
    def __init__(self, params, ctlatl_start=0):
        self.params = params
        self.ctls = []
        self.atls = []
        self.ctlatl_start = [ctlatl_start]
    
    def model(self, load_metric, params):
        if len(params) != 5:
            params = self.params
        self.params = params
        
        self.ctls = self.atls = self.ctlatl_start 
        Banister_Predictions = np.array([])
        for i in range(len(load_metric)):
            ctl = (load_metric[i] * (1-math.exp(-1/params[3]))) + (self.ctls[i] * (math.exp(-1/params[3])))
            atl = (load_metric[i] * (1-math.exp(-1/params[4]))) + (self.atls[i] * (math.exp(-1/params[4])))
            self.ctls.append(ctl)
            self.atls.append(atl)
            Banister_Predictions = np.append(Banister_Predictions, params[2] + params[0]*ctl - params[1]*atl)

        return Banister_Predictions
    
    def optimize_banister(self, load_metric, performance_metric, params):
        valid_perf_idx = performance_metric > 0 # protects fitting for only rows where there is a performance test
        losses = []

        Banister_Predictions = self.model(load_metric, params=params)
        
        losses = abs(performance_metric[valid_perf_idx] - Banister_Predictions[valid_perf_idx])
        MAE = np.mean(losses)
        return MAE
    
    def fit(self, load_metric, performance_metric, initial_guess, bounds=bounds):
        individual_banister_model = optimize.minimize(optimize_banister
                                                    ,x0=initial_guess
                                                    ,bounds=bounds
                                                    # ,method='Nelder-Mead'
                                                    # ,tol=1e-8
                                                    )
        print(individual_banister_model)
        for val in individual_banister_model['x']:
            print(val)
        return individual_banister_model