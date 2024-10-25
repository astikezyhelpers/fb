# import requests

# # Replace these values with your information
# PAGE_ACCESS_TOKEN='EACGFJsgP3fABO6Rq9DFPiT0ZAca7UlWjtvy5T6cYfpijKLdhyZCcmJtlM1GkwsyUBE1O01jdDattf47Qfo90K2p6YuTRtKTuWDUZCSzHDUlPicwUqx1BiDo9b0QXysIWBxw99B49qu7Px5kiWVz4edNBDGI7epQCxBP1V889SQxMmx6UxZCql8ArOj0MilCPnZAUOYtWVWZA11227EAQ0siCxXCK0Gpklq'
# PAGE_ID = '61567518574754'
# IMAGE_PATH = 'image.png'
# CAPTION = 'This is a test caption for the image.'

# # Facebook API endpoint for uploading a photo to a Page
# url = f'https://graph.facebook.com/v18.0/{PAGE_ID}/photos'

# # Prepare the payload
# payload = {
#     'access_token': PAGE_ACCESS_TOKEN,
#     'caption': CAPTION
# }

# # Open the image file in binary mode
# files = {
#     'source': open(IMAGE_PATH, 'rb')
# }

# # Send the POST request to the Facebook API
# response = requests.post(url, data=payload, files=files)

# # Check the response
# if response.status_code == 200:
#     print('Photo uploaded successfully!')
# else:
#     print(f'Error: {response.json()}')



import requests

# # Replace these values with your information
PAGE_ACCESS_TOKEN='EACGFJsgP3fABO6Rq9DFPiT0ZAca7UlWjtvy5T6cYfpijKLdhyZCcmJtlM1GkwsyUBE1O01jdDattf47Qfo90K2p6YuTRtKTuWDUZCSzHDUlPicwUqx1BiDo9b0QXysIWBxw99B49qu7Px5kiWVz4edNBDGI7epQCxBP1V889SQxMmx6UxZCql8ArOj0MilCPnZAUOYtWVWZA11227EAQ0siCxXCK0Gpklq'
PAGE_ID = '393979580475676'
# IMAGE_PATH = 'image.png'
# CAPTION = 'This is a test caption for the image.'

# Replace these values with your information
# PAGE_ACCESS_TOKEN = 'your_page_access_token'
# PAGE_ID = 'your_page_id'
VIDEO_PATH = 'video.mp4'
TITLE = 'Educating through Ezygamers'
DESCRIPTION = 'This is a test description for the video.'

# Facebook API endpoint for uploading a video to a Page
url = f'https://graph.facebook.com/v18.0/{PAGE_ID}/videos'

# Prepare the payload
payload = {
    'access_token': PAGE_ACCESS_TOKEN,
    'title': TITLE,
    'description': DESCRIPTION
}

# Open the video file in binary mode
files = {
    'source': open(VIDEO_PATH, 'rb')
}

# Send the POST request to the Facebook API
response = requests.post(url, data=payload, files=files)

# Check the response
if response.status_code == 200:
    print('Video uploaded successfully!')
else:
    print(f'Error: {response.json()}')
