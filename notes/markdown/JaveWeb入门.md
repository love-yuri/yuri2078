# Jave Web 入门

## request



```java
System.out.println("获取客户端发出请求时的完整url : " + request.getRequestURL());
System.out.println("获取获取请求行中资源名称部分 : " + request.getRequestURI());
System.out.println("获取请求行中参数部分 : " + request.getQueryString());
System.out.println("获取 WebApp名称 : " + request.getContextPath());
request.getParameter(""); // 获取指定参数
request.getParameterValues(""); // 获取指定参数列表
request.getParameterMap(); // 获取参数map

// 请求转发 发出一次请求 域中数据共享 属于服务器行为
request.getRequestDispatcher("/").forward(request, response); 

/* 在一个请求中有效 即一次跳转 */
request.setAttribute("a",4); // 设置参数
request.getAttribute("a"); // 获取参数
request.removeAttribute("a"); // 移除参数

// 打印结果
获取客户端发出请求时的完整url : http://localhost:8080/exam_war_exploded/examServlet
获取获取请求行中资源名称部分 : /exam_war_exploded/examServlet
获取请求行中参数部分 : null
获取 WebApp名称 : /exam_war_exploded
```

## response

```java
response.getWriter(); // 只能写入字符流
response.getOutputStream();  // 能写入任何数据流
response.setCharacterEncoding("UTF-8"); // 设置编码
response.setHeader("content-type", "text/html;charset=UTF-8"); // 设置解码编码
response.sendRedirect("index.jsp"); // 重定向 发出两次请求 域中数据不共享 属于客户端行为
```

## JSP基础

### 常用语法

- `<% 代码片段 %>` 可以包含任何java语句变量
- `<%! 声明语句 %>` 可以在这里声明变量
- `<%= 表达式 %>` 可以嵌入表达式，表达式会被先转换成String

### 注释

| **语法**       | 描述                                                 |
| :------------- | :--------------------------------------------------- |
| <%-- 注释 --%> | JSP注释，注释内容不会被发送至浏览器甚至不会被编译    |
| <!-- 注释 -->  | HTML注释，通过浏览器查看网页源代码时可以看见注释内容 |
| <\%            | 代表静态 <%常量                                      |
| %\>            | 代表静态 %> 常量                                     |
| \'             | 在属性中使用的单引号                                 |
| \"             | 在属性中使用的双引号                                 |

### JSP指令

> JSP指令用来设置与整个JSP页面相关的属性。

JSP指令语法格式：

```
<%@ directive attribute="value" %>
```

这里有三种指令标签：

| **指令**           | **描述**                                                  |
| :----------------- | :-------------------------------------------------------- |
| <%@ page ... %>    | 定义页面的依赖属性，比如脚本语言、error页面、缓存需求等等 |
| <%@ include ... %> | 包含其他文件                                              |
| <%@ taglib ... %>  | 引入标签库的定义，可以是自定义标签                        |

------

### JSP行为

> JSP行为标签使用XML语法结构来控制servlet引擎。它能够动态插入一个文件，重用JavaBean组件，引导用户去另一个页面，为Java插件产生相关的HTML等等。

行为标签只有一种语法格式，它严格遵守XML标准：

```
<jsp:action_name attribute="value" />
```

行为标签基本上是一些预先就定义好的函数，下表罗列出了一些可用的JSP行为标签：：

| **语法**        | **描述**                                                   |
| :-------------- | :--------------------------------------------------------- |
| jsp:include     | 用于在当前页面中包含静态或动态资源                         |
| jsp:useBean     | 寻找和初始化一个JavaBean组件                               |
| jsp:setProperty | 设置 JavaBean组件的值                                      |
| jsp:getProperty | 将 JavaBean组件的值插入到 output中                         |
| jsp:forward     | 从一个JSP文件向另一个文件传递一个包含用户请求的request对象 |
| jsp:plugin      | 用于在生成的HTML页面中包含Applet和JavaBean对象             |
| jsp:element     | 动态创建一个XML元素                                        |
| jsp:attribute   | 定义动态创建的XML元素的属性                                |
| jsp:body        | 定义动态创建的XML元素的主体                                |
| jsp:text        | 用于封装模板数据                                           |

------

### JSP隐含对象

> JSP支持九个自动定义的变量，江湖人称隐含对象。这九个隐含对象的简介见下表：

| **对象**    | **描述**                                                     |
| :---------- | :----------------------------------------------------------- |
| request     | **HttpServletRequest**类的实例                               |
| response    | **HttpServletResponse**类的实例                              |
| out         | **PrintWriter**类的实例，用于把结果输出至网页上              |
| session     | **HttpSession**类的实例                                      |
| application | **ServletContext**类的实例，与应用上下文有关                 |
| config      | **ServletConfig**类的实例                                    |
| pageContext | **PageContext**类的实例，提供对JSP页面所有对象以及命名空间的访问 |
| page        | 类似于Java类中的this关键字                                   |
| exception   | **exception** 类的对象，代表发生错误的 JSP 页面中对应的异常对象 |

------

### 控制流语句

>  JSP提供对Java语言的全面支持。您可以在JSP程序中使用Java API甚至建立Java代码块，包括判断语句和循环语句等等。
