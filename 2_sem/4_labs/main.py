from data import Point_Generator
from line import Line
from ransac import RANSAC
import matplotlib.pyplot as plt


def main():
    point_gen = Point_Generator(100, 0.3)
    points = point_gen.generate_case(None, None, eps=0.1)
    line = Line(points)
    line.estimate_params()
    inlnrs, outlnrs = line.divide_points(points, eps=0.1)
    k, b = line.get_params()
    plt.plot(inlnrs_x, inlnrs_y, "x", label="inliers")
    plt.plot(outlnrs_x, outlnrs_x, "x", label="outliers")
    plt.plot(x, k * x + b, "r", label="Fitted line")
    plt.legend()
    print("Без RANSAC")
    plt.show()
    ransac = RANSAC()
    case_params = {"points": points, "y": y}
    ransac.set_case(case_params)
    ransac.fit()
    print("RANSAC с 2 точками")
    ransac.draw()
    ransac = RANSAC()
    case_params = {"x": x, "y": y, "line_points": 5}
    ransac.set_case(case_params)
    ransac.fit()
    print("RANSAC с 5 точками")
    ransac.draw()


if __name__ == "__main__":
    main()
