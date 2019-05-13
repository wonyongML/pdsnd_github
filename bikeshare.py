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

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to see data for Chicago, New York City, or Washington? : ")

    date_type = input("Would you like to filter the data by month, day, or not at all? (Type 'none' for no time fillter) : ")

    if date_type == 'month':
        month = input(" Which month - January, February, March, April, May, or June? : ")
        day='all'
    elif date_type =='day' :
        day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? : ")
        month='all'
    elif date_type == 'none':
        month = 'all'
        day='all'


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
    df =  pd.DataFrame(pd.read_csv(CITY_DATA[city.lower()]))
    df['Start Time'] =  pd.to_datetime(df['Start Time'],yearfirst=True)
    df['s_month'] = df['Start Time'].dt.month
    df['s_day_of_week'] = df['Start Time'].dt.weekday_name
    df['s_hour'] =df['Start Time'].dt.hour

    df['End Time'] =  pd.to_datetime(df['End Time'],yearfirst=True)
    df['e_month'] = df['End Time'].dt.month
    df['e_day_of_week'] = df['End Time'].dt.weekday_name
    df['e_hour'] =df['End Time'].dt.hour


    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1

        # filter by month to create the new dataframe
        df = df[df['month']==month.lower()]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['s_day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most popular month is {}.".format(df.s_month.mode()[0]))

    # display the most common day of week
    print("The most popular day is {}.".format(df.s_day_of_week.mode()[0]))

    # display the most common start hour
    print("The most popular start hour is {}.".format(df.s_hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    #start_time = time.time()

    # display most commonly used start station

    print("The most popular start station is {} .".format(df['Start Station'].mode()[0]))
    # display most commonly used end station

    print("The most popular end station is {} .".format(df['End Station'].mode()[0]))
    # display most frequent combination of start station and end station trip
    print("The most popular combination of start station and end station trip is {} . ".format((df['Start Station']+df['End Station']).mode()[0]))

    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    #start_time = time.time()

    # display total travel time ( Seconds)
    total_time = np.sum(df['Trip Duration'])
    print("The total time for traveling is {} hours {} miniutes {} seconds.".format(total_time/3600,total_time%3600/60,total_time%60))
    # display mean travel time
    mean_time=np.mean(df['Trip Duration'])
    print("The mean time for trabeling is {} hours {} miniutes {} seconds.".format(mean_time/3600,mean_time%3600/60,mean_time%60))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    #start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Type")
    print(user_types)
    # Display counts of gender
    gender_types = df['Gender'].value_counts()
    print("Gender")
    print(gender_types)

    # Display earliest, most recent, and most common year of birth
    oldest=df['Birth Year'].min()
    youngest = df['Birth Year'].max()
    common_year=df['Birth Year'].mode()[0]
    print("Oldest Customer was borned in {}".format(oldest))
    print("Youngeset customer was borned in {}".format(youngest))
    print("Common year of that customers were borned is {}".format(common_year))
    #print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
