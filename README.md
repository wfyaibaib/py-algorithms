py-algorithms
=============

 Algorithms and data structures for python. I also have a c++ version, [tf-lib](https://github.com/wfyaibaib/tf-lib)
 This project is aim to make the way to learn algorithms and data structures easy!
 
 
Here is a example for red-black tree:
```python
>>> from rbtree import *
>>> tree = Rbtree()
>>> tree.insert_data_list(range(10))
>>> tree.tree_shape()
                                        [None]
                                (9, r)
                                        [None]
                        (8, b)
                                [None]
                (7, r)
                                [None]
                        (6, b)
                                [None]
        (5, b)
                        [None]
                (4, b)
                        [None]
(3, b)
                        [None]
                (2, b)
                        [None]
        (1, b)
                        [None]
                (0, b)
                        [None]
>>> tree.render('rbtree')
>>>
```

After call the render method , you will get a 'rbtree.png' file in the current working directory.
The render method require that you have install the python GraphViz package, called graphviz.
[graphviz](https://github.com/wfyaibaib/graphviz)
![An empty red-black tree insert 10 nodes.](http://d.pcs.baidu.com/thumbnail/f3b542605096b72fd9c6f302cee3ffd2?fid=1242427424-250528-308547114732331&time=1398681167&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-G8%2FQr%2BI4rFWqEkBPLsfr2rpHWzI%3D&expires=8h&prisign=RK9dhfZlTqV5TuwkO5ihMQzlM241kT2YfffnCZFTaEME9YV1nJf6D6J80iU4zC2r2V4S+FNWGNFxHzeBGnigsNFaawa4C9wFhXwC5bIhj4z5T8yM4Gib1laEi0I09FHKk5UdQdxWgLwqyhHIuCXWkoJKwOrktN5yaJjzMFAxE2sJKV7i84jmEBYc0ZhkMVN1qwsW85y4lHrqwShhlBwA3BUVvvOpygWlZVdX1OYCRx/KuA2R1qvvnw==&r=865262101&size=c850_u580&quality=100)

