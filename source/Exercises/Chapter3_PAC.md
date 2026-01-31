# Chapter 3 一般学习模型

## 习题 3.1

**样本复杂度的单调性。** 令 $\mathcal{H}$ 为二分类任务的一个假设类，其是 PAC 可学习的且样本复杂度由函数 $m_{\mathcal{H}}(\epsilon, \delta)$ 给出。证明 **$m_{\mathcal{H}}$ 对其每个参数是单调非增的**。即：

- 给定任意 $0 < m_1 \leq m_2 < 1$ 和 $0 < \delta < 1$, 有 $m_{\mathcal{H}}(\epsilon, \delta) \geq m_{\mathcal{H}}(\epsilon, \delta)$；

- 给定任意 $0 < \epsilon_1 \leq \epsilon_2 < 1$ 和 $0 < \delta < 1$, 有 $m_{\mathcal{H}}(\epsilon_1, \delta) \geq m_{\mathcal{H}}(\epsilon_2, \delta)$。

---

**解** 仅给出对于 $\epsilon$ 的证明；对参数 $\delta$ 的证明类似。

<!-- **定义 (PAC 样本复杂度):**
$m_{\mathcal{H}}(\epsilon, \delta)$ 是满足以下条件的最小整数 $m$：对于任意分布 $\mathcal{D}$ 和目标概念 $c \in \mathcal{H}$，当样本集大小 $|S| \geq m$ 时，算法输出的假设 $h_S$ 满足：
$$\underset{S \sim \mathcal{D}^m}{\mathbb{P}}[L_{\mathcal{D}}(h_S) > \epsilon] \leq \delta$$

为了方便证明，定义“满足 $(\epsilon, \delta)$ 条件的样本量集合”为 $M(\epsilon, \delta)$：
$$M(\epsilon, \delta) = \{ m \in \mathbb{N} \mid \forall \mathcal{D}, c, \underset{S \sim \mathcal{D}^m}{\mathbb{P}}[L_{\mathcal{D}}(h_S) > \epsilon] \leq \delta \}$$
则样本复杂度为该集合的最小值：$m_{\mathcal{H}}(\epsilon, \delta) = \min M(\epsilon, \delta)$。 -->

设样本量 $m \in M(\epsilon_1, \delta)$，则对于该 $m$，失败概率满足 $\mathbb{P}[L_{\mathcal{D}}(h_S) > \epsilon_1] \leq \delta$；

题设不妨 $\epsilon_1 \leq \epsilon_2$，故误差大于 $\epsilon_2$ 的假设误差也大于 $\epsilon_1$；存在包含关系

$$\{ h_S \mid L_{\mathcal{D}}(h_S) > \epsilon_2 \} \subseteq \{ h_S \mid L_{\mathcal{D}}(h_S) > \epsilon_1 \}$$

概率测度是单调的，由包含关系可得

$$\mathbb{P}[L_{\mathcal{D}}(h_S) > \epsilon_2] \leq \mathbb{P}[L_{\mathcal{D}}(h_S) > \epsilon_1] \leq \delta$$

故亦有 $m \in M(\epsilon_2, \delta)$，即 $m \in M(\epsilon_2, \delta) \Leftarrow m \in M(\epsilon_1, \delta)$，从而有

$$M(\epsilon_1, \delta) \subseteq M(\epsilon_2, \delta)$$

子集的最小值大于等于超集的最小值，故
    
$$\min M(\epsilon_1, \delta) \geq \min M(\epsilon_2, \delta) \Leftrightarrow m_{\mathcal{H}}(\epsilon_1, \delta) \geq m_{\mathcal{H}}(\epsilon_2, \delta)$$