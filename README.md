### PWN 入门  
---  

帮助菜鸟玩家上手pwn题  

pwn大概有这么几种类型：  

1. ROP
    * re2text
    * re2lib
    * re2shellcode
    * re2system  
    
2. 格式化字符串漏洞  

3. 堆溢出
    * Unlink
    * Use After Free
    * Fastbin Attack  
    * Chunk Extend / Overlapping  
    * House Of Einherjar  
    * House of Lore  
    * House Of Force  
    * Unsorted Bin Attack  
    * House of Orange  
    * House of Rabbit  
    * House of Roman  


4. IO_FILE利用  
    * 伪造 vtable 劫持程序
    * FSOP
    * 新版本 libc 下 IO_FILE 的利用  

5. 条件竞争  

6. 整数溢出  

7. 沙箱逃逸

pwn是最暴力的攻击方式，也最具美感，希望大家玩的愉快。

在linux下无法愉快的使用IDA，但是kali自带一个非常牛逼的反编译工具radare2  

由于这个工具是开源的，所以维护良好，只是上手难度较大，建议阅读官方文档。  

[radare2文档](https://radare.gitbooks.io/radare2book/content/)  

这两篇文章介绍了c语言调用栈的原理，建议认真阅读：  

[c语言调用栈(1)](http://www.cnblogs.com/clover-toeic/p/3755401.html)  

[c语言调用栈(2)](http://www.cnblogs.com/clover-toeic/p/3756668.html)  

然后我建议阅读《Linux c 一站式编程》这本书的中页部分详细的讲述了c与汇编的对应关系，以及不同编译器的特性，还有各种段的特性，这些基础知识是很有必要的。  

比如对于bss段我就没有查到更多详细的资料，网上介绍大多千篇一律，对于如何识别bss段却很少涉及。  

还需要了解一下数据在内存中存储的方式，以及内存寻址方式，32位机保留了16位机的寄存器名，但是已经不使用 **基址×16 +偏移地址**的方式了(不考虑实模式)，但是传参原理，保存栈帧的方式依然大同小异，还有大端小端的区别等等。

必不可少的工具还有pwntools  

```
pip install pwntools
```

注意python的版本问题  

这里上传了bin-linux是radare官方给的练习题，目的是为了练习Reverse，但是大部分题可以通过pwn解答。  

其他的题目是一些简单题目，上手较容易，python文件是对应的exploit。

另外[pwnable.kr](https://pwnable.kr)也是一个很棒的网站。  

希望大家能够沉下心来欣赏二进制的艺术。  

##### Author dyf@Ever404
