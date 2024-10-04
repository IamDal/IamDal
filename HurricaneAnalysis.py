# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000, "B": 1000000000}

def damages_as_float(conversion: dict, 
                     damage_as_str: list) -> list:
    
    damage_as_float: list = []
    for record in damage_as_str:
        if record != 'Damages not recorded':
            value = record.strip('MB')                          
            record = float(value) * conversion[record[-1]]      
        damage_as_float.append(record)                      
    return damage_as_float

# test function by updating damages
updated_damages = damages_as_float(conversion, damages)

# 2 
# Create a Table
data_list = [names, months, years, max_sustained_winds, 
             areas_affected, updated_damages, deaths]
columns = ["Name","Month", "Year", "Max_sustained_wind", 
           "Areas_affected", "Updated_damages", "Deaths"]

def make_dictionary(keys: list, columns: list, data: list) -> dict:
    hurricanes: dict = {}

    for key, *records in zip(keys, *data):
        hurricanes[key] = dict(zip(columns, records))
    return hurricanes

# Create and view the hurricanes dictionary
hurricanes = make_dictionary(data_list[0],columns,data_list)
print(hurricanes)

# 3
# Organizing by Year
def hurricanes_by_year(dictionary: dict) -> dict:
    dictionary_by_year: dict = {}
    
    for value in dictionary.values():
        year = value['Year']
        if not dictionary_by_year.get(year):
            dictionary_by_year[year] = []
        dictionary_by_year[year].append(value)
    return dictionary_by_year

# create a new dictionary of hurricanes with year and key
yearly_hurricanes = hurricanes_by_year(hurricanes)

# 4
# Counting Damaged Areas
def count_affected_areas(dictionary: dict) -> dict:
    affected_areas: dict = {}
    for value in dictionary.values():
        areas = value['Areas_affected']
        for area in areas:
            if not affected_areas.get(area):
                affected_areas[area] = 0
            affected_areas[area] += 1
    return affected_areas
# create dictionary of areas to store the number of hurricanes involved in
affected_areas = count_affected_areas(hurricanes)
print(affected_areas)

# 5 
# Calculating Maximum Hurricane Count
def most_affected_area(dictionary: dict) -> dict:
    keys, values = zip(*dictionary.items())
    max_value_index = list(values).index(max(values))
    area = list(keys)[max_value_index]
    count = dictionary[area]
    return {area : count}

# find most frequently affected area and the number of hurricanes involved in
top_affected_area = most_affected_area(affected_areas)
print(top_affected_area)

# 6
# Calculating the Deadliest Hurricane
def deadliest(dictionary: dict) -> dict:
    max_mortality = {'Name':0}
    for value in dictionary.values():
        key = list(max_mortality.keys())
        if max_mortality[key[0]] < value['Deaths']:
            max_mortality = {value['Name'] : value['Deaths']}
    return max_mortality

# find highest mortality hurricane and the number of deaths
deadliest_storms = deadliest(hurricanes)
print(deadliest_storms)

# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000, 4: 10000} 
def hurricanes_by_mortality(scale: dict, dictionary: dict) -> dict:
    by_mortality = {key: [] for key in scale}

    for values in dictionary.values():
        for key in mortality_scale.keys():
            if values['Deaths'] <= mortality_scale[key]:
                by_mortality[key].append(values) 
                break
        else:
            by_mortality[len(mortality_scale)-1].append(values)
    return by_mortality

# categorize hurricanes in new dictionary with mortality severity as key
hurricane_mortality = hurricanes_by_mortality(mortality_scale, hurricanes)
print(hurricane_mortality)

# 8 Calculating Hurricane Maximum Damage
# find highest damage inducing hurricane and its total cost
def max_damage(dictionary: dict) -> dict:
    max_damage_storm = {'Name':0}
    for name, value in dictionary.items():
        key = list(max_damage_storm.keys())
        if value['Updated_damages'] == 'Damages not recorded':
            continue
        if max_damage_storm[key[0]] < value['Updated_damages']:
            max_damage_storm = {name:value['Updated_damages']}
    return max_damage_storm

highest_damage = max_damage(hurricanes)
print(highest_damage)

# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0, 1: 100000000, 2: 1000000000, 3: 10000000000, 4: 50000000000}

def hurricanes_by_damage(damage_scale: dict, dictionary: dict) -> dict:   
    by_mortality: dict= {key: [] for key in damage_scale}

    for values in dictionary.values():
        if values['Updated_damages'] == 'Damages not recorded':
            by_mortality[0].append(values)
            continue
        for key in damage_scale.keys():
            if values['Updated_damages'] <= damage_scale[key]:
                by_mortality[key].append(values) 
                break
        else:
            by_mortality[len(damage_scale)-1].append(values)
    return by_mortality

# categorize hurricanes in new dictionary with damage severity as key
hurricane_damage = hurricanes_by_damage(damage_scale,hurricanes)
print(hurricane_damage)
