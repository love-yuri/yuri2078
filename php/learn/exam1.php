<?php
echo <<<HTML
<html lang="zh"> 
<head>    
	<title>表格的颜色</title>  
</head> 
<body>   
	<table border="2" bgcolor="pink">    
		<tr>     
			<th bgcolor="#ffaa00">彩电</th>     
			 <th bgcolor="green">冰箱</th>
             <th bgcolor="pink" row" rowspan="2">家电</th>  
		</tr>     
		<tr bgcolor="yellow">     
            <td>a</td>
            <td>b</td>      
		</tr>     
	</table>  
</body> 
</html>
HTML;
