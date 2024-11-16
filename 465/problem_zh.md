<h2>说明</h2>

又要了丰收的季节，花果山的$n$个香蕉成熟了，每个香蕉的质量为$a_i$。蒜头君还养着$m$只猴子，每只猴子的体重为$b_i$。猴子们吃香蕉有一定的顺序，按照体重从大到小的顺序一个个拿香蕉。当一轮拿完时，如果还有多的香蕉就会继续一个个拿，直到香蕉被取完。每个猴子都很聪明，每次会选质量最大的那个香蕉。<br />
现在问题来了，最后每个猴子能获得多少质量的香蕉？
<h2>输入格式</h2>

第一行两个整数$n$&#44; $m$ ($1 ≤n&#44; m ≤ 10^5$)。<br>第二行$n$个整数$a_i$ ($1 <a_i≤10^4$)，表示每个香蕉的质量。<br>第三行$m$个整数$b_i$ ($1 <b_i≤10^9$)，表示每只猴子的体重，保证每个体重互不相同。

<h2>输出格式</h2>

一行，$m$个用空格分隔的整数，表示每个猴子获得的香蕉质量之和。

<h2>样例</h2>
<pre><code class="language-input1">5 3
1 2 3 4 5
3 2 1</code></pre><pre><code class="language-output1">7 5 3</code></pre>