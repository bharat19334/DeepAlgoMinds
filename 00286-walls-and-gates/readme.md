<h1>286. Walls and Gates</h1>

<p>
You are given an <code>m x n</code> 2D grid <code>rooms</code> initialized with these three possible values:
</p>

<ul>
    <li><code>-1</code> - A wall or an obstacle.</li>
    <li><code>0</code> - A gate.</li>
    <li>
        <code>INF</code> - Infinity means an empty room. We use the value
        <code>2^31 - 1 = 2147483647</code> to represent <code>INF</code>
        as you may assume that the distance to a gate is less than
        <code>2147483647</code>.
    </li>
</ul>

<p>
Fill each empty room with the distance to its <strong>nearest gate</strong>.
If it is impossible to reach a gate, it should be filled with <code>INF</code>.
</p>

<hr>

<h3>Example 1:</h3>

<p><strong>Input:</strong></p>

<pre>
rooms = [
    [2147483647, -1,          0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1,          2147483647, -1],
    [0,          -1,          2147483647, 2147483647]
]
</pre>

<p><strong>Output:</strong></p>

<pre>
[
    [3, -1, 0, 1],
    [2, 2, 1, -1],
    [1, -1, 2, -1],
    [0, -1, 3, 4]
]
</pre>

<hr>

<h3>Example 2:</h3>

<p><strong>Input:</strong></p>

<pre>
rooms = [
    [-1]
]
</pre>

<p><strong>Output:</strong></p>

<pre>
[
    [-1]
]
</pre>

<hr>

<h3>Constraints:</h3>

<ul>
    <li><code>m == rooms.length</code></li>
    <li><code>n == rooms[i].length</code></li>
    <li><code>1 &lt;= m, n &lt;= 250</code></li>
    <li>
        <code>rooms[i][j]</code> is <code>-1</code>, <code>0</code>, or
        <code>2^31 - 1</code>.
    </li>
</ul>
