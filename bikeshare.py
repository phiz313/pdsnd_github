import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citylist = ['chicago','new york city', 'washington']
monthlist = ['january', 'february', 'march', 'april', 'may', 'june', 'july',
              'august', 'september', 'october', 'november', 'december']
daylist = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print('This will be fun!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    while True:

        city = input("What city do you want to explore data on (Chicago, New York City, or Washington? ").lower()
        if city in citylist:
            break

    # TO DO: get user input for month (all, january, february, ... , june)


    while True:
        month = input("What month do you want to explore data on (January/February/etc) ? ").lower()
        if month in monthlist:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("What day of the week do you want data for (Sunday, Monday, etc) or ALL Days? ").lower()
    while day not in daylist:
        print ("Invalid input. ")
        day = input("What day of the week do you want data for (Sunday, Monday, etc) or ALL Days? ").lower()


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
    df['hour'] = df['Start Time'].dt.hour

    if day != 'all':
        df=df[ df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popmonth = df['month'].value_counts().idxmax()
    print (str(popmonth) + ' is the most popular month.')

    # TO DO: display the most common day of week
    popday = df['day_of_week'].value_counts().idxmax()
    print (str(popday) + ' is the most popular day.')

    # TO DO: display the most common start hour
    pophour = df['hour'].value_counts().idxmax()
    print (str(pophour) + ' is the most popular hour.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_start_station = df['Start Station'].value_counts().idxmax()
    print('The most common start station is ' + pop_start_station + ' .')

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].value_counts().idxmax()
    print('The most common ending station is ' + pop_end_station + ' .')

    # TO DO: display most frequent combination of start station and end station trip
    pop_combo = df[['Start Station','End Station']].mode().loc[0]
    print ('The most popular combination of start/end stations are {} and {} '.format(pop_combo[0],pop_combo[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print ('Total travel time: ' + str(total_travel))

    # TO DO: display mean travel time
    avg_travel = df['Trip Duration'].mean()
    print ('Mean travel time: ' + str(avg_travel))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Types :')
    user_type = df['User Type'].value_counts()
    print (user_type )

    # TO DO: Display counts of gender
    print('Count of gender: ')
    try:
        gender_count = df['Gender'].value_counts()
        print (gender_count)
    except:
        print ('No gender data for selected city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        birth = df['Birth Year']
        early_year=birth.min()
        print('The earliest birth year is '+str(early_year) +' .')
        recent_year=birth.max()
        print('The most recent birth year is '+str(recent_year) +' .')
        common_year=birth.value_counts().idxmax()
        print('The most common birth year is '+str(common_year) +' .')
    except:
        print('No birthdate data for selected city.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def rawdata(df):
    x=0
    y=5
    while True:
        show = input ('Would you like to see raw data (yes or no)? ').lower()
        if show == 'yes':
            print(df.iloc[x:y])
            x += 5
            y += 5
        elif show == 'no':
            break
        else:
            return rawdata(df)













def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
