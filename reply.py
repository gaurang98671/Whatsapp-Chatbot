import news
import weather
import dictionary
import tracker
def reply_message(msg):
    if(msg=='news updates'):
        return news.news()

    if(msg.split()[0]=='weather'):
        return weather.get_weather(msg.split()[1])

    if(msg.split()[0]=='defination'):
        return  dictionary.get_defination(msg.split()[1])

    if(msg.split()[0:2] ==['covid', 'update']):
        return tracker.get_corona_updates(msg.split()[2])

    else:
        return "I dont understand"
    
