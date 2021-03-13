def manhattan_distance(data_point1, data_point2):
    
    distance = abs(data_point1['TMAX'] - data_point2['TMAX']) + abs(data_point1['PRCP'] - data_point2['PRCP']) + abs(data_point1['TMIN'] - data_point2['TMIN'])
    
    return distance
    
def read_dataset(filename):
    
    data = []
    file = open(filename, "r")
    for x in file:
        line = x.split(" ")
        dataset = {}
        dataset['DATE'] = line[0]
        dataset['TMAX'] = float(line[2])
        dataset['PRCP'] = float(line[1])
        dataset['TMIN'] = float(line[3])
        dataset['RAIN'] = line[4].split('\n')[0]
        data.append(dataset)           
    
    return data

def majority_vote(nearest_neighbors):
    count_true = 0
    count_false = 0
    for i in nearest_neighbors:
        if i['RAIN'] == 'TRUE':
            count_true+=1
        else:
            count_false+=1
    if count_true >= count_false:
        return 'TRUE'
    else:
        return 'FALSE'
    

def k_nearest_neighbors(filename, test_point, k, year_interval):
    data = read_dataset(filename)
    time_temp = []
    
    """Taking account of only those within correct time interval"""
    for i in data:
        date1 = i['DATE'].split('-')
        year1 = int(date1[0])
        date2 = test_point['DATE'].split('-')
        year2 = int(date2[0])
        
        if year1 < (year2 + year_interval) and year1 > (year2 - year_interval):
            time_temp.append(i)
            
    m_distance = []
    index = 0
       
    """Calculating the manhattan distance of each in time_temp"""
    for i in time_temp:
        m_distance.append((manhattan_distance(test_point, i), index))
        index+=1
        
    k_neighbors = []
    
    if len(time_temp) == 0:
        return 'TRUE'
    
    else:
        m_distance.sort(key = lambda x: x[0])
        
        counter = 0
        for i in m_distance:
            k_neighbors.append(time_temp[i[1]])
            counter += 1
            if counter == k:
                break
                
        return majority_vote(k_neighbors)