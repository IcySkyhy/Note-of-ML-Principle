# 一致收敛性

可学习的充分条件是一致收敛性。

```{prf:theorem} 一致收敛性是可学习的充分条件
:label: thm:uc-sufficient

若假设类 $\mathcal{H}$ 关于函数 $m_\mathcal{H}^{UC}$ 满足一致收敛性。那么在样本复杂度函数 $m_{\mathcal{H}}(\epsilon, \delta) < m_\mathcal{H}^{UC}(\epsilon, \delta)$ 的情形下，该假设类是不可知PAC可学习的，而且其 $ERM$ 范式是成功的学习算法（可以返回好的假设）。
```