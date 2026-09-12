
class Twitter:

    def __init__(self, content: str):
        self.content = content

    def content_post(self):
        return f"🐦 Tweet: '{self.content}' (280 chars max)"


class Instagram:

    def __init__(self, content):
        self.content = content

    def content_post(self):
        return f"📸 Instagram Post: '{self.content}' + ✨ filters"


class LinkedIn:

    def __init__(self, content):
        self.content = content

    def content_post(self):
        return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"


def notification(social_media):
    print(social_media.content_post())


twitter = Twitter("Ronaldo reported against coco-cola")
instagram = Instagram("Vibing with New Instagram features")
linkedin = LinkedIn("Top 5 Ways to master python in 2026")

notification(twitter)
notification(instagram)
notification(linkedin)
