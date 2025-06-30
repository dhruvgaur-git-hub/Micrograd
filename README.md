# 🧠 Micrograd (Python)

A tiny autograd engine + visualization, inspired by [Andrej Karpathy's micrograd](https://github.com/karpathy/micrograd)

This project builds a mini deep learning framework with forward and backward passes, and renders computation graphs using Graphviz.

## 🚀 Features

- 🔢 Forward & backward pass using computation graphs
- 🧮 Automatic differentiation
- 🧠 Visualizes gradients & operations with Graphviz
- 💻 Written in under 100 lines of pure Python

## 📸 Example Graph

Visualizing the backpropagation of this computation:

```python
a = Value(2.0, label='a')
b = Value(3.0, label='b')
c = a + b; c.label = 'c'
d = Value(4.0, label='d')
L = c * d; L.label = 'L'
L.backward()
