#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tensorflow as tf

# Session对象在使用完成或需要关闭以释放资源。除了显示调用close外，也可以使用“with”代码块来自动完成关闭动作。
with tf.Session() as sess:
    example = tf.zeros([10]).eval()
    print(example)
