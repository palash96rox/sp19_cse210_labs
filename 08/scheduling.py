def schedule(activities):
  activities = sorted(activities, key=lambda x: x['end'])
  no_conflict = [activities[0]]
  for j in range(1,len(activities)):
    if activities[j]['start'] >= no_conflict[-1]['end']:
      no_conflict.append(activities[j])
  return no_conflict

def get_activities():
  n = int(input('Enter number of activities: '))
  print('For each activity, enter the following:')
  activities = []
  for i in range(n):
    activities.append({
      'name': input('name-'+str(i+1)+': '),
      'start': input('start-time-'+str(i+1)+': '),
      'end': input('end-time-'+str(i+1)+': ')
    })
  return activities

if __name__ == '__main__':
  activities = get_activities()
  no_conflict = schedule(activities)
  print('Number of non conflicting activities:',len(no_conflict))
  print('List: ' + ','.join(x['name'] for x in no_conflict))