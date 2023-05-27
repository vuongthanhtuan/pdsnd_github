import time
from datetime import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months_list ={'january': 1,
            'february': 2,
            'march': 3,
            'april': 4,
            'may': 5,
            'june' : 6
}
days_list = {
    'monday': 0,
    "tuesday": 1,
    "wednesday": 2,
    "thursday": 3,
    "friday": 4,
    "saturday":5,
    "sunday": 6
}
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
        city = input("Enter the city name: ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print('Not found the city name. Try again!')
            continue
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Enter the month: ").lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print('Not found the month')
            continue
        else:
            break
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day: ').lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'):
            print('Not found the day')
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
    if city == 'new york city':
        df=pd.read_csv("./new_york_city.csv")
    else: 
        df=pd.read_csv("./" + city + ".csv")
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.dayofweek
    df['hour'] =df['Start Time'].dt.hour
    if month !='all':
        df=df[df['month']==months_list[month]]
    if day != 'all':
        df=df[df['day']==days_list[day]]
    
    return df
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"\nThe most common month: {common_month}")
    # TO DO: display the most common day of week
    common_day =df['day'].mode()[0]
    print(f"\nThe most common day: {common_day}")

    # TO DO: display the most common start hour
    common_hour =df['hour'].mode()[0]
    print(f"\nThe most common start hour: {common_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mostStartStation = df['Start Station'].mode()[0]
    print(f"The most commonly used start station: {mostStartStation}")

    # TO DO: display most commonly used end station
    mostEndStation = df['End Station'].mode()[0]
    print(f"The most commonly used end station: {mostEndStation}")

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to')
    combination = df['Start To End'].mode()[0]
    print(f"The most frequent combination of start station and end station trip: {combination}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTravelTime=df['Trip Duration'].sum()
    print(f" the total travel time: {totalTravelTime}")

    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    minutes, seconds = divmod(average_duration, 60)
    if minutes >= 60:
        hours, minutes = divmod(minutes, 60)
        print(f"\nThe average trip duration is {hours}:{minutes}:{seconds}")
    else:
        print(f"\nThe average trip duration is {minutes}:{seconds}")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    countUserType = df['User Type'].value_counts()
    print(f"The counts of user types: {countUserType}")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        countGender = df['Gender'].value_counts()
        print(f"The counts of gender: {countGender}")
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nThe earliest year of birth: {earliest}\n\nThe most recent year of birth: {recent}\n\nThe most common year of birth: {common_year}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("\nWould you like to view 5 rows of individual trip data? Enter yes or no\n").lower()
    start_loc = 0
    while(view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_status=user_stats(df)
        print("this is line change:" user_status")
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        # this command is added for the final project

if __name__ == "__main__":
	main()
