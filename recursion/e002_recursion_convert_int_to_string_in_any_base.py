def convert_int_to_string_in_any_base(x, b=10):
    # à coder caractère si base b > 10
    q = x // b
    m = x % b
    
    #if q > b:
    if x >= b:
        return convert_int_to_string_in_any_base(q, b) + str(m)
    else:
        # FIXME x<b 
        #return str(q) + str(m)
        return str(x)

# web solution
def to_string(n,base):
   convert_String = "0123456789ABCDEF"
   if n < base:
      return convert_String[n]
   else:
      return to_string(n//base,base) + convert_String[n % base]

def result(x, b=10):
    print('dev) conversion', x, 'en base', b, 'en chaîne vaut', convert_int_to_string_in_any_base(x, b))
    print('web) conversion', x, 'en base', b, 'en chaîne vaut', to_string(x, b))

if __name__ == '__main__':
    result(17, 8)
    result(15)
    result(45, 3)
    result(13, 16)
    result(2835, 16)
