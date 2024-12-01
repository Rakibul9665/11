import os

def open_website(url):
    os.system(f"links {url}")

def toggle_flashlight(state):
    if state:
        os.system("termux-torch on")
    else:
        os.system("termux-torch off")

options = {
    1: ("Google", "https://www.google.com"),
    2: ("Facebook", "https://www.facebook.com"),
    3: ("YouTube", "https://www.youtube.com"),
    4: ("Twitter", "https://www.twitter.com"),
    5: ("Instagram", "https://www.instagram.com"),
    6: ("LinkedIn", "https://www.linkedin.com"),
    7: ("Reddit", "https://www.reddit.com"),
    8: ("WhatsApp", "https://www.whatsapp.com"),
    9: ("Amazon", "https://www.amazon.com"),
    10: ("Netflix", "https://www.netflix.com"),
    11: ("Microsoft", "https://www.microsoft.com"),
    12: ("Apple", "https://www.apple.com"),
    13: ("Spotify", "https://www.spotify.com"),
    14: ("Wikipedia", "https://www.wikipedia.org"),
    15: ("GitHub", "https://www.github.com"),
    16: ("Stack Overflow", "https://stackoverflow.com"),
    17: ("Quora", "https://www.quora.com"),
    18: ("Yahoo", "https://www.yahoo.com"),
    19: ("Bing", "https://www.bing.com"),
    20: ("Medium", "https://medium.com"),
    21: ("Pinterest", "https://www.pinterest.com"),
    22: ("Tumblr", "https://www.tumblr.com"),
    23: ("Vimeo", "https://www.vimeo.com"),
    24: ("Discord", "https://www.discord.com"),
    25: ("Slack", "https://www.slack.com"),
    26: ("Dropbox", "https://www.dropbox.com"),
    27: ("Google Drive", "https://www.drive.google.com"),
    28: ("OneDrive", "https://www.onedrive.com"),
    29: ("Gmail", "https://mail.google.com"),
    30: ("Outlook", "https://outlook.live.com"),
    31: ("ProtonMail", "https://protonmail.com"),
    32: ("Yahoo Mail", "https://mail.yahoo.com"),
    33: ("AOL Mail", "https://mail.aol.com"),
    34: ("Hotmail", "https://outlook.live.com/owa/"),
    35: ("WordPress", "https://www.wordpress.com"),
    36: ("Blogger", "https://www.blogger.com"),
    37: ("Wix", "https://www.wix.com"),
    38: ("Squarespace", "https://www.squarespace.com"),
    39: ("Weebly", "https://www.weebly.com"),
    40: ("Etsy", "https://www.etsy.com"),
    41: ("AliExpress", "https://www.aliexpress.com"),
    42: ("eBay", "https://www.ebay.com"),
    43: ("Flipkart", "https://www.flipkart.com"),
    44: ("Best Buy", "https://www.bestbuy.com"),
    45: ("Walmart", "https://www.walmart.com"),
    46: ("Target", "https://www.target.com"),
    47: ("BBC News", "https://www.bbc.com/news"),
    48: ("CNN", "https://www.cnn.com"),
    49: ("The New York Times", "https://www.nytimes.com"),
    50: ("The Guardian", "https://www.theguardian.com"),
    51: ("Flashlight ON", "flashlight_on"),
    52: ("Flashlight OFF", "flashlight_off"),
}

def menu():
    print("Select an option:")
    for key, value in options.items():
        print(f"{key}. {value[0]}")

    choice = int(input("Enter your choice: "))
    if choice in options:
        if options[choice][1] == "flashlight_on":
            toggle_flashlight(True)
        elif options[choice][1] == "flashlight_off":
            toggle_flashlight(False)
        else:
            open_website(options[choice][1])
    else:
        print("Invalid choice")

if __name__ == "__main__":
    menu()
