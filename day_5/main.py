# Level 1
list1 = []
list2 = ["Japan", "UK", "USA", "Pakistan", "UAE", "Iran", "Iraq"]
print(len(list2))
print(list2[0])
print(list2[3])
print(list2[6])
mixed_data_types = ["huzaifa", 16, 1.60, False, "Mianwali"]
print(mixed_data_types)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[3])
print(it_companies[6])
it_companies[1], it_companies[2] = "Microsoft", "Google"
print(it_companies)
it_companies.append("Lenovo")
print(it_companies)
it_companies.insert(5, "Nvidia")
print(it_companies)
it_companies[5] = it_companies[5].upper()
print(it_companies)
print("NVIDIA" in it_companies)
it_companies.sort(reverse=True)
print(it_companies)
print(it_companies[0:3])
print(it_companies[6:9])
print(it_companies[3:6])
it_companies.pop(0)
print(it_companies)
it_companies.remove("IBM")
print(it_companies)
it_companies.remove("Amazon")
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

# Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
minAge = ages[0]
maxAge = ages[len(ages)-1]
print(minAge)
print(maxAge)
ages.insert(0, minAge)
ages.insert(10, maxAge)
print(ages)
median = (ages[5] + ages[6]) // 2
print(median)
average = sum(ages) / len(ages)
print(average)
_range = maxAge - minAge
print(_range)
minAverage = abs(minAge - average)
maxAverage = abs(maxAge - average)

# Countries
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau','Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya','Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania','Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands','New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Poland','Portugal','Qatar','Romania','Russia','Rwanda','Saint Kitts and Nevis','Saint Lucia','Saint Vincent','Samoa','San Marino','Sao Tome and Principe','Saudi Arabia','Senegal','Serbia and Montenegro','Seychelles','Sierra Leone','Singapore','Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','Spain','Sri Lanka','Sudan','Suriname','Swaziland','Sweden','Switzerland','Syria','Taiwan','Tajikistan','Tanzania','Thailand','Togo','Tonga','Trinidad and Tobago','Tunisia','Turkey','Turkmenistan','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','Uruguay','Uzbekistan','Vanuatu','Vatican City','Venezuela','Vietnam','Yemen','Zambia','Zimbabwe',];
print(countries[(len(countries) // 2)])
first_half = countries[0:len(countries) // 2]
print(first_half)
second_half = countries[len(countries) // 2:]
print(second_half)

other_country = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
country1, country2, country3, *scandic = other_country
print(country1)
print(country2)
print(country3)
print(scandic)