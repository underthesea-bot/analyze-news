from underthesea import word_tokenize

from utils import Github, Repository, USERNAME, PASSWORD, REPO_OWNER, REPO_NAME


class Propose:
    def __init__(self):
        self.github = Github(USERNAME, PASSWORD)
        self.repository = Repository(REPO_OWNER, REPO_NAME)

    def submit(self):
        pass


class WordTokenizePropose(Propose):
    def __init__(self):
        Propose.__init__(self)

    def submit(self, text):
        labels = ["data", "data-word-tokenize"]
        title = 'Thêm một câu vào dữ liệu tách từ'
        body = 'Body text'
        self.github.create_issue(self.repository, title, body, assignee=None, labels=self.labels)


for line in open("titles.txt")[:2]:
    text = line.strip()
    tokenized_text = word_tokenize(text, format="text")
    wtp = WordTokenizePropose()
    wtp.submit(tokenized_text)
