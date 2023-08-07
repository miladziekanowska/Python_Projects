import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adultdata.csv')
    df.head()

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df.loc[df['sex'] == 'Male', 'age'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    high_ed = ['Bachelors', 'Masters', 'Doctorate']
    higher_education = df[df['education'].isin(high_ed)]
    lower_education = df.drop(higher_education.index)

    # percentage with salary >50K
    higher_education_rich = len(higher_education.loc[higher_education['salary'] == '>50K']) \/ len(higher_education.index)
    lower_education_rich = len(
        lower_education.loc[lower_education['salary'] == '>50K']) / len(lower_education.index)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[(df['hours-per-week'] == min_work_hours)
                             & (df['salary'] == '>50K')])

    rich_percentage = num_min_workers / len(df[df['hours-per-week'] == min_work_hours])

    # What country has the highest percentage of people that earn >50K?
    df_rich = df.loc[df['salary'] == '>50K']
    countries = df['native-country'].unique()
    rich_percentage = {}

    for country in countries:
        rich_percentage[country] = len(df_rich[df_rich['native-country'] == country]) / len(df[df['native-country'] == country])

    highest_earning_country_percentage = max(list(rich_percentage.values()))
    highest_earning_country = next(
        key for key, value in rich_percentage.items()
        if value == highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.
    df_india = df.loc[(df['native-country'] == 'India')
                        & (df['salary'] == '>50K')]
    top_IN_occupation = df_india.groupby('occupation').count().sort_values(by='salary', ascending=False).iloc[0].name


    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(
          f"Percentage with higher education that earn >50K: {higher_education_rich}%"
        )
        print(
          f"Percentage without higher education that earn >50K: {lower_education_rich}%"
        )
        print(f"Min work time: {min_work_hours} hours/week")
        print(
          f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
        )
        print("Country with highest percentage of rich:", highest_earning_country)
        print(
          f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
        )
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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
      }
