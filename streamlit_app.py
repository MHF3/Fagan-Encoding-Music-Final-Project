import pandas as pd
import streamlit as st
import gspread
from datetime import datetime

@st.cache_resource
def get_worksheet():
    gc = gspread.service_account_from_dict(st.secrets['service_account_credentials'])
    sh = gc.open_by_key("1O_3tSNb1i4bk6a7YfH4mmlhRnBQJoN-0qCzKABkDBCM")
    worksheet = sh.worksheet('Form Responses 1')
    return worksheet

source_data = get_worksheet()

st.title('Beatles Recommendations')
st.write("Looking for your new favorite song? Want it to be a Beatles song? Specifically from the albums Revolver, Sgt. Pepper's Lonely Hearts Club Band, and/or Abbey Road? Then you're in luck! Simply enter in your ratings for the songs you know below, select the kind of output you want to see, and discover the perfect songs for you!")

st.header('Ratings')
st.write("Enter in your ratings for the songs you know! 7 means you really like the song, 1 means you really dislike the song; 0 represents an unrated song. If you've used this app before, please differentiate between previous ratings and any new ratings you're inputting for the first time.")

returning = st.checkbox("I've Used This App Before!")

songs = []
songs_new = []
for x in range (44):
    songs.append(None)
    songs_new.append(None)

if (returning):
    with st.expander('Previous Ratings'):
        with st.expander('Revolver'):
            songs[0] = st.slider('Taxman', 0, 7)
            songs[1] = st.slider('Eleanor Rigby', 0, 7)
            songs[2] = st.slider("I'm Only Sleeping", 0, 7)
            songs[3] = st.slider('Love You To', 0, 7)
            songs[4] = st.slider('Here, There and Everywhere', 0, 7)
            songs[5] = st.slider('Yellow Submarine', 0, 7)
            songs[6] = st.slider('She Said She Said', 0, 7)
            songs[7] = st.slider('Good Day Sunshine', 0, 7)
            songs[8] = st.slider('And Your Bird Can Sing', 0, 7)
            songs[9] = st.slider('For No One', 0, 7)
            songs[10] = st.slider('Doctor Robert', 0, 7)
            songs[11] = st.slider('I Want to Tell You', 0, 7)
            songs[12] = st.slider('Got to Get You Into My Life', 0, 7)
            songs[13] = st.slider('Tomorrow Never Knows', 0, 7)
        with st.expander("Sgt. Pepper's Lonely Hearts Club Band"):
            songs[14] = st.slider("Sgt. Pepper's Lonely Hearts Club Band", 0, 7)
            songs[15] = st.slider('With a Little Help From My Friends', 0, 7)
            songs[16] = st.slider('Lucy In the Sky with Diamonds', 0, 7)
            songs[17] = st.slider('Getting Better', 0, 7)
            songs[18] = st.slider('Fixing a Hole', 0, 7)
            songs[19] = st.slider("She's Leaving Home", 0, 7)
            songs[20] = st.slider('Being For the Benefit of Mr. Kite!', 0, 7)
            songs[21] = st.slider('Within You Without You', 0, 7)
            songs[22] = st.slider("When I'm Sixty-Four", 0, 7)
            songs[23] = st.slider('Lovely Rita', 0, 7)
            songs[24] = st.slider('Good Morning Good Morning', 0, 7)
            songs[25] = st.slider("Sgt. Pepper's Lonely Hearts Club Band (Reprise)", 0, 7)
            songs[26] = st.slider('A Day In the Life', 0, 7)
        with st.expander('Abbey Road'):
            songs[27] = st.slider('Come Together', 0, 7)
            songs[28] = st.slider('Something', 0, 7)
            songs[29] = st.slider("Maxwell's Silver Hammer", 0, 7)
            songs[30] = st.slider('Oh! Darling', 0, 7)
            songs[31] = st.slider("Octopus's Garden", 0, 7)
            songs[32] = st.slider("I Want You (She's So Heavy)", 0, 7)
            songs[33] = st.slider('Here Comes the Sun', 0, 7)
            songs[34] = st.slider('Because', 0, 7)
            songs[35] = st.slider('You Never Give Me Your Money', 0, 7)
            songs[36] = st.slider('Sun King', 0, 7)
            songs[37] = st.slider('Mean Mr. Mustard', 0, 7)
            songs[38] = st.slider('Polythene Pam', 0, 7)
            songs[39] = st.slider('She Came In Through the Bathroom Window', 0, 7)
            songs[40] = st.slider('Golden Slumbers', 0, 7)
            songs[41] = st.slider('Carry That Weight', 0, 7)
            songs[42] = st.slider('The End', 0, 7)
            songs[43] = st.slider('Her Majesty', 0, 7)
    with st.expander('New Ratings'):
        with st.expander('Revolver'):
            songs_new[0] = st.slider('Taxman', 0, 7, key=0)
            songs_new[1] = st.slider('Eleanor Rigby', 0, 7, key=1)
            songs_new[2] = st.slider("I'm Only Sleeping", 0, 7, key=2)
            songs_new[3] = st.slider('Love You To', 0, 7, key=3)
            songs_new[4] = st.slider('Here, There and Everywhere', 0, 7, key=4)
            songs_new[5] = st.slider('Yellow Submarine', 0, 7, key=5)
            songs_new[6] = st.slider('She Said She Said', 0, 7, key=6)
            songs_new[7] = st.slider('Good Day Sunshine', 0, 7, key=7)
            songs_new[8] = st.slider('And Your Bird Can Sing', 0, 7, key=8)
            songs_new[9] = st.slider('For No One', 0, 7, key=9)
            songs_new[10] = st.slider('Doctor Robert', 0, 7, key=10)
            songs_new[11] = st.slider('I Want to Tell You', 0, 7, key=11)
            songs_new[12] = st.slider('Got to Get You Into My Life', 0, 7, key=12)
            songs_new[13] = st.slider('Tomorrow Never Knows', 0, 7, key=13)
        with st.expander("Sgt. Pepper's Lonely Hearts Club Band"):
            songs_new[14] = st.slider("Sgt. Pepper's Lonely Hearts Club Band", 0, 7, key=14)
            songs_new[15] = st.slider('With a Little Help From My Friends', 0, 7, key=15)
            songs_new[16] = st.slider('Lucy In the Sky with Diamonds', 0, 7, key=16)
            songs_new[17] = st.slider('Getting Better', 0, 7, key=17)
            songs_new[18] = st.slider('Fixing a Hole', 0, 7, key=18)
            songs_new[19] = st.slider("She's Leaving Home", 0, 7, key=19)
            songs_new[20] = st.slider('Being For the Benefit of Mr. Kite!', 0, 7, key=20)
            songs_new[21] = st.slider('Within You Without You', 0, 7, key=21)
            songs_new[22] = st.slider("When I'm Sixty-Four", 0, 7, key=22)
            songs_new[23] = st.slider('Lovely Rita', 0, 7, key=23)
            songs_new[24] = st.slider('Good Morning Good Morning', 0, 7, key=24)
            songs_new[25] = st.slider("Sgt. Pepper's Lonely Hearts Club Band (Reprise)", 0, 7, key=25)
            songs_new[26] = st.slider('A Day In the Life', 0, 7, key=26)
        with st.expander('Abbey Road'):
            songs_new[27] = st.slider('Come Together', 0, 7, key=27)
            songs_new[28] = st.slider('Something', 0, 7, key=28)
            songs_new[29] = st.slider("Maxwell's Silver Hammer", 0, 7, key=29)
            songs_new[30] = st.slider('Oh! Darling', 0, 7, key=30)
            songs_new[31] = st.slider("Octopus's Garden", 0, 7, key=31)
            songs_new[32] = st.slider("I Want You (She's So Heavy)", 0, 7, key=32)
            songs_new[33] = st.slider('Here Comes the Sun', 0, 7, key=33)
            songs_new[34] = st.slider('Because', 0, 7, key=34)
            songs_new[35] = st.slider('You Never Give Me Your Money', 0, 7, key=35)
            songs_new[36] = st.slider('Sun King', 0, 7, key=36)
            songs_new[37] = st.slider('Mean Mr. Mustard', 0, 7, key=37)
            songs_new[38] = st.slider('Polythene Pam', 0, 7, key=38)
            songs_new[39] = st.slider('She Came In Through the Bathroom Window', 0, 7, key=39)
            songs_new[40] = st.slider('Golden Slumbers', 0, 7, key=40)
            songs_new[41] = st.slider('Carry That Weight', 0, 7, key=41)
            songs_new[42] = st.slider('The End', 0, 7, key=42)
            songs_new[43] = st.slider('Her Majesty', 0, 7, key=43)
else:
    with st.expander('Revolver'):
        songs[0] = st.slider('Taxman', 0, 7)
        songs[1] = st.slider('Eleanor Rigby', 0, 7)
        songs[2] = st.slider("I'm Only Sleeping", 0, 7)
        songs[3] = st.slider('Love You To', 0, 7)
        songs[4] = st.slider('Here, There and Everywhere', 0, 7)
        songs[5] = st.slider('Yellow Submarine', 0, 7)
        songs[6] = st.slider('She Said She Said', 0, 7)
        songs[7] = st.slider('Good Day Sunshine', 0, 7)
        songs[8] = st.slider('And Your Bird Can Sing', 0, 7)
        songs[9] = st.slider('For No One', 0, 7)
        songs[10] = st.slider('Doctor Robert', 0, 7)
        songs[11] = st.slider('I Want to Tell You', 0, 7)
        songs[12] = st.slider('Got to Get You Into My Life', 0, 7)
        songs[13] = st.slider('Tomorrow Never Knows', 0, 7)
    with st.expander("Sgt. Pepper's Lonely Hearts Club Band"):
        songs[14] = st.slider("Sgt. Pepper's Lonely Hearts Club Band", 0, 7)
        songs[15] = st.slider('With a Little Help From My Friends', 0, 7)
        songs[16] = st.slider('Lucy In the Sky with Diamonds', 0, 7)
        songs[17] = st.slider('Getting Better', 0, 7)
        songs[18] = st.slider('Fixing a Hole', 0, 7)
        songs[19] = st.slider("She's Leaving Home", 0, 7)
        songs[20] = st.slider('Being For the Benefit of Mr. Kite!', 0, 7)
        songs[21] = st.slider('Within You Without You', 0, 7)
        songs[22] = st.slider("When I'm Sixty-Four", 0, 7)
        songs[23] = st.slider('Lovely Rita', 0, 7)
        songs[24] = st.slider('Good Morning Good Morning', 0, 7)
        songs[25] = st.slider("Sgt. Pepper's Lonely Hearts Club Band (Reprise)", 0, 7)
        songs[26] = st.slider('A Day In the Life', 0, 7)
    with st.expander('Abbey Road'):
        songs[27] = st.slider('Come Together', 0, 7)
        songs[28] = st.slider('Something', 0, 7)
        songs[29] = st.slider("Maxwell's Silver Hammer", 0, 7)
        songs[30] = st.slider('Oh! Darling', 0, 7)
        songs[31] = st.slider("Octopus's Garden", 0, 7)
        songs[32] = st.slider("I Want You (She's So Heavy)", 0, 7)
        songs[33] = st.slider('Here Comes the Sun', 0, 7)
        songs[34] = st.slider('Because', 0, 7)
        songs[35] = st.slider('You Never Give Me Your Money', 0, 7)
        songs[36] = st.slider('Sun King', 0, 7)
        songs[37] = st.slider('Mean Mr. Mustard', 0, 7)
        songs[38] = st.slider('Polythene Pam', 0, 7)
        songs[39] = st.slider('She Came In Through the Bathroom Window', 0, 7)
        songs[40] = st.slider('Golden Slumbers', 0, 7)
        songs[41] = st.slider('Carry That Weight', 0, 7)
        songs[42] = st.slider('The End', 0, 7)
        songs[43] = st.slider('Her Majesty', 0, 7)

save = st.button('Save Ratings')

if save:
    with st.spinner('Saving...'):
        st.session_state.user_index = -1
        if (returning):
            old_row = []
            
            for o in range(44):
                if (songs[o] != 0 and songs[o] != None): old_row.append(str(songs[o]))
                else: old_row.append('')
            
            row = 2
            
            for row_number in range(1, source_data.row_count):

                if (old_row.__eq__(source_data.get_all_values()[row_number][1:])): break
                else: row += 1
            
            if (row == source_data.row_count + 1): st.write('No matching data found!')
            else:        
                alter_row = []
                alter_row.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
                
                for a in range(44):
                    if (songs_new[a] != 0 and songs_new[a] != None): alter_row.append(songs_new[a])
                    elif (songs[a] != 0 and songs[a] != None): alter_row.append(songs[a])
                    else: alter_row.append('')
                
                source_data.delete_rows(row)
                if (row == source_data.row_count + 1): source_data.append_row(alter_row)
                else: source_data.insert_row(alter_row, row)

                st.session_state.user_index = row - 2
                st.write('Saved!')
        else:
            new_row = []
            new_row.append(datetime.now().strftime("%m/%d/%Y %H:%M:%S"))

            for s in range(44):
                if (songs[s] != 0 and songs[s] != None): new_row.append(songs[s])
                else: new_row.append('')
            
            source_data.append_row(new_row)

            st.session_state.user_index = source_data.row_count - 2
            st.write('Saved!')

st.header('Output Type')

st.write("'Best New Song' will display the name of the song with the highest predicted rating that you haven't already listened to. 'Top N Songs' will list out an amount of songs, as determined by you, with the highest rating, whether that rating was given (you've listened to the song before) or predicted (you haven't listened to the song before). 'Raw Data' will display a dataframe of all the given ratings the app is using to make recommendations.")

output = st.selectbox('Desired Output', ['Best New Song', 'Top N Songs', 'Raw Data'])

if (output == 'Top N Songs'): n = st.number_input('N', 1, 44)

go = st.button('Produce Output')

if go:
    if (st.session_state.user_index == -1): st.write('You Need to Save Ratings First!')
    else:
        data = pd.DataFrame(source_data.get_all_records()).iloc[:, 1:]

        song_ratings = {}
        weight_values = []
        weight_rows = []
        row_index = 0

        for row in data.iterrows():
            differences = 0
            differences_count = 0
            
            for index in range(44):
                if (row[1][index] != None and data.iloc[st.session_state.user_index, index] != None and row[1][index] != "" and data.iloc[st.session_state.user_index, index] != ""):
                    differences += float(row[1][index]) - float(data.iloc[st.session_state.user_index, index])
                    differences_count += 1
                    if (differences_count == 1): weight_rows.append(row_index)
            
            if (differences_count != 0):
                average_difference = differences / differences_count
                weight_values.append(average_difference / 7)
            
            row_index += 1
        
        for column in data:
            if (data[column][st.session_state.user_index] != None and data[column][st.session_state.user_index] != ""):
                song_ratings[column] = float(data[column][st.session_state.user_index])
            else:
                rating_total = 0
                rating_count = 0
                
                for x in range(data[column].__len__()):
                    if (data[column][x] != None and data[column][x] != ""):
                        value = float(data[column][x])
                        
                        if (x in weight_rows):
                            rating_total += value - (value * weight_values[weight_rows.index(x)])                    
                            rating_count += 1
                        else:
                            rating_total += value
                            rating_count += 1
                
                song_ratings[column] = rating_total / rating_count

        song_ratings_sorted = dict(sorted(song_ratings.items(), key=lambda item: item[1], reverse=True))
        
        if (output == 'Best New Song'):
            song_outputted = False
            
            for song in song_ratings_sorted.items():
                if (data[song[0]][st.session_state.user_index] == None or data[song[0]][st.session_state.user_index] == ""):
                    st.write(song[0])
                    song_outputted = True
                    break
            
            if (song_outputted == False): st.write("You've listened to every song, there is no new song to recommend!")
        elif (output == 'Top N Songs'):
            song_count = 0
            
            for key in song_ratings_sorted:
                st.write(key)
                song_count += 1
                if (song_count == n): break
        elif (output == 'Raw Data'):
            st.dataframe(data)