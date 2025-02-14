from life import WordCloud
import matplotlib.pyplot as plt

text = """I grew in a multicultural family where I was taught mainly English and French and later I got to also learn German. 
I used to speak English at home with my mum and brother and used to speak Romanian with my grandmother. 
As soon as I grew I was also able to speak with my auntie French. 
My family always wanted me to know foreign languages. 
At my Grandmother's house I've had my childhood with German, English and French kids. 
Later I developed myself, studied and worked in the UK and in a few years' time, I also managed to pave my way to the German community 
where I could spend time more with my fellow German friends. 
I am glad to have developed such an international lifestyle."""

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
