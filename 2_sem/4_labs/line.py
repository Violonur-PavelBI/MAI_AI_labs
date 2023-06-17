"""Модуль для работы с прямыми.
"""
from typing import Tuple

import numpy as np


class Line:
    def __init__(self, points: np.ndarray) -> None:
        self.k = None
        self.b = None
        self.points = points

    def estimate_params(self) -> None:
        points_num = len(self.points.T[0])
        if points_num < 2:
            raise ValueError(
                f"Not enough points. Must be at least 2, but got {points_num}."
            )
        else:
            A = np.vstack([self.points.T[0], np.ones(len(self.points.T[0]))]).T
            self.k, self.b = np.linalg.lstsq(A, self.points.T[1], rcond=None)[0]

    def get_params(self) -> Tuple[float, float]:
        return (self.k, self.b)

    def set_params(self, k: float, b: float) -> None:
        self.k = k
        self.b = b

    def devide_points(
        self, points: np.ndarray, eps: float, mse: bool = False
    ) -> Tuple[np.ndarray, np.ndarray]:
        inliers = np.array([[]])
        outliers = np.array([[]])
        for x, y in points:
            score = abs(y - x * self.k - self.b)
            if mse:
                score = score**2
            if score < eps:
                inliers = np.append(
                    inliers, [[x, y]], axis=(1 if inliers.shape[1] < 2 else 0)
                )
            else:
                outliers = np.append(
                    outliers, [[x, y]], axis=(1 if outliers.shape[1] < 2 else 0)
                )
        return (inliers, outliers)
