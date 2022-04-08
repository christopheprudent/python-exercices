# web solution

'''Days of the week'''
# Source:https://bit.ly/30NoXF8
 
from datetime import date
from itertools import islice
 
# xmasIsSunday :: Int -> Bool
def xmasIsSunday(y):
    '''True if Dec 25 in the given year is a Sunday.'''
    return 6 == date(y, 12, 25).weekday()
 
 
# main :: IO ()
def main():
    '''Years between 2000 and 2150 with 25 December on a Sunday'''
 
    xs = list(filter(
        xmasIsSunday,
        enumFromTo(2000)(2150)
    ))
    total = len(xs)
    #print(f'DEBUG\nxs={xs}\nindex={index(xs)(enumFromTo(0)(total - 1))}\n')
    print(f'DEBUG\nxs={xs}\n')
    #print(unlines(map(str,xs)))
    print(
        fTable(main.__doc__ + ':\n\n' + '(Total ' + str(total) + ')\n')(
            lambda i: str(1 + i)
        )(str)(index(xs))(
            enumFromTo(0)(total - 1)
        )
    )
 
 
# GENERIC -------------------------------------------------
 
# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    '''Integer enumeration from m to n.'''
    return lambda n: list(range(m, 1 + n))
 
 
# index (!!) :: [a] -> Int -> a
def index(xs):
    '''Item at given (zero-based) index.'''
    return lambda n: None if 0 > n else (
        #'item'+str(xs[n]) if (
        xs[n] if (
            hasattr(xs, "__getitem__")
        #) else 'islice'+next(islice(xs, n, None))
        ) else next(islice(xs, n, None))
    )
 
 
# unlines :: [String] -> String
def unlines(xs):
    '''A single string formed by the intercalation
       of a list of strings with the newline character.
    '''
    return '\n'.join(xs)
 
 
#  FORMATTING ---------------------------------------------
# fTable :: String -> (a -> String) ->
#                     (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
                     f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        print(f'DEBUG\nxs={xs}\nys={ys}\nw={w}\n')
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    ) 
 
# MAIN --
if __name__ == '__main__':
    main()

