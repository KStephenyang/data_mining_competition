# coding=utf-8


param = {
    # 1.General Parameters
    'booster': 'gbtree', # 提升计算的模型
    'silent': 0,  # 0为打印信息，1为缄默
    # 'nthread': 4, # XGBoost运行时的线程数

    # 2.Booster Parameters
    'eta': 0.1,  # 学习率，默认0.3，取值范围为：[0,1]，典型值为0.01-0.2，越小越保守

    'gamma': 0,  # 节点分裂所需的最小损失函数下降值，和损失函数息息相关。默认0，典型值0.1、0.2，越大越保守，
    'subsample':0.8, # 用于训练模型的子样本占整个样本集合的比例，行采样，典型值0.5-1，越小越保守。
    'colsample_bytree ': 1,  # 在建立树时对特征采样的比例，列采样。典型值0.5-1
    'max_depth': 3,  # 树的最大深度，默认6，典型值为3-10，越大越易过拟合。
    'min_child_weight':5, # 这个参数非常影响结果，最小叶子节点样本权重和。如果一个叶子节点的样本权重和小于min_child_weight则拆分过程结束。在现行回归模型中，这个参数是指建立每个模型所需要的最小样本数。默认1，越大算法越易欠拟合


    # 'max_delta_step': 0,  # 限制每棵树权重改变的最大步长。越大越保守。通常，这个参数不需要设置。但是当各类别的样本十分不平衡时，它对逻辑回归是很有帮助的。

    'lambda':3, # 权重的L2正则化项，默认是1
    'alpha':1,# 权重的L1正则化项，默认是1
    'lambda_bias': 0,  # 在偏置上的L2正则。缺省值为0（在L1上没有偏置项的正则，因为L1时偏置不重要）
    # 'scale_pos_weight':1 # 各类样本十分不平衡时，把这个参数设置为一个正数，可以使算法更快收敛。默认是1

    # 3.Task Parameters
    # 'tree_method': 'approx',
    'objective': 'binary:logistic',  # 使用的模型，分类的数目
    'eval_metric':'logloss', # 校验数据所需要的评价指标，不同的目标函数将会有缺省的评价指标
    'base_score':0.5, # 对于所有样本预测为正样本的全局偏置（初始分数）。如果迭代次数够多，改变这个参数对结果不会有影响。
    'seed':0 # 随机数的种子
}
num_boost_round = 7  # 迭代的次数，弱分类器的数量
nfold = 5 # 交叉验证的折数

feature_num = 101
start = 316580

end = 538636






