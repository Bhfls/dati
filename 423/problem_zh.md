<h2>说明</h2>

王老师正在教简单算术运算。细心的王老师收集了$i$道学生经常做错的口算题，并且想整理编写成一份练习。编排这些题目是一件繁琐的事情，为此他想用计算机程序来提高工作效率。王老师希望尽量减少输入的工作量，比如$5+8$的算式最好只要输入$5$和$8$，输出的结果要尽量详细以方便后期排版的使用，比如对于上述输入进行处理后输出$5+8=13$以及该算式的总长度$6$。王老师把这个光荣的任务交给你，请你帮他编程实现以上功能。
<h2>输入格式</h2>

第一行一个整数$n$ ($1≤n≤50$)。<br>接着的$n$行为需要输入的算式，每行可能有三个数据或两个数据。<br>若该行为三个数据则第一个数据表示运算类型，$a$表示加法运算，$b$表示减法运算，$c$表示乘法运算，接着的两个数据$x$&#44;$y$ 表示参加运算的运算数。<br>若该行为两个数据$x$&#44;$y$，则表示本题的运算类型与上一题的运算类型相同，而这两个数据为运算数。<br>数据保证第一个算式有三个数据，$0≤x&#44;y<10000$。

<h2>输出格式</h2>

输出 $2n$行，对于每个输入的算式，第一行输出完整的运算式及结果，第二行输出该运算式的总长度。

<h2>样例</h2>
<pre><code class="language-input1">4
a 64 46
275 125
c 11 99
b 46 64</code></pre><pre><code class="language-output1">64+46=110
9
275+125=400
11
11*99=1089
10
46-64=-18
9</code></pre>