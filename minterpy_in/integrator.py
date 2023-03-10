# -*- coding:utf-8 -*-
import numpy as np

from minterpy.transformation import Transformer


def monomial_integrate(gamma):
    case = np.mod(gamma, 2) == 0
    temp_gamma = gamma[case]
    temp_integ = 2 / (temp_gamma + 1)
    res = np.zeros(gamma.shape)
    res[case] = temp_integ
    return res.prod(axis=0)


# TODO
class integrate(Transformer):
    def __init__(self, m=2, n=2, lp_degree=2):
        Transformer.__init__(self, m, n, lp_degree)
        self.__build_trans_prod()

    def __build_trans_prod(self):
        self.__integ_li = np.dot(self.lagrange2canonical.T, monomial_integrate(self.exponents))

    def integrate(self, func):
        return np.dot(func(self.tree.grid_points), self.__integ_li)
w

# TODO is this a test, routine...?
if __name__ == '__main__':
    from src.minterpy.diagnostics import count
    from scipy.integrate import tplquad  # dblquad,
    from src.minterpy.integrator_others import ngauss_quad

    input_para = (3, 4, 1)
    test_integrate1 = integrate(*input_para)


    @count
    def f(x):
        return -2 * x[0] ** 4 + 4 * x[1] ** 2 + 3 * x[2] + 10


    def f_wrapper(x, y, z):
        return f([x, y, z])


    test_res = test_integrate1.integrate(f)

    count_ours = f.called

    test_res_quad = tplquad(f_wrapper, -1, 1, lambda x: -1, lambda x: 1, lambda x, y: -1, lambda x, y: 1)
    count_quad = f.called - count_ours

    print("==== COMPARE TO SCIP.TPLQUAD ====")
    print("---- setting ----")
    print("dim: %d, deg: %d, lp_degree: %d" % (input_para[0], input_para[1], input_para[2]))
    print()

    print("---- result -----")
    print("our result", test_res)
    print("quad result", test_res_quad)
    print("abs_err", np.abs(test_res - test_res_quad[0]))
    print()

    print("---- function calls ----")
    print("func calls (our)", count_ours)
    print("func calls (quad)", count_quad)
    print()

    input_para = (4, 7, 1)
    test_integrate = integrate(*input_para)

    test_gauss = ngauss_quad(input_para[0], input_para[1])


    @count
    def f(x):
        return -2 * x[0] ** 4 + 4 * x[1] ** 2 + 3 * x[2] + 10 + 11 * x[2] ** 6 + 100 * x[3] ** 5 * x[2] ** 2 - 89 * x[
            1] ** 7


    test_res = test_integrate.integrate(f)

    count_ours = f.called

    test_res_gauss = test_gauss.integrate(f)
    count_gauss = f.called - count_ours

    print("==== COMPARE TO GAUSS ====")
    print("---- setting ----")
    print("dim: %d, deg: %d, lp_degree: %d" % (input_para[0], input_para[1], input_para[2]))
    print()

    print("---- result -----")
    print("our result", test_res)
    print("gauss result", test_res_gauss)
    print("abs_err", np.abs(test_res - test_res_gauss))
    print()

    print("---- function calls ----")
    print("func calls (our)", count_ours)
    print("func calls (gauss)", count_gauss)
