class pow_solution:
    def my_pow(self, x, y):
        if y == 0:
            return 1
        # oubli exposant négatif!
        elif y < 0:
            return 1/self.my_pow(x, -y)
        else:
            result = x
            for _ in range(y-1):
                result *= x

        return result

# web solution
class py_solution:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print('classe simulant la fonction puissance')
my_power = pow_solution()
print('0**2', my_power.my_pow(0, 2))
print('-1**2', my_power.my_pow(-1, 2))
print('-1**3', my_power.my_pow(-1, 3))
print('2**0', my_power.my_pow(2, 0))
print('2**2', my_power.my_pow(2, 2))
print('10**3', my_power.my_pow(10, 3))
print('-10**5', my_power.my_pow(-10, 5))
print('2**-3', my_power.my_pow(2, -3))

print('2**-3', py_solution().pow(2, -3))
print('3**5', py_solution().pow(3, 5))
print('100**0', py_solution().pow(100, 0))

