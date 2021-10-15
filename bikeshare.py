import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
# TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_abbreviations = ['chi', 'ny', 'w']
    while True:
        city = input('Kindly specify a city by typing chicago or new york city or washington: \n\n').lower()
        if city in CITY_DATA.keys():
            break
        elif city.lower() == 'new york': #if the user forgot to add city to new york as it's a common mistake between users
            print('\nPlease notify that the city you typed called new york city, So retype it again right this time: \n')
        elif city in city_abbreviations: #if the user input was abbreviations of the name as it's a common mistake between users
            print('\nPlease notify that city abbreviation\'s is not allowed, Retype city full name!\n')
        elif city.lower() == 'newyorkcity': #if user's input was newyorkcity without any spaces as it's a common mistake between users
            print('\nPlease notify that the city you typed called new york city with spaces between words, So retype it again right this time: \n')
        else:                            #if user printed any other things like wrong name or used speical chracters like space _ + = ~
            print('\nThats invalid input....\n\nplease choose one of the three cities chicago or new york city or washington.\n')         
# TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    months_abbreviations = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug']
    while True:
        month = input('\n\nTo filter data by a particuler month, please type the month or all for not filtering by month: \n-january\n-february\n-march\n-april\n-may\n-june\n-all\n\n').lower()
        if month in months:
            break
        elif month in months_abbreviations:
            print('\nPlease notify that months abbreviation\'s is not allowed, Retype month full name!\n')
        else:                            #if the user input was abbreviations of the name as it's a common mistake between users  
            print('\nThats invalid input....\n\n\nplease choose one of the six  months listed to filter with or use no filter\n')
# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday', 'all']
    days_abbreviations = ['mon', 'tu', 'tue', 'tues', 'wed', 'th', 'thu', 'thur', 'thurs', 'fri', 'sat', 'sun']
    while True:
        day = input('\n\nTo filter data by a particuler day, please type the day or all for not filtering by day: \n-saturday\n-sunday\n-monday\n-tuesday\n-wednesday\n-thursday\n-friday\n-all\n\n').lower()
        if day in days:
            break
        elif day in days_abbreviations:   #if the user input was abbreviations of the name as it's a common mistake between users
            print('\nPlease notify that day abbreviation\'s is not allowed, Retype day full name!\n')                           
        else:
            print('\nThats invalid input....\n\n\nplease choose one of the seven days listed to filter with or use no filter\n')       
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #loading data of the city chosen by user into dataframe
    df = pd.read_csv(CITY_DATA[city])
    #converting the start time clomn from object (string) to datetime object so as we can use datetime  Attributes and methonds to extract month coulmn and day to filter with them
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #extracting month and day into new columns and days into new column 'month_name' and 'day_name' are methods in pandas datetime (https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.DatetimeIndex.html) as it's in this link
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #filtering data city with user inputs filter by moth and day:
    if month != 'all':
        df = df[df['month'] == month.title()]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating statistics of The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]     
    print('Most common Month is: ', most_common_month )
    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most common Day is: ', most_common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('Most common Hour is: ', most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most popular Start station is: ', popular_start_station)
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most popular End Station is ', popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_trip_start_end = (df['Start Station'] + ' To ' + df['End Station']).mode()[0]
    print('Most popular Trip from star to end: ', popular_trip_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time in seconds is : ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time in seconds is : ', mean_travel_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts().to_frame()
    print(user_type_count)
    # TO DO: Display counts of gender
    try:
        most_common_gender = df['Gender'].value_counts().to_frame()
        print(most_common_gender)
    # TO DO: Display earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        print('\nEarliest birth year is : ', int(earliest_birth_year))
        most_recent_birth_year = df['Birth Year'].max()
        print('\nMost recent birth year is : ', int(most_recent_birth_year))
        most_common_birth_year = df['Birth Year'].mode()[0]
        print('\nMost common birth year is : ', int(most_common_birth_year))
    except KeyError:
        print('\nGender and Birth year data is only available in \'chicago\' and \'new york city\'')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_raw_data(city):
    ''' Display raw data for users input based on his choice to see it or not'''
    print('\nRaw Data is available to be checked!\n')
    user_display_raw = input('Do you want to see the available raw data for the first 5 rows?\nPlease type Yes if you want to see or No\n').lower()
    while user_display_raw not in ('yes', 'no'):
        print('\nThat\'s invalid input, Please answer the question with Yes or No!')
        user_display_raw = input('\nDo you want to see the available raw data for the first 5 rows?\nPlease type Yes if you want to see or No\n').lower()
    while user_display_raw == 'yes':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize = 5): #chunk in data frame info https://janakiev.com/blog/python-pandas-chunks/
                print(chunk)
                user_display_raw = input('\nDo you want to see the available raw data for the Next 5 rows?\nPlease type Yes if you want to see or No\n').lower()
                if user_display_raw == 'no':
                    print('\nSee you next time.')
                    break
                while user_display_raw not in ('yes', 'no'):
                    print('\nThat\'s invalid input, Please answer the question with Yes or No!')
                    user_display_raw = input('\nDo you want to see the available raw data for the Next 5 rows?\nPlease type Yes if you want to see or No\n').lower()
                if user_display_raw == 'no':
                    print('\nSee you next time.')
                    break
            break
        except KeyboardInterrupt:
            print('\nSee you next time.')
            
            
def main():
    while True:
        city, month, day = get_filters()
        print('You have selcted City: {}\nMonth filter: {}\nDay filter: {}\n\'Notify that all means no filter is used\''.format(city, month, day))
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
            
if __name__ == "__main__":
	main()