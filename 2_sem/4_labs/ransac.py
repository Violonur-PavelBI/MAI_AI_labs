"""
RANSAC for 2d lines
Algorythm:

I Hypotesys generation Stage

1. Sample 2d points (1. 2 ponts; 2. 5 points)
2. Model estimation (1. analytics; 2. MSE estimation)

II Hypotesys evaluation Stage

3. Inlier counting (%inlinear > threshold) 
    if True -> best params
    if False -> 1.
4. # iter > num_iter?

"""
import numpy as np
from line import Line
import matplotlib.pyplot as plt

class RANSAC:
    def __init__(self) -> None:
        self.iter_num: int = 100
        self.inlin_thrsh: float = 0.8
        self.epsilon: float = 0.1
        self.n_pointsy: int = 2
        self.best_params: dict = {"k": None, "b": None}
        self.inlinears: list = []
        self.outliers: list = []
        self.score: int = 0
        self.points: np.ndarray = None
        self.mse: bool = False

    def set_case(self, case_params) -> None:

        if "iter_num" in case_params.keys():
            self.iter_num = case_params["iter_num"]
        if "n_pointsy" in case_params.keys():
            self.n_pointsy = case_params["n_pointsy"]
        if "inlin_thrsh" in case_params.keys():
            self.inlin_thrsh = case_params["inlin_thrsh"]
        if "epsilon" in case_params.keys():
            self.epsilon = case_params["epsilon"]
        if "mse" in case_params.keys():
            self.mse = case_params["mse"]
        if not "points" in case_params.keys():
            raise ValueError(f"case_params обязан включать в себя ключь 'points'")
        self.points = case_params["points"]

    def clear_case(self) -> None:
        self.__init__()

    def fit(self):
        for i in range(self.iter_num):
            point = self.points[np.random.choice(self.points.shape[0], self.n_pointsy, replace=False), :]
            line = Line(point)
            line.estimate_params()
            inlnrs, outlnrs= line.devide_points(self.points, self.epsilon,self.mse)
            score = len(inlnrs) / self.points.shape[0] # accuracy
            if score > self.score:
                k, b = line.get_params()
                self.best_params["b"] = b
                self.best_params["k"]=k
                self.score = score
                self.inlinears = inlnrs
                self.outliers = outlnrs

    def draw(self):
        plt.plot(self.inlinears.T[0], self.inlinears.T[1], 'o', label='inlinears')
        plt.plot(self.outliers.T[0], self.outliers.T[1], 'o', label='outliers')
        plt.plot(self.points.T[0], self.best_params['k']*self.points.T[0] + self.best_params['b'], 'r', label='Fitted line')
        plt.legend()
        plt.show()
