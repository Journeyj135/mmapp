# **My MMApp**:

#### **<ins>Video Demo</ins>**:  https://youtu.be/76v4_tH6tCc

### **<ins>Decription</ins>**:

This is a simple mma app where you can:

1. Look Up A Fighter in the __UFC__
2. Search __UFC__ Pound4Pound Rankings
3. Check out past and upcoming events
4.  Get The Lastest news on upcoming events

+ <ins>SEARCH</ins>🔍: when looking up a fighter. The user can easily type in the name and press the search button, taking them directly to an _ESPN_ website with detailed info on a specific fighter.

+ <ins>POUND4POUND</ins>🏆: There is a Mens and Womend divsion listbox where a user has the option to check the pound for pound rankings of the *UFC*

+ <ins>EVENTS</ins>🎈: Search a list of past and upcoming events by year
    >Years Available: 2018-2024

+ <ins>NEWS</ins>📰: Get the lastest news on the next upcoming event, Where to watch and more.
___
# **Modules**:
This project required the following libraries:
- Request Library

- Tkinter

- from PIL- ImageTk

- webbrowser

- from datetime - date
___
# **Features**:

This app comes with:
- Date & Time
- 1 Search Entry Widget
- 4 Exit Buttons
- 1 News Button
- 2 Comboboxes
- 3 Search Buttons
- 5 Functions ⬇️
___
# Functions:
## 1. **<ins>todays_date Function</ins>**:

This funciton simply displays the current datetime at the top of the screen.

```python
def todays_date():
    today = date.today()
    f_today = today.strftime('%A, %B %d, %Y')
    return f_today
```

## 2. **<ins> related_news Function</ins>**:

This function gets the next event and displays on home screen

>[!IMPORTANT]
> When using related_news function. The next event must be manually changed to show the next event
```python
try:
        # Requests api For News On PPV Event
        url = "https://mma-api1.p.rapidapi.com/news"
        response = requests.get(url, headers=headers)

        # Return Link In A webbrowser
        link = response.json()[0]['link']
        webbrowser.open(link)

    except requests.exceptions.RequestException:
        return 'CONNECTION ERROR! Please Try Again Later'
```

## 3. **<ins>search_fighter function</ind>**:

This function searches any fighter on the **UFC** roster
```python
try:
        # Search For Athletes Data
        url = "https://mma-api1.p.rapidapi.com/search"
        querystring = {"query": fighter}
        response = requests.get(url, headers=headers, params=querystring)

        # Return Link in Webbrowser
        fighter_link = response.json()['players'][0]['link']
        webbrowser.open(fighter_link)

    except requests.exceptions.ConnectionError:
        return 'ERROR! Link To {} Not Found...Please Try Another Name'.format(fighter)
```
## 4. **<ins>pound4pound_rankings function</ins>**:

This function returns the Mens/Womens top10 Rankings.
```python
try:
        # Create A New Window
        new_window = Toplevel()
        new_window.geometry('500x530')
        new_window.title('Pound4Pound Rankings')
        new_window.config(bg='#363636')

        if gender == 'Mens':    # Fetch api Fpr Mens Rankings
            url = "https://mma-api1.p.rapidapi.com/rankings-ufc"
            response = requests.get(url, headers=headers)
            mens_rankings = response.json()['rankings'][0]['ranks']
            rank_number = [num['rank'] for num in mens_rankings]
            fighter_name = [name['name'] for name in mens_rankings]

            # Display Simple Design For Male Rankings
            rank_title = Label(new_window, text='Rank', bg='#363636', fg='white', font=('Arial', 12, 'underline'))
            rank_title.place(x=60, y=50)
            Name_title = Label(new_window, text='Name', bg='#363636', fg='white', font=('Arial', 12, 'underline'))
            Name_title.place(x=320, y=50)

            rankings_title = Label(new_window, text='Mens Rankings:', bg='#363636', fg='red', font=('Roman Text', 20, "italic"))
            rankings_title.place(x=120)
            rank_label = Label(new_window, text='\n\n'.join(rank_number[:10]), bg='#363636', fg='red', font=('Arial', 12))
            rank_label.place(x=75, y=90)
            fight_name_label = Label(new_window, text='\n\n'.join(fighter_name[:10]), bg='#363636', fg='white', font=('Arial', 12))
            fight_name_label.place(x=260, y=90)

            message = Label(new_window, text='*Rankings Subject To Change', bg='#363636', fg='white', font=('Arial', 8))
            message.place(x=150, y=510)
            exit_button = Button(new_window, text='EXIT', bg='red',fg='black', activebackground='#363636',activeforeground='white', command=quit)
            exit_button.place(x=435, y=495)


        elif gender == 'Womens':    # Fetch api Of Womens Rankings
            url = "https://mma-api1.p.rapidapi.com/rankings-ufc"
            response = requests.get(url, headers=headers)
            womens_rankings = response.json()['rankings'][9]['ranks']
            womens_p4p = [rank for rank in womens_rankings]
            womens_rank_number = [women['rank'] for women in womens_p4p]
            womens_name = [name['name'] for name in womens_p4p]

            # Display Simple Design For Female Rankings Page
            rank_title = Label(new_window, text='Rank', bg='#363636', fg='white', font=('Arial', 12, 'underline'))
            rank_title.place(x=60, y=50)
            name_title = Label(new_window, text='Name', bg='#363636', fg='white', font=('Arial', 12, 'underline'))
            name_title.place(x=300, y=50)

            womens_rankings_title = Label(new_window, text='Womens Rankings:', bg='#363636', fg='red', font=('Arial', 20,"italic"))
            womens_rankings_title.place(x=100)
            womens_rank_label = Label(new_window, text='\n\n'.join(womens_rank_number[:10]), bg='#363636', fg='red',font=('Arial', 12))
            womens_rank_label.place(x=75, y=85)
            display_rankings = Label(new_window, text='\n\n'.join(womens_name[:10]), bg='#363636', fg='white',font=('Arial', 12))
            display_rankings.place(x=240, y=85)

            message = Label(new_window, text='*Rankings Subject to Change', bg='#363636', fg='white', font=('Arial', 8))
            message.place(x=130, y=510)
            exit_button = Button(new_window, text='EXIT', bg='red',fg='black', activebackground='#363636',activeforeground='white', command=quit)
            exit_button.place(x=435, y=495)

    except requests.exceptions.ConnectionError:
        return 'CONNECTION ERROR! Please Try Again Later'
```
## 5. **<ins>upcoming_events function</ins>**:

This function returns the past/upcoming events.
```python
try:
        # Fetch api of Upcoming Events
        url = "https://mma-api1.p.rapidapi.com/getEventId"
        querystring = {"year": selected_year}
        response = requests.get(url, headers=headers, params=querystring)
        list_of_events = response.json()['result']

        # Grab The Last 10 Events and startdates Of Those Events
        zuffa_events = [event['event'] for event in list_of_events]
        ufc_dates = [date['startDate'][:10] for date in list_of_events]
        ufc_events = [event for event in zuffa_events if 'UFC' in event]

        # Open New Window
        new_window = Toplevel()
        new_window.config(bg='#363636')
        new_window.title('Events Page')
        new_window.geometry('500x600')

        # Display Simple Design Of Upcoming Events
        upcoming_events_title = Label(new_window, text='Past - UpComing Events', bg='#363636', fg='red', font=('Roman', 20))
        upcoming_events_title.place(x=75)
        date_title = Label(new_window, text='Dates', bg='#363636', fg='white', font=('helvitica',12, 'underline'))
        date_title.place(x=35, y=75)
        event_title = Label(new_window, text='Events', bg='#363636', fg='white', font=('helvitica',12, 'underline'))
        event_title.place(x=265, y=75)

        events = Label(new_window, text="\n\n".join(ufc_events[-10:]), bg='#363636', fg='white', font=('helvitica',12))
        events.place(x=145, y=120)
        dates = Label(new_window, text="\n\n".join(ufc_dates[-10:]), bg='#363636', fg='red', font=('helvitica',12))
        dates.place(x=10, y=120)
        message = Label(new_window, text='*Cards Subject to Change', bg='#363636', fg='white', font=('Arial', 8))
        message.place(x=150, y=570)
        exit_button = Button(new_window, text='EXIT', bg='red',fg='black', activebackground='#363636',activeforeground='white', command=quit)
        exit_button.place(x=425, y=550)

    except requests.exceptions.ConnectionError:
        return 'CONNECTION ERROR! Please Try Again Later'
```
___
# **Usage**:
### Example 1:
Output of *<ins>P4P function</ins>* when executed.


[![](/cs50_project/images/mens_rankings.png)]

### Example 2:
 Output of *<ins>search fighter function</ins>* when executed.

 (hey! thats me!).
[![](/cs50_project/images/espn.png)]

### Example 3:
Output of *<ins>upcoming_events function</ins>* when executed.
[![](/cs50_project/images/events.png)]
___
# **Images**:
Images used for this project:
[![](/cs50_project/images/blackbelt.png)]
___
# **acknowledgments:**
Thank you team cs50p for building an awsome course to learn web development.

It is quite challenging to go from one career to the next, especially when the two careers are quite different from one another. Had a blast with this course and plan to do more in hopes of changing careers from a professional mma fighter to a full time web developer.
