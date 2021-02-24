# CLI接口

这是一个复杂应用的命令行接口程序包,它依赖于[Click](https://click-docs-zh-cn.readthedocs.io/zh/latest/index.html),通过该接口可以方便的扩展自己项目的脚本命令,它是可拔插的

## 脚本命令开发

Tips: 请在项目虚拟环境下进行操作

1. 把该程序包拷贝到你需要扩展的项目根目录下,当然你也可以自己选择拷贝到项目下的其他位置;
2. `cd`到该程序包的根目录下,这时候你可以看到有一个`setup.py`文件,然后执行下面命令

```pip
pip install --editable .
```

- 目录下会多出一个`easy_script.egg-info`文件夹,说明开发环境配置成功
- 然后,我们主要在`.../esp/command/`目录下进行自己的脚本开发,里面初始化安装时默认放了两个演示如何开发的文件,分别是`demo.py`和`demo2.py`
- 想要看懂该程序如何运作的你需要了解[复杂的应用程序](https://click-docs-zh-cn.readthedocs.io/zh/latest/complex.html)这一小节的内容

当你开发完,打包安装之前别忘了执行下面代码清理环境

```pip
pip uninstall easy-script
```

## 打包/安装

当项目开发完,一切准备就绪时,该cli脚本也可以单独捆绑程序打包发布  

**打包:**

```shell
# 同样需要先cd到脚本根目录
python setup.py sdist
```

文件会被打包到`.../dist/easy_script-0.1.tar.gz

**安装:**

```shell
pip install easy_script-0.1.tar.gz
```

安装完以后,打包时留下的`build`文件(`.../dist/`, `.../easy_script.egg-info/`)都可以删除
