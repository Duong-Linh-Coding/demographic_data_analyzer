import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    get_men=df[df['sex'] == 'Male']
    average_age_men = round(get_men['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education']=='Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100,1)


    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    q1 = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    q2 = df['salary'] == '>50K'

    higher_education_rich = round((q1 & q2).sum() / q1.sum() * 100, 1)
    lower_education_rich = round((~q1 & q2).sum() / (~q1).sum() * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[df['hours-per-week']==1])

    rich_percentage = round(len(df[(df['hours-per-week'] == 1) & (df['salary'] == '>50K')]) *100/num_min_workers,1)

    # What country has the highest percentage of people that earn >50K?
    rich_df = df[df['salary'] == '>50K']
    country_counts = df['native-country'].value_counts()
    rich_country_counts = rich_df['native-country'].value_counts()
    earning_country_percentage = (rich_country_counts / country_counts) * 100
    highest_earning_country = earning_country_percentage.idxmax()
    highest_earning_country_percentage = round(earning_country_percentage.max(),1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian=df[df['native-country']=='India']
    rich_indian = indian[indian['salary']=='>50K']
    top_IN_occupation = rich_indian['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
