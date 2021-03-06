def print_letter_from_pattern(pattern, m=7, n=5, block='*'):
    for i in range(m):
        line = ''
        for j in range(n):
            if pattern[i][j]:
                line += block
            else:
                line += ' '
        print(line)

letters_pattern = {
    'A' : {
        'pattern' : [
            [0, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 1, 1, 1, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
        ]
    }
  , 'D' : {
        'pattern' : [
            [1, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 1, 1, 1, 0]
        ]
    }
  , 'E' : {
        'pattern' : [
            [1, 1, 1, 1, 1]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 1, 1, 1, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 1, 1, 1, 1]
        ]
    }
  , 'G' : {
        'pattern' : [
            [0, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 0]
          , [1, 0, 1, 1, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [0, 1, 1, 1, 0]
        ]
    }
  , 'L' : {
        'pattern' : [
            [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 1, 1, 1, 1]
        ]
    }
  , 'M' : {
        'pattern' : [
            [1, 0, 0, 0, 0, 0, 0, 0, 1]
          , [1, 0, 0, 0, 0, 0, 0, 0, 1]
          , [1, 0, 1, 0, 0, 0, 1, 0, 1]
          , [1, 0, 0, 0, 1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 0, 0, 0, 0, 1]
          , [1, 0, 0, 0, 0, 0, 0, 0, 1] 
          , [1, 0, 0, 0, 0, 0, 0, 0, 1] 
        ]
      , 'n' : 9
    }
  , 'O' : {
        'pattern' : [
            [0, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [0, 1, 1, 1, 0]
        ]
      , 'block' : '#'
    }
  , 'P' : {
        'pattern' : [
            [1, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 1, 1, 1, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
        ]
    }
  , 'R' : {
        'pattern' : [
            [1, 1, 1, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 1, 1, 1, 0]
          , [1, 0, 1, 0, 0]
          , [1, 0, 0, 1, 0]
          , [1, 0, 0, 0, 1]
        ]
    }
  , 'S' : {
        'pattern' : [
            [0, 1, 1, 1, 1]
          , [1, 0, 0, 0, 0]
          , [1, 0, 0, 0, 0]
          , [0, 1, 1, 1, 0]
          , [0, 0, 0, 0, 1]
          , [0, 0, 0, 0, 1]
          , [1, 1, 1, 1, 0]
        ]
    }
  , 'S2' : {
        'pattern' : [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          , [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          , [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
          , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
          , [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
          , [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
      , 'm' : 15
      , 'n' : 18
      , 'block' : 'o'
    }
  , 'T' : {
        'pattern' : [
            [1, 1, 1, 1, 1]
          , [0, 0, 1, 0, 0]
          , [0, 0, 1, 0, 0]
          , [0, 0, 1, 0, 0]
          , [0, 0, 1, 0, 0]
          , [0, 0, 1, 0, 0]
          , [0, 0, 1, 0, 0]
        ]
    }
  , 'U' : {
        'pattern' : [
            [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [0, 1, 1, 1, 0]
        ]
    }
  , 'X' : {
        'pattern' : [
            [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
          , [0, 1, 0, 1, 0]
          , [0, 0, 1, 0, 0]
          , [0, 1, 0, 1, 0]
          , [1, 0, 0, 0, 1]
          , [1, 0, 0, 0, 1]
        ]
    }
  , 'Z' : {
        'pattern' : [
            [1, 1, 1, 1, 1, 1, 1]
          , [0, 0, 0, 0, 0, 1, 0]
          , [0, 0, 0, 0, 1, 0, 0]
          , [0, 0, 0, 1, 0, 0, 0]
          , [0, 0, 1, 0, 0, 0, 0]
          , [0, 1, 0, 0, 0, 0, 0] 
          , [1, 1, 1, 1, 1, 1, 1]
        ]
      , 'n' : 7
    }
}

print('Affichage de lettre sous forme de pattern')
#for c in ['A', 'D', 'E', 'G', 'L', 'M', 'O', 'P', 'S']:
for c in 'ADEGLMOPSTUXZ':
    #print(c)
    print()
    print_letter_from_pattern(**letters_pattern[c])
    if c == 'S':
        print_letter_from_pattern(**letters_pattern[c+'2'])
