# 自动化测试之PO模型-学习总结

代码内部已敲注释！

顺序：
case -> pages -> base -> base -> pages -> case -> case ->test

其中：
(这里先初始化绑定，传浏览器驱动、网址什么的)（case -> pages -> base） ->（base这里传动作，如点击动作、滑动动作、点击动作。pages里面是base动作的合集，可以完成像输入账号密码并点击登录这种操作，case是pages的集合）（base -> pages -> case）-> (这里是用来生成测试用例)（case -> test）

![untitled43](https://user-images.githubusercontent.com/70384877/143869226-698f80cd-0aff-43bf-a525-219a8ec98b0a.png)

