if __name__ == '__main__':
  
  import scheduling
  import knapsack
  import platforms

  print('\n' + ('-'*50) + '\nlab08\n' + ('-'*50))
  
  while True:  
    
    print()
    print('1. No conflict scheduling')
    print('2. Knapsack Problem')
    print('3. Fractional Knapsack')
    print('4. Platform problem')
    print('5. Exit')
    c = int(input('?: '))
    
    if c==1:
      no_conflict = scheduling.schedule(scheduling.get_activities())
      print('-'*50)
      print('Number of non conflicting activities:',len(no_conflict))
      print('List: ' + ','.join(x['name'] for x in no_conflict))
    
    elif c==2 or c==3:
      items = knapsack.get_list()
      w = int(input('Knapsack capacity: '))
      print('-'*50)
      if c==2: 
        selected = knapsack.knapsack(items,w)
        print('Value of knapsack: ' + 
          str(sum(item['value'] for item in selected)))
        print('Weight of knapsack: ' + 
          str(sum(item['weight'] for item in selected)))
        print('List: ' + 
          ','.join(str((item['value'],item['weight'])) for item in selected))
      elif c==3: 
        selected = knapsack.fractional_knapsack(items,w)
        print('Value of fractional-knapsack: ' + 
          str(sum(item['value'] for item in selected)))
        print('Weight of fractional-knapsack: ' + 
          str(sum(item['weight'] for item in selected)))
        print('List: ' + 
          ','.join(str((item['value'],item['weight'])) for item in selected))

    elif c==4:
      arr = platforms.get_arrivals()
      dep = platforms.get_departures()
      plats = platforms.min_platforms(arr,dep)
      print('Minimum platforms required:',plats)
    
    elif c==5: break
    else: print('Invalid')

    print('-'*50)
  
  print('bye.')