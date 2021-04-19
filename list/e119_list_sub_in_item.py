def sub_in_item(l, sub):
    return any(sub in x for x in l)

L = ['red', 'black', 'white', 'green', 'orange']
print('Liste', L)
sub = 'ack'
print('présence "{}" ? : {}'.format(sub, sub_in_item(L, sub)))
sub = 'abc'
print('présence "{}" ? : {}'.format(sub, sub_in_item(L, sub)))
