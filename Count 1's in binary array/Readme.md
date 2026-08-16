<h1>Count 1's in Binary Array</h1>

<h2>Problem Statement</h2>
<p>
You are given a binary array that is sorted in non-increasing order,
meaning all the <strong>1's</strong> appear before the <strong>0's</strong>.
Find the total number of <strong>1's</strong> present in the array.
</p>

<h2>Examples</h2>

<h3>Example 1</h3>
<pre>
Input: arr[] = [1, 1, 1, 1, 1, 0, 0, 0]
Output: 5
</pre>

<p>Explanation: Count of 1's in the array is 5.</p>

<h3>Example 2</h3>
<pre>
Input: arr[] = [1, 1, 1, 1, 1, 1, 1]
Output: 7
</pre>

<p>Explanation: Count of 1's in the array is 7.</p>

<h2>Approach</h2>
<p>
Since the array is sorted with all 1's before 0's, we can use
<strong>Binary Search</strong> to find the first occurrence of 0.
The index of the first 0 is equal to the total number of 1's.
If there is no 0, then all elements are 1.
</p>

<h2>Complexity</h2>
<p><strong>Time Complexity:</strong> O(log n)</p>
<p><strong>Space Complexity:</strong> O(1)</p>

<h2>Constraints</h2>
<ul>
<li>1 ≤ arr.size() ≤ 10<sup>5</sup></li>
<li>0 ≤ arr[i] ≤ 1</li>
</ul>
