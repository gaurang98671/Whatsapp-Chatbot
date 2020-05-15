import news
import weather
import dictionary
def reply_message(msg):
    if(msg=='news updates'):
        return news.news()

    if(msg.split()[0]=='weather'):
        return weather.get_weather(msg.split()[1])

    if(msg.split()[0]=='defination'):
        return  dictionary.get_defination(msg.split()[1])
    else:
        return "I dont understand"
