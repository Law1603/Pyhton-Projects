import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    # Download the 'punkt' tokenizer models.
    nltk.download('punkt')

    # The URL of the article to be summarized.
    url = utext.get('1.0', "end").strip()
    # Create an Article object.
    article = Article(url)

    # Download the article.
    article.download()

    # Parse the article.
    article.parse()

    # Perform NLP tasks.
    article.nlp()

    # Display the results in the GUI
    title.config(state='normal')
    title.delete('1.0', "end")
    title.insert('1.0', article.title)
    title.config(state='disabled')

    author.config(state='normal')
    author.delete('1.0', "end")
    author.insert('1.0', ', '.join(article.authors))
    author.config(state='disabled')

    publication.config(state='normal')
    publication.delete('1.0', "end")
    publication.insert('1.0', str(article.publish_date))
    publication.config(state='disabled')

    summary.config(state='normal')
    summary.delete('1.0', "end")
    summary.insert('1.0', article.summary)
    summary.config(state='disabled')

    analysis = TextBlob(article.text)
    sentiment_analysis = f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}'
    sentiment.config(state='normal')
    sentiment.delete('1.0', "end")
    sentiment.insert('1.0', sentiment_analysis)
    sentiment.config(state='disabled')

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()

author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publishing Date')
plabel.pack()

publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

analysis = TextBlob('article.text')
print(analysis.polarity)
print(f'sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"})')


splabel = tk.Label(root, text="Sentiment Analysis")
splabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()

utext= tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
