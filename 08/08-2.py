if __name__ == '__main__':
  
  import platforms

  print('\n' + ('-'*50) + '\nlab08-2\n' + ('-'*50))
  
  while True:  
    
    print()
    print('1. ???')
    print('2. Platform Problem')
    print('3. Exit')
    c = int(input('?: '))
    
    if c==1: pass
    elif c==2:
      arr = platforms.get_arrivals()
      print('Sorted arrival times:',arr)
      dep = platforms.get_departures()
      print('Sorted departure times:',dep)
      plats = platforms.min_platforms(arr,dep)
      print('Minimum platforms required:',plats)
    elif c==3: break
    else: print('Invalid')

    print('-'*50)
  
  print('bye.')