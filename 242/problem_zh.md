<h2>说明</h2>

每一本正式出版的图书都有一个 ISBN 号码与之对应，ISBN 码包括 $9$ 位数字、$11$位识别码和 $3$位分隔符，其规定格式如"$x-xxx-xxxxx-x$"，其中符号"$-$"是分隔符（键盘上的减号），最后一位是识别码，例如 "$0-670-82162-4$" 就是一个标准的 ISBN 码。ISBN 码的首位数字表示书籍的出版语言，例如 $0$ 代表英语；第一个分隔符"$-$"之后的三位数字代表出版社，例如 $670$代表维京出版社；第二个分隔之后的五位数字代表该书在出版社的编号；最后一位为识别码。<br />
识别码的计算方法如下：<br />
首位数字乘以$1$加上次位数字乘以$2$⋯以此类推，用所得的结果$\mod 11$，所得的余数即为识别码，如果余数为 $10$，则识别码为大写字母'$X$'。例如ISBN号码 "$0-670-82162-4$"中的识别码$4$是这样得到的：对 "$067082162$" 这 $9$个数字，从左至右，分别乘以 $1$，$2$，⋯，$9$，再求和，即$0×1+6×2+⋯+2×9=158$，然后取 $158\mod 11$ 的结果 $4$ 作为识别码。<br />
你的任务是编写程序判断输入的 ISBN 号码中识别码是否正确，如果正确，则仅输出"<code>Right</code>"；如果错误，则输出你认为是正确的 ISBN 号码。
<h2>输入格式</h2>

只有一行，是一个字符序列，表示一本书的 ISBN 号码（保证输入符合 ISBN 号码的格式要求）。

<h2>输出格式</h2>

共一行，假如输入的 ISBN 号码的识别码正确，那么输出"<code>Right</code>"，否则，按照规定的格式，输出正确的 ISBN 号码（包括分隔符"$-$"）。

<h2>样例</h2>
<pre><code class="language-input1">0-670-82162-4</code></pre><pre><code class="language-output1">Right</code></pre>