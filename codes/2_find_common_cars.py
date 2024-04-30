obj = {
    "Delhi": ['BMW', 'VOLKSWAGEN', 'MARUTI', 'TATA'],
    "Bangalore": ['BMW', 'MG', 'HONDA', 'AUDI'],
    "Chennai": ['MG', 'HONDA', 'TOYOTA', 'MAHINDRA'],
    "Chandigarh": ['MG', 'HONDA', 'AUDI']
}

d = {}

for city, companies in obj.items():
    for company in companies:
        if company not in d:
            d[company] = [city]
        else:
            d[company].append(city)

print(d)