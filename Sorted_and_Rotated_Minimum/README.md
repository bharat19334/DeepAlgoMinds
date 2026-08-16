<h1>Sorted and Rotated Minimum</h1>

<h2>Problem Statement</h2>
<p>
A sorted array of distinct elements <strong>arr[]</strong> is rotated at
some unknown point. The task is to find the minimum element in the array.
</p>

<h2>Examples</h2>

<h3>Example 1</h3>
<pre>
Input: arr[] = [5, 6, 1, 2, 3, 4]
Output: 1
</pre>
<p>Explanation: 1 is the minimum element in the array.</p>

<h3>Example 2</h3>
<pre>
Input: arr[] = [3, 1, 2]
Output: 1
</pre>
<p>Explanation: Here 1 is the minimum element.</p>

<h3>Example 3</h3>
<pre>
Input: arr[] = [4, 2, 3]
Output: 2
</pre>
<p>Explanation: Here 2 is the minimum element.</p>

<h2>Approach</h2>
<p>
We use <strong>Binary Search</strong> because the array was originally sorted
and then rotated. Compare the middle element with the rightmost element.
If <strong>arr[mid] &gt; arr[right]</strong>, the minimum element lies in the
right half. Otherwise, it lies in the left half including mid.
</p>

<h2>Complexity</h2>
<p><strong>Time Complexity:</strong> O(log n)</p>
<p><strong>Space Complexity:</strong> O(1)</p>

<h2>Constraints</h2>
<ul>
<li>1 ≤ arr.size() ≤ 10<sup>6</sup></li>
<li>1 ≤ arr[i] ≤ 10<sup>9</sup></li>
</ul>
