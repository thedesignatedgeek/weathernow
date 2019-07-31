Things to note...

1) This project is far from being complete.  As with many projects, especially mine, scope creeps greatly.  What I started out to do, was to prove that Tkinter projects don't have to "look like something out of Windows 95".  I believe that I've done that.  I also wanted to, as I often do, push my envelope and learn just how far I could push my knowledge of Python and Tkinter programming to it's logical limits.  Again, I believe I've done that.  However, I always want my programs to do more, and my learning to go past the limits of today, even if I don't quite remember just what I was doing on tomorrow.

2) I used Page to design the base UI.  So roughly 90% of the "glory" is due to Page and Don.  Page makes my programming life so very easy and gives me a huge latitude to push the envelope.

3) About the "dark theme".  This was all done in Page, with the exception of the code to remove the "standard" title bar.  The background of all the widgets, with the exception of the ttk.combobox widgets, was set to "#595959" and the foreground was set to "#ffffff".  I tried to make the font for many of the widgets to be "Ubuntu Condensed" or "Ubuntu".  These are easy to add to Linux systems, if it is not there by default.  The widgets that don't have one of those two fonts, use the "default" TKFont, which in my case is "DejaVu Sans".  I haven't tried very hard to change the background/foreground of the ttk.combobox widgets.  The "standard" title bar is removed, not by using the "root.overrideredirect(True)" command.  This is because that process also makes the topmost form fully modal.  While this is helpful in a splash screen, it is not helpful for a normal desktop application, that needs to be moved, minimized, restored and allow for keyboard input.  While, there are tricks that allow for the form to be moved, and in fact I use some of these tricks in this program, the biggest issues are:
    a) Lack of easy keyboard input into the form.
    b) You can't have another modal form on top of a modal form.
Instead, I use three wm_attributes calls that allow the desired look, while allowing the required abilities.  These are:
    root.wm_attributes('-topmost', False)
    root.wm_attributes('-fullscreen', False)
    root.wm_attributes('-type', 'splash')
The "false" title bar is simply a standard frame on top of the standard topmost form, which is sized to be the same width as the form.  A standard label is placed within the frame, as is a standard button.  The button and label are both set to a flat relief mode.  In the 'init' function, both the frame and label have bindings to the <B1-Motion> and <Button-1> events and have the callbacks set to 'move_window' and 'get_pos' respectively.  This allows the form to be moved as in a "normal" desktop application.

4) The "hourly block" that shows a 5 hour forecast with the hour, the expected temperature and an icon showing the general weather conditions.  Each of the widgets that shows the icons, are standard labels.  I alias these labels and place these aliases into a list to be able to manipulate them easily.  (see function 'widgets_to_list()'...
hourlyWidgets = [w.Label5, w.Label6, w.Label7, w.Label8, w.Label9]
When the program needs to load/update the graphics (and text) (see function 'displayHourly'), there are 5 variables that are created:
img1 = img2 = img3 = img4 = img5 = None
and put into a list:
imglist = [img1, img2, img3, img4, img5]
The list 'imglist' was declared as global at the head of the function.  The filename of the icon matches (generally) the icon name data coming from the data.  Then, in standard practice, the image holder is set as the return from 'tkPhotoImage()' and then the image property is set for the proper label based on an index:
hourlyWidgets[indx].configure(image=imglist[indx])
The individual time and temperature labels are handled in a similar manner.

5) The data comes from the darksky.net API using a "secret" api_key.  This is a free access key that allows up to 1000 API calls per day for no cost.  The function 'ask_web() is the routine that handles the internet request, building a URL string that include the latitude and longitude for the location in question.  The data is returned in a json data structure.  Once we have the structure, it is saved to a json file named 'data2.json'.  I do this to be able to develop, enhance and troubleshoot the program without incurring too many API calls.  On average, I have made less than 40 API calls on any given day, and rarely over 10 calls per day. See https://darksky.net/dev/docs for a full discussion on the API and it's calls.

6) Since the darksky data can be set to a number of languages and display units (mph, kmh, etc), that capability is supported.  Some of the supported languages are Norwegian, Spanish, German, English and more.  However, the only data that is in the requested data is the raw data itself, i.e. summary data.  The json keys are all in English.  For example:
summary:	"Lettskyet i løpet av de neste timene."
Which translates to English as "Overcast over the next few hours.".  Notice however the key ('summary') is in english.  Not knowing any spoken/written languages besides English and Bad English, I wouldn't know how to translate the labels on the form like 'Wind:', 'Pressure', etc. and it seems that it would be silly to leave the label prompts in English and display the information is Norwegian or Spanish.  With a bit of research, I found that there is (at least for the moment) a way to access the GoogleTranslateAPI for free.  I will be working on this and hopefully be done before I released the program to you.  There are many more languages supported by the API, but I needed to limit the number that this program would support to 11.  Other languages can be supported by a few modifications to the code. (see function 'load_lang_units() )

7) My coding style is, as has been for almost 40 years, one that lends itself to teaching.  I really didn't try to be pythonic in style.  Sorry, but that's just how I do things.  One more thing about the code itself.  This program is the result of about 5 different proof of concept type attempts, cobbled  together into this (currently) mess.  I'm lazy, so there are some routines/globals/variables that probably dont' make sense.  Hopefully, I will eventually be able to get it all straightened out into something that works.

8) Required libraries that would need to be installed before running the program are currently only the following:
    requests
    geopy
Both of these can be installed through pip3 or pip depending on your system.

9) Future directions.  I would like to support a popup form for weather alert data and eventually one for historical weather data.  I'm not sure how soon this would be implemented.

EOF


