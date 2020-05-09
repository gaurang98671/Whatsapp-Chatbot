import news
import weather
def reply_message(msg):
    if(msg=='news updates'):
        return news.news()

    if(msg.split()[0]=='weather'):
        return weather.get_weather(msg.split()[1])
