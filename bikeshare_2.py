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
    while True:
      city = input("please input the city you want from [chicago, new york city, washington]: ").lower()
      if city == 'chicago' or city == 'new york city' or city == 'washington':
        break
      else:
        print('Wrong City Name, please try again!')

    # get user input for month (all, january, february, ... , june)
    while True:
      selection_month = ['january','february', 'march','april', 'may', 'june','all']

      month = input("please input the Month you want from [january, february, ... , june] or all: ").lower()
      if month in selection_month:
        break
      else:
        print('Wrong Month Name, please try again!')

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
      selection_day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday','all']

      day = input("please input the Day you want from [monday, tuesday, ... , sunday] or all: ").lower()
      if day in selection_day:
        break
      else:
        print('Wrong Day Name, please try again!')


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
    # Creating a column for the month so we can filter it
    df['month'] = df['Start Time'].dt.month
    # Creating  a column for the day_of_week so we can filter it
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
      months = ['january','february', 'march','april', 'may', 'june','all']
      month = months.index(month) + 1
      df = df[df['month'] == month]
    if day != 'all':
      df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("The most common month : ",df['month'].mode()[0])

    # display the most common day of week
    print("The most common day of week : ",df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour : ", df['hour'].mode()[0])

    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(" The most commonly used start station: ", df['Start Station'].mode()[0])

    # display most commonly used end station
    print(" The most commonly used End station: ", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['combination'] =  df['Start Station'] + ' -- '+ df['End Station']
    print(" The most commonly used combination: ", df['combination'].mode()[0])

    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('The total for the travel time is :',df['Trip Duration'].sum())

    # display mean travel time
    print('The mean for the travel time is :',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % round((time.time() - start_time),5))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # Display counts of user types
    print('The Counts of the user types is :\n', df['User Type'].value_counts())
    if city != 'washington':
      # Removing the Nan values from the dataframe
      df.fillna(method = 'ffill', axis = 0, inplace = True)
      # Display counts of gender
      print('The Counts of the gender is :\n',df['Gender'].value_counts())

      # Display earliest, most recent, and most common year of birth
      print('Displaying the most recent year of birth: ',int(df['Birth Year'].sort_values().max()))
      print('Displaying the earlist year of birth: ',int(df['Birth Year'].sort_values().min()))
      print('Displaying the most common year of birth: ',int(df['Birth Year'].sort_values().mode()[0]))

      print("\nThis took %s seconds." % round((time.time() - start_time),5))
      print('-'*40)

def display_raw_data(df):
  """
  This function job is to display for the user the data for the city he chooses
  Returns:
  df - Pandas DataFrame containing city data
  """
  i = 5
  pd.set_option('display.max_columns',200)
  raw = input("Do you want to display some raw data? Yes/No ").lower()
  while True:
    if raw == 'no':
      break
    elif raw == 'yes':
      print(df[:i])
      raw = input("Do you want to dispaly more? Yes/No) ").lower()
      i += 5
    else:
      raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()


def main():
    flag = False
    while flag == False:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(df)
        while True:
          restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
          if restart == 'yes':
            break
          elif restart == 'no':
            flag = True
            break



if __name__ == "__main__":
	main()
