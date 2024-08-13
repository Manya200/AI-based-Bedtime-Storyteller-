import os, openai, requests, datetime, random, time
import sys
def printinfo(character1_name_value,character1_type_value,character2_name_value,character2_type_value,venue_value,genre_value):
    try:
        def write_list(list_to_write, filename):
            for number, paragraph in enumerate(list_to_write):
                filepath = os.path.join(directory,f"{filename}-{number}.txt")
                with open(filepath, "w") as file:
                    file.write(paragraph)

        date_time_str = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        directory = os.path.abspath( f"Story {date_time_str}" )
        #directory = f"Story {date_time_str}"
        os.mkdir(directory)
        image_prompts, story_paragraphs = [], []


        char1_name = character1_name_value
        char1_type = character1_type_value
        char2_name = character2_name_value
        char2_type = character2_type_value
        venue_val = venue_value
        genre_val = genre_value

        story_prompt = f"Please write me a short {genre_val}\story. In this story, {char1_name} is a\
        {char1_type} and {char2_name} is a\
        {char2_type}. The story takes place{venue_val}.\
        For each paragraph, write me an image prompt for\
        an AI image generator. Each image prompt must\
        start in a new paragraph and have the words\
        'Image Prompt:' at the start. Choose a book\
        illustrator and put something in the image\
        prompts to say the images should be made in the\
        style of that artist."
        while len(image_prompts) == 0:
            print("Making ChatGPT request")
            openai.api_key = "Put ChatGPT API key here"
            ChatGPT_output = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "system",
                "content": "You are a children's author."},
                {"role": "user",
                "content": story_prompt}
            ])
            new_story = ChatGPT_output.choices[0].message["content"]
            print(new_story)
            for paragraph in new_story.split("\n\n"):
                if paragraph.startswith("Image Prompt"):
                 image_prompts.append(paragraph)
                else:
                    story_paragraphs.append(paragraph)
                    write_list(story_paragraphs, "story")
                    write_list(image_prompts, "prompt")
        # Move the image generation loop outside of the while loop
        for number, image_prompt in enumerate( image_prompts ):
            image_prompt += f"{char1_name} is {char1_type} and {char2_name} is{char2_type}. They are {venue_val}."
            print( f"Generating image {number}" )
            r = requests.post( "https://api.deepai.org/api/text2img",
                           data={'text': image_prompt, 'negative_prompt': "poorly drawn face, mutation, "
                                                                          "deformed, distorted face,extra limbs, "
                                                                          "bad anatomy", 'width': "720",
                                 'height': "720",
                                 'grid_size': "1"},
                           headers={'api-key': 'Put DeepAI key here'} )
            image_url = (r.json()["output_url"])
            print( f"Image {number} is at {image_url}. Saving now...\n\n" )
            filename = f"{number}.jpg"
            filepath = os.path.join(directory, filename)
            img_data = requests.get(image_url).content
            with open( filepath, 'wb') as handler:
                handler.write(img_data)

        print( f"Your files are in {directory}.")
        return {"status": "success", "directory": directory}

    except Exception as e:
        error_message = f"An error occurred in the printinfo function: {e}"
        print(error_message)
        return {"status": "error", "error_message": error_message}

