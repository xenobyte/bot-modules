#
# This modules checks for news on the fulldisclosure list and informs
# the channel about it.
#

import sopel.module
import feedparser

url = 'http://seclists.org/rss/fulldisclosure.rss'
last_date = ""

@sopel.module.interval(3600) # run every hour
def read_rss(bot):
        # request the feed
        d = feedparser.parse(url)

        # store the pub date
        pub_date = d.feed.published
        global last_date

        if last_date != pub_date: # any news?
                last_date = pub_date
                for post in d.entries:
                        bot.msg("#root-shell", post.title + ": " + post.link)
