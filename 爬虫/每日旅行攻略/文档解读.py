#windows中这样写路径，加r在字符串前面，或者两个\\代表一个实际的\
r""  //
#r代表读取的是纯文本文件（plain text）。

#rb代表用二进制方式打开，读取的就都是字节了，或者你简单理解就是乱码。
#encoding 代表的是编码格式，它会用这个将字节读取成字符。前者你可以继续理解成乱码（当然这个说法不严谨，为初学者方便理解准备的）

f=open('/Users/michael/notfound.txt', 'r',encoding='utf8')
按照文本的实际格式去设置。

默认值会根据系统去定，所以建议显示的赋值。不要让程序代你去赋值。

如果是新手，强烈建议，文本保存成utf8格式，encoding也是utf8

如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/path/to/file', 'r',encoding='utf8')
    print(f.read())
finally:
    if f:
        f.close()
但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('/path/to/file', 'r',encoding='utf8') as f
    print(f.read())
这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。

读取大文件

比较pythonic的方法是：

with open(filename, 'r',encoding='utf8') as flie:
    for line in file:
		print(line)
以上代码会逐行去读取文本内容，不会出现内存泄露的情况。

或者使用以下代码也可以，readline会逐行读取，不会一次加载。

while True:
    line = f.readline()
    if not line:
        break
以下方法针对小文件的时候可以，但是文件比较大的时候会有内存泄露的风险，因为readlines是一次读取所有的行，放到一个list中返回。

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
写入文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

>>> f = open('/Users/michael/test.txt', 'w',encoding='utf8')
>>> f.write('Hello, world!')
>>> f.close()
你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：

with open('/Users/michael/test.txt', 'w',encoding='utf8') as f:
    f.write('Hello, world!')
要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

file-like Object

像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

二进制文件

前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

这个时候不要用encoding了，因为是它已经不是字符了，刚才的编解码是针对字符的。

这块大家看看就好。

>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
字符编码

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'

遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

小结

在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。        