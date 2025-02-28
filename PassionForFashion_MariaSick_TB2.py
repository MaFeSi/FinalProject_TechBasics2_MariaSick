#Importing the streamlit library
import streamlit as st
#To set the page title as well as its icon (this can be seen in the browser tab)
st.set_page_config(page_title="PASSION FOR FASHION",
                   page_icon="🪡")

#To create a session state variable that safes the user's name
if 'name' not in st.session_state:
    st.session_state.name = ""

def main_page():
    st.image("images /Passion_for_Fashion.png", use_container_width=True) #To display an image as a nice introduction to my app

    st.subheader("Welcome to Passion for Fashion!✂️👗🪡")
    st.write("This app is your personal styling assistant. Not only will it help you learn more about your own style"
             " with a quiz and a style guide, but it will also assist you with creating cool new outfits with your own clothes."
             "\n\n Start your fashion journey now! I hope you'll have fun with my app!") #To set a second header that is bit smaller than the title
             #and to set a description with st.write describing what my app is about

    st.session_state.name = st.text_input("What is your name?") #Asking for the user's name and then storing it in session state

def get_style(answer_list):
    A_count = answer_list.count('A') #To get more specific results I created counters counting results A and B
    B_count = answer_list.count('B') #according to the user's answers

    if A_count > B_count: #This is an if-else-statement that returns a style depending on the counters results
        style = "Classic, Casual and Comfortable"
        description = ("You like to wear comfortable and classic looks with muted and neutral colors and simple accessories. "
                       " Go on to the next page to get some tips on improving your style choices even more!")
    elif B_count > A_count:
        style = "Extravagant, Brave and Eye-Catching"
        description = ("You like to wear extravagant and eye-catching outfits to attract everyones attention. There are never "
                       " too many colors or patterns in one outfit in your opinion and you like to wear bold accessories. "
                       " Go on to the next page to get some tips on improving your style choices even more!")

    else:
        style = "A versatile mix of Simple and Extravagant"
        description = ("You don't really fit in one style category. While you love to wear comfortable and casual clothing on one day,"
                       " you might wear eye-cathing statement pieces on another. It seems like you've found the right balance.")

    return style, description #Returns the determined style

def quiz_page():

    st.title("Quiz - What is your style?🪡") #To set the quiz page's title and a subheder with the saved user name
    st.subheader(f"Hi {st.session_state.name},")

    st.subheader("this quiz will help you find out more about your own style! Just answer a few of my questions:")

    answer_list = [] #To create an empty list that stores the quiz answers

    question_1 = st.radio("How would you describe your own style?", #All of the questions are displayed in a radio button format
                          ["Plain and Simple", "Extravagant with lots of accessories"])
    answer_list.append('A' if "Plain and Simple" in question_1 else 'B') #dependent on the user's answers the answers are saved as A or B

    question_2 = st.radio("What colors do you prefer?",
                          ["Neutral and Muted colors (Black, White, Grey)", "Bright and Popping Colors (Bright Red, Royal Blue)"])
    answer_list.append('A' if "Neutral and Muted colors (Black, White, Grey)" in question_2 else 'B')

    question_3 = st.radio("What accessories do you wear?",
                          ["Minimal", "Bold Jewelry"])
    answer_list.append('A' if "Minimal" in question_3 else 'B')

    question_4 = st.radio("Which outfit would you wear for a city trip?",
                          ["A subtle outfit that looks timeless, elegant and simple.", "An outfits that attracts a lot of attention."
                           " with lots of color"])
    answer_list.append('A' if "A subtle outfit that looks timeless, elegant and simple." in question_4 else 'B')

    question_5 = st.radio("Do you prefer...",
                          ["...simple, solid-coloured designs?", "...clothes with extravagant patterns and shapes?"])
    answer_list.append('A' if "...simple, solid-coloured designs?" in question_5 else 'B')

    question_6 = st.radio("Is it important to you how comfortable your clothes are?",
                          ["Yes, I prefer practical and comfortable clothes!", "I don't care, if my clothes are comfortable as long as they look cool!"])
    answer_list.append('A' if "Yes, I prefer practical and comfortable clothes!" in question_6 else 'B')

    question_7 = st.radio("What outfit would you wear at work?",
                          ["A simple shirt and jeans.","A suit or an elegant dress."])
    answer_list.append('A' if "A simple shirt and jeans." in question_7 else 'B')

    question_8 = st.radio("Do you prefer...",
                          ["...sneakers and loafers?", "...pumps and boots?"])
    answer_list.append('A' if "...sneakers and loafers?" in question_8 else 'B')

    #To display the results from the quiz
    if st.button("Your Results"):
        style, description = get_style(answer_list)

        st.subheader(f"Your style is: {style}") #To display the results
        st.write(description)
def guide_page():
    st.title("Your Style Guide🪡") #The purpose of the next page is then introduced with a title, subheader and introduction
    st.write("Now that you've found out what your style is, here's some advice for you on how to style perfect outfits for you."
             " Of course this is only meant to be an inspiration! If your comfortable with what you are wearing, please don't change anything about it"
             " because of others.")
    st.subheader("Classic, Casual and Comfortable:")
    st.write("You can't really go wrong with a simple and classic look, but it might sometimes lack some individuality.\n\n"
             "**Here are some tips to give your outfits a certain extra without you having to go out of your comfort zone**:\n\n"
             "- Wear multiple layers: by combining a white shirt with a sweater for example.\n\n"
             "- Wear accessories: Even the simplest accessories like a bracelett or a necklace will make your look more unique!\n\n"
             "- Mix and match shapes: If you wear a tight top with an oversized jacked or oversized jeans, the different shapes"
             "  will make your outfit look a bit more extra.")
    with st.expander("**Here are some outfit inspirations:**"): #The expander makes the app more interactive and clear
        c1, c2, c3 = st.columns(3) #By creating columns, it is possible to place multiple pictures or texts next to each other
        with c1:
            st.image("images /casual1.jpeg",
                     width=200)
        with c2:
            st.image("images /casual2.png",
                     width=210)
        with c3:
            st.image("images /casual3.jpeg",
                     width=215)

    st.subheader("Extravagant, Brave and Eye-Catching:")
    st.write("An extravagant and colorful look will attract a lot of attention, but it might sometimes be a bit over the top.\n\n"
        "**Here are a few tips to keep your outfits special and maintain your individuality without making it look too much**:\n\n"
        "- Don't mix and match too many patterns and colors: bright colors and cool patterns can look very cool together, but"
        "  sometimes they might not match or look weird together. Try to focus on just 2-3 colors. \n\n"
        "- Focus on one statement piece: It will look great if you build your outfits around one special and extravagant"
        "  statement piece!\n\n"
        "- Mix and match shapes: It's the same with simple and extravagant clothing. Different shaped clothes can make the outfits"
        "  look special without looking too much.")
    with st.expander("**Here are some outfit inspirations:**"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.image("images /extravagant1.jpeg",
                width=200)
        with c2:
            st.image("images /extravagant2.jpg",
                width=200)
        with c3:
            st.image("images /extravagant3.jpeg",
                width=210)
def upload_page():
    st.title("Your Outfit Generator🪡")
    st.write("This is your personal outfit generator. Just upload your own photos and create cool new outfits from your own "
             "closet!")

    for category in ["tops", "bottoms", "shoes", "accessories"]: #This creates session state variables to store uploaded images
        if category not in st.session_state:
            st.session_state[category] = [] #To create an empty list storing the uploaded images of every category
        if f"{category}_index" not in st.session_state:
            st.session_state[f"{category}_index"] = 0

    st.sidebar.header("Upload your own photos here") #I had help from ChatGpt with finding this upload function to upload your own pictures
    uploaded_files = {
        "tops": st.sidebar.file_uploader("Upload your tops", type=["png", "jpg", "jpeg"], accept_multiple_files=True),
        "bottoms": st.sidebar.file_uploader("Upload your bottoms", type=["png", "jpg", "jpeg"], accept_multiple_files=True),
        "shoes": st.sidebar.file_uploader("Upload your shoes", type=["png", "jpg", "jpeg"], accept_multiple_files=True),
        "accessories": st.sidebar.file_uploader("Upload your accessories", type=["png", "jpg", "jpeg"], accept_multiple_files=True)
    }
    #To store the uploaded files in the session state
    for category, files in uploaded_files.items():
        if files:
            st.session_state[category].extend(files)

    st.header("This is how your outfit looks at the moment:")

    def display_item(category, emoji, caption):
        col1, col2 = st.columns([3, 1]) #This creates two columns, a larger one for the images and a smaller one for the buttons
        with col1:
            if st.session_state[category]: #To display the current image from the uploaded category with a caption
                st.image(st.session_state[category][st.session_state[f"{category}_index"]], caption=caption, width=200)
            else:
                st.write(f"{emoji} No {caption.lower()} uploaded yet.") #This displays a message if no images have been uploaded

        with col2:
            if st.session_state[category]: #To only show the buttons if images exist
                if st.button(f"Next {caption}", key=f"{category}_btn"):
                    new_index = (st.session_state[f"{category}_index"] + 1) % len(st.session_state[category]) #To update the index to display the next image
                    st.session_state[f"{category}_index"] = new_index
                    st.rerun() #Reload the page to apply the change
    #to call the display function for each clothing category
    display_item("tops", "👕", "TOP")
    display_item("bottoms", "👖", "BOTTOM")
    display_item("shoes", "👟", "SHOES")
    display_item("accessories", "👜", "ACCESSORIES")

def info_page(): #Most of this page is made the same way as the other: a title, pictures and an expander with even more pictures)
    st.title("About Me🪡")
    st.write("Hi, my name is Maria. I have a huge passion for fashion and I love buying new clothes and express my personality"
             " through my style. Unfortunately, this tempts me to buy more and more clothes even though my closet is"
             " completely packed, which isn't very sustainable. That got me thinking, isn't there a way to keep track of"
             " all the clothes that we already have in our closet and create new outfits with them. You might have seen the film **Clueless*** where Cher"
             " is picking out her outfit with a computer programme. This inspired me to create an outfit generator just like hers! "
             " But while Cher is pretty confident and knows what clothes suits her, some may not have found their style. "
             " That's why I've added a quiz for you to find out what kind of style you have"
             " and then create new outfits inspired by my style guide.")

    c1, c2 = st.columns(2)
    with c1:
        st.image("images /Cher.jpeg",
        width=300)
    with c2:
        st.image("images /clueless.png",
        width=350)

    with st.expander("This is me and some of my outfits:"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.image("images /me1.jpg",
                     width=200)
        with c2:
            st.image("images /me2.jpg",
                     width=200)
        with c3:
            st.image("images /me3.jpg",
                     width=200)

st.sidebar.header("Menu") #The sidebar is set so the user can skip through all of the pages
options = ['Passion for Fashion', 'Quiz - What is your style?', "Your Style Guide", 'Your Outfit Generator', "About Me"]
page_selection = st.sidebar.selectbox("Choose a page", options)

if page_selection == "Passion for Fashion":
    main_page()
elif page_selection == "Quiz - What is your style?":
    quiz_page()
elif page_selection == "Your Style Guide":
    guide_page()
elif page_selection == "Your Outfit Generator":
    upload_page()
elif page_selection == "About Me":
    info_page()

def set_theme(theme_name): #This sidebar is particularly for changing the color themes depending on what the user wants.
    themes = {
        "Blue": {"background_color": "#298897", "sidebar_color": "#1A5966"},
        "Green": {"background_color": "#3F804E", "sidebar_color": "#2F6036"},
        "Red": {"background_color": "#BC6175", "sidebar_color": "#A0525F"},
        "Brown": {"background_color": "#8B4513", "sidebar_color": "#5E3010"},
        "Purple": {"background_color": "#6A0DAD", "sidebar_color": "#4B0082"}
    }
    #I had some help from ChatGpt finding out what the color codes are and creating this function that changes background and sidebar colors
    if theme_name in themes:
        theme = themes[theme_name]
        custom_css = f"""
        <style>
            .stApp {{
                background-color: {theme['background_color']};
            }}
            section[data-testid="stSidebar"] {{
                background-color: {theme['sidebar_color']};
            }}
        </style>
        """
        st.markdown(custom_css, unsafe_allow_html=True)

# This is the sidebar for collecting the color themes
theme_name = st.sidebar.selectbox("Choose a colour theme", ["Blue", "Green", "Red", "Brown", "Purple"], index=0)
set_theme(theme_name)



