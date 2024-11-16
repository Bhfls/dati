<h2>说明</h2>

奶牛们按不太传统的方式玩起了小孩子们玩的"跳房子"游戏。奶牛们创造了一个$5×5$的、由与$x$&#44;$y$轴平行的数字组成的直线型网格，而不是用来在里面跳的、线性排列的、带数字的方格。 然后他们熟练地在网格中的数字中跳：向前跳、向后跳、向左跳、向右跳(从不斜过来跳)，跳到网格中的另一个数字上。他们再这样跳啊跳(按相同规则)，跳到另外一个数字上(可能是已经跳过的数字)。 一共在网格内跳过五次后，他们的跳跃构建了一个六位整数(可能以$0$开头，例如$000201$)。 求出所有能被这样创造出来的不同整数的总数。
<h2>输入格式</h2>

第$1$到$5$行: 这样的网格，一行$5$个整数。

<h2>输出格式</h2>

第$1$行: 能构建的不同整数的总数。

<h2>样例</h2>
<pre><code class="language-input1">1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 2 1
1 1 1 1 1</code></pre><pre><code class="language-output1">15</code></pre>