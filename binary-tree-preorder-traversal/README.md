<h2>144. Binary Tree Preorder Traversal</h2><h3>Easy</h3><hr><div><p>Given <mark id="b80fc0e5-d4cf-41b9-b900-5b3251c30c3a" data-private-id="ca2a9348-4e33-4de4-974c-d28126bab59d" class="f3b44f50-9848-452b-b71a-7f94fed025e5 a2bbc857-cb36-45bd-b7e8-b8239c28674e default-cyan-f88e8827-e652-4d79-a9d9-f6c8b8ec9e2b" tabindex="0">the </mark><code>root</code> of a <mark id="ea6c2be3-06f2-4675-bcc6-8bfd64141bcf" data-private-id="dba747fe-4d32-4139-b1fc-1c301988385b" class="f3b44f50-9848-452b-b71a-7f94fed025e5 a2bbc857-cb36-45bd-b7e8-b8239c28674e default-red-aa94e3d5-ab2f-4205-b74e-18ce31c7c0ce" tabindex="0"><mark id="c14fe06f-832e-4599-99ef-ed9d24032d74" data-private-id="aaec209c-832b-4067-a9c1-20b0e237537b" class="f3b44f50-9848-452b-b71a-7f94fed025e5 a2bbc857-cb36-45bd-b7e8-b8239c28674e default-green-c4d41e0a-e40f-4c3f-91ad-2d66481614c2" tabindex="0">binary </mark><button class="ssh-close" data-foreign=""></button></mark>tree, return <em>the preorder <mark id="f0f82525-1dbb-4b3a-b282-a6e8b24df44f" data-private-id="a09832b6-4134-419e-813a-e184103aeb6f" class="f3b44f50-9848-452b-b71a-7f94fed025e5 a2bbc857-cb36-45bd-b7e8-b8239c28674e default-cyan-f88e8827-e652-4d79-a9d9-f6c8b8ec9e2b" tabindex="0">traversal </mark>of its nodes' values</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;">
<pre><strong>Input:</strong> root = [1,null,2,3]
<strong>Output:</strong> [1,2,3]
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> root = []
<strong>Output:</strong> []
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> [1]
</pre>

<p><strong>Example 4:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;">
<pre><strong>Input:</strong> root = [1,2]
<strong>Output:</strong> [1,2]
</pre>

<p><strong>Example 5:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;">
<pre><strong>Input:</strong> root = [1,null,2]
<strong>Output:</strong> [1,2]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 100]</code>.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Recursive solution is trivial, could you do it iteratively?</p>
</div>