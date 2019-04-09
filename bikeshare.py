import time
import pandas as pd
import numpy as np
from time import strptime

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
    
    while True:
        city = input("What city would you like to filter by? Chicago, New York City, or Washington? :").lower()  
        if city not in ('chicago', 'new york city', 'washington'):
            print('Invalid city')
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("What month would you like to filter for? (all, january, february, ... , june) :").lower()  
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('invalid month')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("What day of the week would you like to filter for? (all, sunday, monday, ... , saturday)  :").lower()  
        if day not in ('all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'):
            print('invalid day of the week')
            continue
        else:
            break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    print(df)

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("The most popular month is: ", popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("The most popular Start Day is: ", popular_day)


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most popular Start hour is: ", popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print("The most popular Start Station was: ", popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print("The most popular End Station was: ", popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['Full Trip'] = df['Start Station'] + ' to ' + df['End Station']
    popular_full = df['Full Trip'].mode()[0]
    print("The most popular full trip was: ", popular_full)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = sum(df['Trip Duration'])
    duration_days = total_travel_time // 86400
    duration_hours = (total_travel_time%86400) // 3600
    duration_minutes = (total_travel_time%3600) // 60
    duration_seconds = total_travel_time%60
    print("Total Travel Duration was {} day(s), {} hour(s), {} minute(s), and {} second(s).".format(duration_days, duration_hours, duration_minutes, duration_seconds))



    # TO DO: display mean travel time
    mean_duration = np.mean(df['Trip Duration'])
    mean_duration_hours = mean_duration // 3600
    mean_duration_minutes = (mean_duration%3600) // 60
    mean_duration_seconds = mean_duration%60
    print("The average trip duration was {} hour(s), {} minute(s), {} second(s).".format(mean_duration_hours, mean_duration_minutes, mean_duration_seconds))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print(user_count)
    print()


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print(gender_count)
    except KeyError:
        print("Calculating Gender Stats...")
        print()
        print("No gender data available for this query")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        oldest_by = int(df['Birth Year'].max())
        youngest_by = int(df['Birth Year'].min())
        common_by = int(df['Birth Year'].mode()[0])
        print()
        print("The oldest rider was born in {}".format(oldest_by))
        print("The youngest rider was born in {}".format(youngest_by))
        print("The most common birth year(s) were {}".format(common_by))
    except KeyError:
        print()
        print("No age data available for this query")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    ri1 = 0
    ri2 = 5
    while True:
        raw_input_prompt = input("Would you like to view 5 rows of raw data? Yes/No :").lower()
        if raw_input_prompt == "yes":
            print(df.iloc[ri1:ri2,:])
            ri1 = ri1 + 5
            ri2 = ri1 + 5
            continue
        else:
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
