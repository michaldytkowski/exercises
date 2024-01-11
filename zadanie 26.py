def clean_hashtags(r, w, length):
    with open(r, 'r') as file:
        content = file.read()
    hashtags = content.split()
    short_hashtags = [
        hashtag for hashtag in hashtags if len(hashtag) <= length + 1
    ]
    result = sorted(set(short_hashtags))
    with open(w, 'w') as file:
        for item in result:
            item = item + '\n'
            file.write(item)
 
 
clean_hashtags('hashtags.txt', 'clean.txt', 5)