import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
df.head(5)
clean_df = df.dropna()


#Question 1 : What college major has the highest mid-career salary? How much do graduates with this major earn?
mid_career_max = clean_df['Mid-Career Median Salary'].idxmax()
college_major_1 = clean_df['Undergraduate Major'].loc[mid_career_max]
salary_1 = clean_df['Mid-Career Median Salary'].loc[mid_career_max]

print(f"{college_major_1} has the highest mid-career salary and these graduates can expect to earn ${salary_1}")


#Question 2: Which college major has the lowest starting salary and how much do graduates earn after university?
start_career_min = clean_df['Starting Median Salary'].idxmin()
college_major_2 = clean_df['Undergraduate Major'].loc[start_career_min]
salary_2 = clean_df['Mid-Career Median Salary'].loc[start_career_min]

print(f"{college_major_2} has the lowest starting salary and these graduates can expect to earn ${salary_2}")

#Question 3: Which college major has the lowest mid-career salary and how much can people expect to earn with this degree?
mid_career_min = clean_df['Mid-Career Median Salary'].idxmin()
college_major_3 = clean_df['Undergraduate Major'].loc[mid_career_min]
salary_10_pct = clean_df['Mid-Career 10th Percentile Salary'].loc[mid_career_min]
salary_90_pct = clean_df['Mid-Career 90th Percentile Salary'].loc[mid_career_min]

print(f"{college_major_3} has the lowest mid-career salary and these graduates can expect to earn from ${salary_10_pct} to ${salary_90_pct}")