<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Square Root</title>
</head>
<body>
<h1>Square Root</h1>
<p><strong>Difficulty:</strong> Easy</p>
<p><strong>Points:</strong> 2</p>
<p><strong>Accuracy:</strong> 54.03%</p>
<p><strong>Submissions:</strong> 388K+</p>
<p><strong>Average Time:</strong> 20m</p>
<hr>
<h2>Problem Statement</h2>
<p>Given a positive integer <code>n</code>, find the square root of <code>n</code>.</p>
<p>If <code>n</code> is not a perfect square, return the <strong>floor value</strong> of its square root.</p>
<p>The <strong>floor value</strong> of a number is the greatest integer that is less than or equal to that number.</p>
<h2>Examples</h2>
<h3>Example 1</h3>
<p><strong>Input:</strong></p>
<pre>n = 4</pre>
<p><strong>Output:</strong></p>
<pre>2</pre>
<p><strong>Explanation:</strong> Since <code>4</code> is a perfect square, its square root is <code>2</code>.</p>
<h3>Example 2</h3>
<p><strong>Input:</strong></p>
<pre>n = 11</pre>
<p><strong>Output:</strong></p>
<pre>3</pre>
<p><strong>Explanation:</strong> Since <code>11</code> is not a perfect square:</p>
<pre>√11 = 3.316...</pre>
<p>The floor value of <code>3.316...</code> is <code>3</code>.</p>
<h3>Example 3</h3>
<p><strong>Input:</strong></p>
<pre>n = 1</pre>
<p><strong>Output:</strong></p>
<pre>1</pre>
<p><strong>Explanation:</strong> Since <code>1</code> is a perfect square, its square root is <code>1</code>.</p>
<h2>Constraints</h2>
<pre>1 ≤ n ≤ 3 × 10⁴</pre>
<h2>Key Point</h2>
<p>The task is to find the <strong>largest integer x</strong> such that:</p>
<pre>x × x ≤ n</pre>
<p>For example, when <code>n = 11</code>:</p>
<pre>3 × 3 = 9 ≤ 11
4 × 4 = 16 > 11</pre>
<p>Therefore, the answer is <strong>3</strong>.</p>
</body>
</html>
