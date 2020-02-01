# NucleusWarpsToEssentialsX
Python3脚本
将Sponge服务器Nucleus插件的传送点转换为Spigot EssentialsX的传送点

这个脚本是我在尝试把我和朋友的sponge(mc1.12)服务器升级到Paper(1.14)服务器时所写的脚本。

## 提示

* 需要安装Python3.x，并安装`pyyaml`模块(`pip install pyyaml`)
* 需要提前知道新旧世界名字和ID

## 使用方法

1. 下载`converter.py`
2. 将海绵端服务器`nucleus`目录下的`general.json`文件拷贝到`converter.py`旁
3. 在`converter.py`第13行修改世界对应id
4. 运行脚本`python converter.py`
5. 将所有的yml文件复制到另一个服务器`\plugins\Essentials\warps`目录下
6. 完成
