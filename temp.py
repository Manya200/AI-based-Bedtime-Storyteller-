import os, openai, requests, datetime, random,time
def write_list(list_to_write, filename):
    for number, paragraph in enumerate(list_to_write):
        filepath = os.path.join(directory,f"{filename}-{number}.txt")
        with open(filepath, "w") as file:
            file.write(paragraph)
date_time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
directory = f"Story {date_time_str}"
os.mkdir(directory)
image_prompts, story_paragraphs = [], []
character1_name = input("What is your main character's name? ")
character1_type = input("What kind of a character is that? ")
character2_name = input("What is your second character's name? ")
character2_type = input("And what kind of a character is that? ")
venue = input("Where does the story take place? (e.g. in acastle, on Mars) ")
genre = input("What is your story genre? ")
story_prompt = f"Please write me a short {genre}\story. In this story, {character1_name} is a\{character1_type} and {character2_name} is a\{character2_type}. The story takes place{venue}.\
For each paragraph, write me an image prompt for\
an AI image generator. Each image prompt must\
start in a new paragraph and have the words\
'Image Prompt:' at the start. Choose a book\
illustrator and put something in the image\
prompts to say the images should be made in the\
style of that artist."
while len(image_prompts) == 0:
    print("Making ChatGPT request")
    openai.api_key = "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" ### PUT YOUR API KEY HERE
    ChatGPT_output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system",
        "content": "You are a children's author."},
        {"role": "user",
        "content": story_prompt}
    ] )
    new_story = ChatGPT_output.choices[0].message["content"]
    print( new_story )
    for paragraph in new_story.split( "\n\n" ):
        if paragraph.startswith("Image Prompt" ):
            image_prompts.append( paragraph )
        else:
            story_paragraphs.append( paragraph )
            write_list( story_paragraphs, "story" )
            write_list( image_prompts, "prompt" )
    for number, image_prompt in enumerate(image_prompts ):
        image_prompt += f"{character1_name} is{character1_type} and {character2_name} is{character2_type}.They are{venue}."
        print( f"Generating image {number}" )
        r = requests.post( "https://api.deepai.org/api/text2img", data={'text': image_prompt,'negative_prompt': "poorly drawn face, mutation, deformed, distorted face,extra limbs, bad anatomy",'width': "720", 'height': "720",'grid_size': "1"},
        headers={'api-key': '3df7a8ca-168d-4306-be54-2e3eb1ed9a67'}
                           ### PUT YOUR API KEY HERE
        )
        image_url = (r.json()["output_url"])

        print( f"Image {number} is at {image_url}.Saving now...\n\n" )
        filename = f"{number}.jpg"
        filepath = os.path.join( directory, filename )
        img_data = requests.get( image_url ).content
        with open( filepath, 'wb' ) as handler:
            handler.write( img_data )
print( f"Your files are in {directory}." )
