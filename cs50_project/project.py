import requests
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import webbrowser
from datetime import date


headers = {
    "x-rapidapi-key": "14656dad08msh0e30e09547ffe31p1c1337jsna4dc6785c261",
    "x-rapidapi-host": "mma-api1.p.rapidapi.com"
}


def main():
    window = Tk()
    window.geometry('623x873')
    window.resizable(False, False)
    window.title('my MMApp')

    # Background Image Display
    img = ImageTk.PhotoImage(file='/workspaces/137717808/cs50_project/images/blackbelt.png', master=window)
    img_bg = Label(window, image=img)
    img_bg.place(relheight=1, relwidth=1)

    # Todays Date
    todays_label = Label(window, text=f'{todays_date()}', bg='white', fg='black')
    todays_label.pack()

    # Search Fighter Label
    lf = LabelFrame(window)
    search_fighter_label = Label(lf, text='Search Fighter: ', bg='white', fg='black', font=('helvitica', 10))
    search_fighter_label.grid(row=0, column=0)
    lf.place(x=10, y=50)

    # Insert fight Name Widget
    fight_name = StringVar()
    search_entry = Entry(lf, textvariable=fight_name, bg='white', fg='black', bd=0, width=15)
    search_entry.grid(row=0, column=1)

    # Display Button to search fighter info
    search_button = Button(window, text='Search',
                           bg='white', fg='black',
                           activebackground='red', activeforeground='black',
                           command=lambda: search_fighter(fight_name.get()), relief='raised')
    search_button.place(x=530, y=48)


    # Pound4Pound Rankings display
    p4p_lf = LabelFrame(window)
    p4p_label = Label(p4p_lf, text='P4P Rankings: ', bg='white', font=('helvitica', 10))
    p4p_lf.place(x=10, y=100)
    p4p_label.grid(row=1, column=1)

    # P4P Entry To Select Gender
    gender = StringVar()
    gender_box = ttk.Combobox(p4p_lf, textvariable=gender, width=10)
    gender_box.set('  Mens')
    gender_box['values'] = ('Mens', 'Womens')
    gender_box.grid(row=1, column=2)

    #P4P Button
    p4p_button = Button(window, text='Search',
                        bg='white', fg='black',
                        activebackground='red', activeforeground='black',
                        command=lambda: pound4pound_rankings(gender.get()), relief='raised')
    p4p_button.place(x=530, y=98)

    # Upcoming Events Label
    lblframe = LabelFrame(window)
    upcoming_events_label = Label(lblframe, text='Past - UpComing Events: ', bg='white',bd= 0, font=('helvitica',10))
    upcoming_events_label.grid(row=1, column=1)
    lblframe.place(x=10, y=150)

    # Combobox Widget for User to Select A Year
    year = StringVar()
    search_year = ttk.Combobox(lblframe, textvariable=year, width=7)
    search_year.set('  Year')
    search_year['values'] = ('2018', '2019', '2020', '2021', '2022', '2023', '2024')
    search_year['state'] = 'read only'
    search_year.grid(row=1, column=2)

    # Combobox Button Activates Function
    upcoming_events_button = Button(window, text='Search',
                           bg='white', fg='black',
                           activebackground='red', activeforeground='black',
                           command=lambda: upcoming_events(year.get()), relief='raised')
    upcoming_events_button.place(x=530, y=150)

    # Get The Last Seven Events Of The Year And Display The Next Event
    next_event = Label(window, text='Coming Up Next...',bg='white', fg='black', font=('helvitica', 14))
    next_event.place(x=10, y=550)

    # Display Next Event On Home Page
    next_event = Label(window, text=f'{coming_up_next()}',bg='white', fg='black', font=('helvitica', 14))
    next_event.place(x=10, y=580)

    # Display How to Watch button
    how_to_button = Button(window, text='Latest News', bg='red',fg='black', activebackground='#363636',activeforeground='white', command=related_news)
    how_to_button.place(x=10, y=620)

    # Exit Button
    cancel_button = Button(window, text='EXIT',bg='red', activebackground='white', command=window.quit, padx=55, pady=5, relief='raised')
    cancel_button.place(x=460, y=645)

    window.mainloop()



def todays_date():
    ''' Return The Today's Date  '''
    today = date.today()
    f_today = today.strftime('%A, %B %d, %Y')
    return f_today



def coming_up_next():
    ''' Display The Next Event Coming Up On the Home Screen '''
    try:
        # Search News For Next Event
        url = "https://mma-api1.p.rapidapi.com/getEventId"
        querystring = {"year": "2024"}
        response = requests.get(url, headers=headers, params=querystring)
        events = response.json()['result']

        # Loop Through each event in the list
        for event in events:
            next_event = events[-2:]
        up_next = next_event[0]['event']

        return up_next

    except requests.exceptions.ConnectionError:
        return 'An ERROR Occured'


def related_news():
    ''' Get Next Event '''
    try:
        # Requests api For News On PPV Event
        url = "https://mma-api1.p.rapidapi.com/news"
        response = requests.get(url, headers=headers)

        # Return Link In A webbrowser
        link = response.json()[0]['link']
        webbrowser.open(link)

    except requests.exceptions.ConnectionError:
        return 'CONNECTION ERROR! Please Try Again Later'


def search_fighter(fighter):
    ''' Search for Fighter And Return URL Info '''
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

    except KeyError:
        return 'ERROR! {} Not Found'.format(fighter)




def pound4pound_rankings(gender):
    ''' Get Men & Women's Pound4Pound Top 10 Rankings '''

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


def upcoming_events(selected_year):
    ''' Get UFC Event Dates For The Year '''

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
        new_window.geometry('520x600')

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
        exit_button.place(x=440, y=560)

    except requests.exceptions.ConnectionError:
        return 'CONNECTION ERROR! Please Try Again Later'


if __name__ == '__main__':
    main()
