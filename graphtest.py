from micrograd import Value
from graph_utils import draw_dot

a = Value(2.0, label='a')
b = Value(3.0, label='b')
c = a + b; c.label = 'c'
d = Value(4.0, label='d')
L = c * d; L.label = 'L'

L.backward()

draw_dot(L).render('graph_output', view=True)
