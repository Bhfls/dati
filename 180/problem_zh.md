<h2>说明</h2>

数学上，一个数的平方 $x$ 的平方定义为 $x^2=x ×x$。而一个正数 $x$ 的平方根定义为满足$y×y=x$ 的所有的 $y$。<br />
第一步：令初始的解$y_0=1$;<br />
第二步：令$y_1=\frac{y_0+\frac{x}{y_0}}{2}$<br />
第三步：令$y_2=\frac{y_1+\frac{x}{y_1}}{2}$<br />
第四步：令$y_3=\frac{y_2+\frac{x}{y_2}}{2}$<br />
……<br />
第n步：令$y_n=\frac{y_{n-1}+\frac{x}{y_{n-1}}}{2}$<br />
当无限执行下去的时候，结果就会无限接近真实值。当然计算机不可能无限循环执行下去，只能求出近似解。<br />
现在给出要求根号值的 $x$ 和迭代的次数 $n$，请你用该算法求出 $x$ 的平方根的近似值。

<h2>输入格式</h2>

输入第一行两个整数 $x$($1≤x≤10^4$) 和$n$($1≤n≤1000$)，含义如题。

<h2>输出格式</h2>

输出 $x$ 的平方根的近似值，结果保留三位小数。

<h2>样例</h2>
<pre><code class="language-input1">4 10</code></pre><pre><code class="language-output1">2.000</code></pre>
