# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

spain_population        =47163418
switzerland_population  =8508698

#1 The language spoken the most in Switzerland is the same as in Spain.
spain_spoken_language = 74 / 100            #74% speaks spanish in spain        | 0% speak swiss
switzerland_spoken_language = 62.1 / 100    #62.1% speaks swiss in switzerland | 2.3% speak spanish
most_spoken_language = switzerland_spoken_language == spain_spoken_language
print(most_spoken_language)

#2 The most prevalent religion in Switzerland is the same as in Spain.
spain_religion = "Catholic"
switzerland_religion = "Catholic"
most_popular_religion = spain_religion == switzerland_religion
print (most_popular_religion)

#3 The name length of Spain's capital does not equal that of Switzerland.
spain_capital_name_length = "Madrid"
switzerland_capital_name_length = "Bern"
Capital_name_length = len(spain_capital_name_length) != len(switzerland_capital_name_length)
print (Capital_name_length)

#4 Switzerland's GDP is greater than Spain's GDP.
spain_gdp       = 1714860000000
switzerland_gdp = 590710000000
greater_gdp = switzerland_gdp > spain_gdp
print(greater_gdp)

#5 The population growth is less than 1% in Switzerland and Spain.
spain_pop_growth = 0.13
switzerland_pop_growth = 0.65
pop_growth = (spain_pop_growth or switzerland_pop_growth) < 1
print(pop_growth)

#6 At least one of the two countries has a population count of over 10 million.
ten_mil_pop = (spain_population or switzerland_population ) > 10000000
print(ten_mil_pop)

#7 Exactly one of the two countries has a population count of over 10 million.
exactly_mil_pop = (spain_population or switzerland_population ) > 10000000
print(exactly_mil_pop)
